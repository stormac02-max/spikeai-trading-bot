"""Simulated spot paper trading account, on Kraken's real public market data.

The spot twin of paper_futures.py: buy-only, no leverage, no funding, no liquidation.
- Buys and sells fill at the average price you'd get by walking Kraken's live order book.
- Fees work like Alpaca's crypto fees (0.25% taker by default): a buy delivers 0.25% fewer coins,
  and a sell pays out 0.25% fewer dollars, so the simulation is comparable with the Alpaca mirror.
- sync() replays every finished hour since the last sync from Kraken's hourly candles, so a
  stop-loss hit at 3 AM is applied at 3 AM at the stop price (or the hour's open, if it gapped past).

Coins use spot names. Hyperliquid's "k" coins are quoted per 1,000 (kPEPE), so spot_name() strips
the k (PEPE). Kraken was chosen because it lists all of the weekly top-20 coins and, being a US
exchange, its public API is reachable from GitHub's US servers. No keys are needed.

The account is saved as JSON (state/spot_<strategy>.json, chosen by the caller).
"""

import json
import logging
import time
from datetime import datetime, timezone

import requests

from paper_futures import BASE_DIR, HOUR_MS, iso, now_ms

KRAKEN = "https://api.kraken.com/0/public"
ALIASES = {"XBT": "BTC", "XDG": "DOGE"}  # Kraken's names for a few coins
QUOTES = ("USD", "USDT", "USDC")  # preferred quote currencies, in order

log = logging.getLogger("paper_spot")
_pairs = None


def spot_name(coin):
    """Hyperliquid name -> spot coin: kPEPE -> PEPE (k-coins are quoted per 1,000)."""
    return coin[1:] if coin.startswith("k") and coin[1:].isupper() else coin


def kraken(path, **params):
    response = requests.get(f"{KRAKEN}/{path}", params=params, timeout=30)
    response.raise_for_status()
    data = response.json()
    if data.get("error"):
        raise RuntimeError(f"Kraken {path}: {data['error']}")
    return data["result"]


def kraken_pairs():
    """{coin: (altname, result key)} for coins with a USD (or USDT/USDC) spot pair on Kraken."""
    global _pairs
    if _pairs is None:
        best = {}
        for key, p in kraken("AssetPairs").items():
            if "wsname" not in p or p.get("status", "online") != "online":
                continue
            base, quote = p["wsname"].split("/")
            base = ALIASES.get(base, base)
            if quote in QUOTES and (base not in best or QUOTES.index(quote) < QUOTES.index(best[base][2])):
                best[base] = (p["altname"], key, quote)
        _pairs = {coin: (alt, key) for coin, (alt, key, _) in best.items()}
    return _pairs


def kraken_pair(coin):
    pairs = kraken_pairs()
    if coin not in pairs:
        raise RuntimeError(f"{coin} has no USD spot pair on Kraken")
    return pairs[coin]


def get_prices(coins):
    """Last traded price for each coin that Kraken lists: {coin: price}."""
    pairs = {c: kraken_pairs()[c] for c in coins if c in kraken_pairs()}
    if not pairs:
        return {}
    result = kraken("Ticker", pair=",".join(alt for alt, _ in pairs.values()))
    by_key = {key: coin for coin, (_, key) in pairs.items()}
    by_alt = {alt: coin for coin, (alt, _) in pairs.items()}
    prices = {}
    for key, ticker in result.items():
        coin = by_key.get(key) or by_alt.get(key)
        if coin:
            prices[coin] = float(ticker["c"][0])
    return prices


def get_hourly(coin, since_ms):
    """Finished hourly candles since `since_ms`: [{t, o, h, l, c}] (t = start, ms)."""
    alt, _ = kraken_pair(coin)
    result = kraken("OHLC", pair=alt, interval=60, since=int(since_ms // 1000) - 1)
    rows = next(v for k, v in result.items() if k != "last")
    current_hour = now_ms() // HOUR_MS * HOUR_MS
    return [{"t": int(r[0]) * 1000, "o": float(r[1]), "h": float(r[2]), "l": float(r[3]), "c": float(r[4])}
            for r in rows if since_ms <= int(r[0]) * 1000 < current_hour]


def fill(coin, side, notional=None, size=None):
    """Market order against Kraken's live book. `notional` in USD to buy, or `size` in coins to sell.

    Returns (average price, coins filled).
    """
    alt, _ = kraken_pair(coin)
    book = next(iter(kraken("Depth", pair=alt, count=500).values()))
    levels = book["asks"] if side == "buy" else book["bids"]
    cost = filled = 0.0
    for px, available, _ in levels:
        px, available = float(px), float(available)
        wanted = (notional - cost) / px if notional is not None else size - filled
        take = min(available, wanted)
        cost += take * px
        filled += take
        if (notional is not None and notional - cost <= 1e-9) or (size is not None and size - filled <= 1e-12):
            return cost / filled, filled
    raise RuntimeError(f"{coin}: Kraken's visible order book is too thin to fill this order")


class SpotAccount:
    def __init__(self, starting_balance, fee, path):
        self.path = BASE_DIR / path
        self.fee = fee
        if self.path.exists():
            self.state = json.loads(self.path.read_text(encoding="utf-8"))
        else:
            now = now_ms()
            self.state = {"created": iso(now), "starting_balance": starting_balance, "balance": starting_balance,
                          "last_sync": now // HOUR_MS * HOUR_MS, "positions": {}, "history": []}
            log.info("Created simulated spot account with $%s", f"{starting_balance:,.2f}")

    @property
    def balance(self):
        return self.state["balance"]

    @property
    def positions(self):
        return self.state["positions"]

    def save(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        tmp = self.path.with_suffix(".tmp")
        tmp.write_text(json.dumps(self.state, indent=2), encoding="utf-8")
        tmp.replace(self.path)

    def has_signal(self, signal_id):
        return any(h.get("signal_id") == signal_id for h in self.state["history"])

    def equity(self, prices):
        return self.balance + sum(p["qty"] * prices.get(c, p["entry"]) for c, p in self.positions.items())

    def _record(self, at, coin, action, qty, price, fee, pnl=0.0, signal_id=None, reason=None):
        entry = {"time": iso(at), "coin": coin, "action": action, "side": "long", "qty": qty, "price": price,
                 "fee": round(fee, 6), "pnl": round(pnl, 6), "balance": round(self.balance, 6)}
        if signal_id:
            entry["signal_id"] = signal_id
        if reason:
            entry["reason"] = reason
        self.state["history"].append(entry)
        return entry

    def buy(self, coin, usd, stop_pct=None, signal_id=None):
        """Buy `usd` dollars' worth at market. Returns the position, or None if this signal was already traded."""
        if signal_id and self.has_signal(signal_id):
            log.info("%s: %s was already traded; skipping.", coin, signal_id)
            return None
        if coin in self.positions:
            raise RuntimeError(f"{coin}: already held")
        if usd > self.balance:
            raise RuntimeError(f"{coin}: not enough cash ({self.balance:,.2f}) for a ${usd:,.2f} buy")
        price, gross = fill(coin, "buy", notional=usd)
        qty = gross * (1 - self.fee)  # like Alpaca: the fee comes out of the coins received
        at = now_ms()
        self.state["balance"] -= usd
        pos = {"qty": qty, "gross": gross, "entry": price, "cost": usd,
               "stop": price * (1 - stop_pct) if stop_pct else None, "opened": at, "alpaca": None}
        if signal_id:
            pos["signal_id"] = signal_id
        self.positions[coin] = pos
        self._record(at, coin, "buy", qty, price, usd * self.fee, signal_id=signal_id)
        log.info("%s: bought %.8g @ %.6g for $%.2f (fee $%.2f), stop %s", coin, qty, price, usd, usd * self.fee,
                 f"{pos['stop']:.6g}" if pos["stop"] else "none")
        return pos

    def sell(self, coin, reason, price=None, at=None, signal_id=None):
        """Sell the whole position at market (or at `price`, for stops replayed from candles).

        Returns (closed position, history entry).
        """
        pos = self.positions.pop(coin)
        if price is None:
            price, _ = fill(coin, "sell", size=pos["qty"])
        gross = pos["qty"] * price
        fee = gross * self.fee
        self.state["balance"] += gross - fee
        entry = self._record(at or now_ms(), coin, "sell", pos["qty"], price, fee, pnl=gross - fee - pos["cost"],
                             signal_id=signal_id, reason=reason)
        log.info("%s: sold %.8g @ %.6g (%s), profit $%.2f after fees", coin, pos["qty"], price, reason, entry["pnl"])
        return pos, entry

    def sync(self, now=None):
        """Replay finished hours since the last sync for stop-losses. Returns [(position, entry)] stopped out."""
        now = now or now_ms()
        current_hour = now // HOUR_MS * HOUR_MS
        stopped = []
        for coin in list(self.positions):
            pos = self.positions[coin]
            start = max(self.state["last_sync"], (pos["opened"] // HOUR_MS + 1) * HOUR_MS)
            if not pos.get("stop") or start >= current_hour:
                continue
            for candle in get_hourly(coin, start):
                if candle["o"] <= pos["stop"] or candle["l"] <= pos["stop"]:
                    price = candle["o"] if candle["o"] <= pos["stop"] else pos["stop"]
                    stopped.append(self.sell(coin, "stop-loss", price=price, at=candle["t"]))
                    break
            time.sleep(0.3)
        self.state["last_sync"] = max(self.state["last_sync"], current_hour)
        return stopped
