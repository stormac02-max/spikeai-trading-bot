"""Backtest futures strategies on Hyperliquid's daily history, using the simulator's rules.

Universe: every Monday 00:00 UTC, the 20 most-traded perps by trailing 7-day volume (excluding BTC and
ETH) that have at least 51 days of history. Delisted markets are included while they traded, so dead
coins aren't silently left out.

Each strategy trades the universe with the same settings: 5x leverage (capped at the coin's max),
$500 margin per position, $10,000 starting balance, 0.045% taker fee plus 5 bp slippage per fill.

Simplifications versus the live simulator (paper_futures.py):
- Daily candles: signals and trades happen at each day's close (00:00 UTC). Stops and liquidations are
  checked against the day's high and low; if a day touches both, the nearer level is taken first.
- Funding uses Hyperliquid's baseline rate (0.00125% an hour, paid by longs to shorts), not the actual
  hourly history, which would take thousands of API calls.
- Each coin's leverage cap is its current one.

Usage:
  python backtest_futures.py                 # 365 days, with and without an 8% stop
  python backtest_futures.py --days 180
"""

import argparse
import pickle
import time
from pathlib import Path

import pandas as pd

from paper_futures import hl_info, liquidation_price, unrealized_pnl

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DAY_MS = 86_400_000

UNIVERSE_SIZE = 20
EXCLUDE = {"BTC", "ETH"}
MIN_HISTORY = 51
LEVERAGE = 5
MARGIN = 500.0
START_BALANCE = 10_000.0
TAKER_FEE = 0.00045
SLIPPAGE = 0.0005
FUNDING_PER_DAY = 0.0000125 * 24  # baseline hourly rate x 24, longs pay shorts


# ---- data ----------------------------------------------------------------------

def fetch_history(days):
    """Daily candles for every Hyperliquid perp (live and delisted), cached per day in data/."""
    DATA_DIR.mkdir(exist_ok=True)
    cache = DATA_DIR / f"hl_daily_{days}d_{time.strftime('%Y%m%d')}.pkl"
    if cache.exists():
        return pickle.loads(cache.read_bytes())

    universe = hl_info({"type": "meta"})["universe"]
    end = int(time.time() * 1000) // DAY_MS * DAY_MS  # today 00:00 UTC: only finished days
    start = end - (days + MIN_HISTORY + 30) * DAY_MS
    frames, max_lev = {}, {}
    for i, asset in enumerate(universe, 1):
        coin = asset["name"]
        max_lev[coin] = asset["maxLeverage"]
        for attempt in range(5):
            try:
                rows = hl_info({"type": "candleSnapshot",
                                "req": {"coin": coin, "interval": "1d", "startTime": start, "endTime": end - 1}})
                break
            except Exception as error:  # rate limit or network hiccup: back off and retry
                time.sleep(5 * (attempt + 1))
        else:
            raise RuntimeError(f"could not fetch {coin}: {error}")
        if rows:
            df = pd.DataFrame(rows)
            df.index = pd.to_datetime(df["t"], unit="ms", utc=True)
            frames[coin] = df[["o", "h", "l", "c", "v"]].astype(float)
        if i % 25 == 0:
            print(f"  fetched {i}/{len(universe)} markets")
        time.sleep(1.3)  # stay under the API's rate limit

    data = {field: pd.DataFrame({coin: f[field] for coin, f in frames.items()}).sort_index()
            for field in ("o", "h", "l", "c", "v")}
    data["usd_volume"] = data["v"] * data["c"]
    data["max_lev"] = max_lev
    cache.write_bytes(pickle.dumps(data))
    return data


def weekly_universes(data, days):
    """{Monday date: [coins]} chosen from the 7 days before each Monday."""
    closes, volume = data["c"], data["usd_volume"]
    history = closes.notna().cumsum()
    first_day = closes.index[-1] - pd.Timedelta(days=days - 1)
    universes = {}
    for day in closes.index[closes.index >= first_day]:
        if day.dayofweek != 0:  # Monday
            continue
        past = volume.loc[day - pd.Timedelta(days=7): day - pd.Timedelta(days=1)]
        ranked = past.sum().sort_values(ascending=False)
        eligible = [c for c in ranked.index
                    if c not in EXCLUDE and ranked[c] > 0
                    and history.loc[:day - pd.Timedelta(days=1), c].iloc[-1] >= MIN_HISTORY
                    and pd.notna(closes.loc[day, c])]
        universes[day] = eligible[:UNIVERSE_SIZE]
    return universes


# ---- simulated account ---------------------------------------------------------

class Backtest:
    def __init__(self, data, stop_pct, leverage=LEVERAGE):
        self.data, self.stop_pct, self.leverage = data, stop_pct, leverage
        self.balance = START_BALANCE
        self.positions = {}
        self.trades = []
        self.fees = self.funding = 0.0

    def open(self, coin, side, price):
        if coin in self.positions:
            return
        lev = min(self.leverage, self.data["max_lev"].get(coin, 3))
        fill = price * (1 + SLIPPAGE if side == "long" else 1 - SLIPPAGE)
        notional = MARGIN * lev
        fee = notional * TAKER_FEE
        if MARGIN + fee > self.balance:
            return  # not enough free balance: skip, like the live account would
        stop = None
        if self.stop_pct:
            stop = fill * (1 - self.stop_pct) if side == "long" else fill * (1 + self.stop_pct)
        self.positions[coin] = {"side": side, "size": notional / fill, "entry": fill, "margin": MARGIN,
                                "mm_rate": 1 / (2 * self.data["max_lev"].get(coin, 3)), "stop": stop}
        self.balance -= MARGIN + fee
        self.fees += fee

    def close(self, coin, price, reason, slip=True):
        pos = self.positions.pop(coin)
        if slip:
            price = price * (1 - SLIPPAGE if pos["side"] == "long" else 1 + SLIPPAGE)
        pnl = unrealized_pnl(pos, price)
        fee = price * pos["size"] * TAKER_FEE
        result = max(pos["margin"] + pnl - fee, 0.0)  # isolated margin: loss stops at the margin
        if result == 0.0:
            reason = "liquidation"
        self.balance += result
        self.fees += fee if result else 0.0
        self.trades.append({"coin": coin, "side": pos["side"], "pnl": result - MARGIN, "reason": reason})

    def intraday_exits(self, day):
        h, l = self.data["h"].loc[day], self.data["l"].loc[day]
        for coin in list(self.positions):
            pos = self.positions[coin]
            if pd.isna(h.get(coin)):
                continue
            long = pos["side"] == "long"
            levels = [("liquidation", liquidation_price(pos))]
            if pos["stop"]:
                levels.append(("stop-loss", pos["stop"]))
            levels.sort(key=lambda lv: -lv[1] if long else lv[1])
            for kind, level in levels:
                if (l[coin] <= level) if long else (h[coin] >= level):
                    if kind == "liquidation":
                        self.positions.pop(coin)
                        self.trades.append({"coin": coin, "side": pos["side"], "pnl": -MARGIN, "reason": kind})
                    else:
                        self.close(coin, level, kind, slip=False)
                    break

    def daily_funding(self, day):
        closes = self.data["c"].loc[day]
        for coin, pos in self.positions.items():
            if pd.isna(closes.get(coin)):
                continue
            payment = pos["size"] * closes[coin] * FUNDING_PER_DAY
            change = -payment if pos["side"] == "long" else payment
            pos["margin"] += change
            self.funding += change

    def equity(self, closes):
        """Balance plus open positions' margin and unrealized profit at `closes` (last known prices)."""
        return self.balance + sum(p["margin"] + unrealized_pnl(p, closes[c]) for c, p in self.positions.items())


# ---- strategies (each called at every day's close) -----------------------------

def ma_crossover(bt, day, universe, data, ind, rebalance):
    s, l = ind["sma20"], ind["sma50"]
    i = data["c"].index.get_loc(day)
    for coin in universe:
        prev_s, prev_l, cur_s, cur_l = s[coin].iloc[i - 1], l[coin].iloc[i - 1], s[coin].iloc[i], l[coin].iloc[i]
        if pd.isna(prev_l) or pd.isna(cur_l):
            continue
        price = data["c"].loc[day, coin]
        pos = bt.positions.get(coin)
        if prev_s <= prev_l and cur_s > cur_l:
            if pos and pos["side"] == "short":
                bt.close(coin, price, "signal")
            if coin not in bt.positions:
                bt.open(coin, "long", price)
        elif prev_s >= prev_l and cur_s < cur_l:
            if pos and pos["side"] == "long":
                bt.close(coin, price, "signal")
            if coin not in bt.positions:
                bt.open(coin, "short", price)


def breakout(bt, day, universe, data, ind, rebalance):
    for coin in universe:
        price = data["c"].loc[day, coin]
        hh20, ll20 = ind["hh20"].loc[day, coin], ind["ll20"].loc[day, coin]
        hh10, ll10 = ind["hh10"].loc[day, coin], ind["ll10"].loc[day, coin]
        if pd.isna(hh20) or pd.isna(price):
            continue
        pos = bt.positions.get(coin)
        if pos and pos["side"] == "long" and price < ll10:
            bt.close(coin, price, "signal")
        elif pos and pos["side"] == "short" and price > hh10:
            bt.close(coin, price, "signal")
        if coin not in bt.positions:
            if price > hh20:
                bt.open(coin, "long", price)
            elif price < ll20:
                bt.open(coin, "short", price)


def momentum(bt, day, universe, data, ind, rebalance, picks=5):
    if not rebalance:
        return  # only trades weekly; stops still apply in between
    ret = ind["ret14"].loc[day, universe].dropna().sort_values()
    targets = {c: "long" for c in ret.index[-picks:]} | {c: "short" for c in ret.index[:picks]}
    for coin in list(bt.positions):
        if targets.get(coin) != bt.positions[coin]["side"]:
            bt.close(coin, data["c"].loc[day, coin], "rebalance")
    for coin, side in targets.items():
        if coin not in bt.positions:
            bt.open(coin, side, data["c"].loc[day, coin])


STRATEGIES = {"MA crossover 20/50": ma_crossover, "Breakout 20/10": breakout, "Momentum 14d, 5 long/5 short": momentum}


def run(data, universes, strategy, stop_pct, leverage=LEVERAGE):
    closes = data["c"]
    last_known = closes.ffill()
    ind = {
        "sma20": closes.rolling(20).mean(), "sma50": closes.rolling(50).mean(),
        "hh20": data["h"].rolling(20).max().shift(1), "ll20": data["l"].rolling(20).min().shift(1),
        "hh10": data["h"].rolling(10).max().shift(1), "ll10": data["l"].rolling(10).min().shift(1),
        "ret14": closes / closes.shift(14) - 1,
    }
    bt = Backtest(data, stop_pct, leverage)
    days = closes.index[closes.index >= min(universes)]
    universe, curve = [], []
    for day in days:
        bt.intraday_exits(day)
        bt.daily_funding(day)
        # Delisted or no price today: close at the last known price.
        for coin in list(bt.positions):
            if pd.isna(closes.loc[day, coin]):
                bt.close(coin, closes.loc[:day, coin].dropna().iloc[-1], "delisted")
        rebalance = day in universes
        if rebalance:
            universe = universes[day]
            for coin in list(bt.positions):
                if coin not in universe:
                    bt.close(coin, closes.loc[day, coin], "left universe")
        strategy(bt, day, universe, data, ind, rebalance)
        curve.append(bt.equity(last_known.loc[day]))
    curve = pd.Series(curve, index=days)
    trades = pd.DataFrame(bt.trades)
    peak = curve.cummax()
    return {
        "final": curve.iloc[-1],
        "return_pct": (curve.iloc[-1] / START_BALANCE - 1) * 100,
        "max_dd_pct": ((curve - peak) / peak).min() * 100,
        "trades": len(trades),
        "win_rate": (trades["pnl"] > 0).mean() * 100 if len(trades) else 0.0,
        "stops": int((trades["reason"] == "stop-loss").sum()) if len(trades) else 0,
        "liquidations": int((trades["reason"] == "liquidation").sum()) if len(trades) else 0,
        "fees": bt.fees,
        "funding": bt.funding,
        "curve": curve,
    }


def benchmark(data, universes):
    """Equal-weight, unleveraged long of the weekly universe (no fees): what simply holding them did."""
    closes = data["c"]
    rets = closes.pct_change()
    days = closes.index[closes.index >= min(universes)]
    value, universe, curve = START_BALANCE, [], []
    for day in days:
        if universe:
            value *= 1 + rets.loc[day, universe].fillna(0).mean()
        if day in universes:
            universe = universes[day]
        curve.append(value)
    curve = pd.Series(curve, index=days)
    peak = curve.cummax()
    return curve.iloc[-1], (curve.iloc[-1] / START_BALANCE - 1) * 100, ((curve - peak) / peak).min() * 100


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--days", type=int, default=365)
    args = parser.parse_args()

    data = fetch_history(args.days)
    universes = weekly_universes(data, args.days)
    members = sorted({c for u in universes.values() for c in u})
    print(f"{len(universes)} weekly universes, {len(members)} different coins were in the top 20 at some point")

    final, ret, dd = benchmark(data, universes)
    print(f"\nBenchmark, hold the top 20 equally at 1x: {ret:+.1f}% (worst drawdown {dd:.1f}%)\n")
    print(f"{'strategy':32} {'stop':>5} {'final $':>10} {'return':>8} {'max DD':>8} {'trades':>7} "
          f"{'win %':>6} {'stops':>6} {'liqs':>5} {'fees $':>8} {'funding $':>10}")
    results = {}
    for name, fn in STRATEGIES.items():
        for stop in (0.08, None):
            r = run(data, universes, fn, stop)
            results[(name, stop)] = r
            print(f"{name:32} {'8%' if stop else 'none':>5} {r['final']:>10,.0f} {r['return_pct']:>+7.1f}% "
                  f"{r['max_dd_pct']:>7.1f}% {r['trades']:>7} {r['win_rate']:>6.1f} {r['stops']:>6} "
                  f"{r['liquidations']:>5} {r['fees']:>8,.0f} {r['funding']:>+10,.0f}")
    return results


if __name__ == "__main__":
    main()
