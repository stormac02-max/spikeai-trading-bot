"""Paper trade the shortlisted futures strategies side by side, each in its own simulated account.

Runs once a day after Hyperliquid's daily candle closes (00:00 UTC). For every strategy listed in
futures_config.toml:
  1. Replay the hours since the last run in that strategy's account: stop-losses, liquidations, funding.
  2. On Mondays (or if the last refresh is over a week old), refresh the coin universe: the most-traded
     Hyperliquid perps over the past 7 days, minus the excluded coins, with at least 51 days of history.
     This is the same rule as backtest_futures.py.
  3. Close positions in coins that left the universe, then apply the strategy's signals for the last
     finished day. The signal code is shared with backtest_futures.py, and fills use live order-book prices.

Each strategy's account lives in state/futures_<strategy>.json, with a daily equity history, so the
strategies can be compared at the end of the evaluation period. The shared universe is in
state/futures_universe.json. The log goes to futures_bot.log, or the path in FUTURES_BOT_LOG.

Usage:
  python futures_bot.py            # run every strategy and save the accounts
  python futures_bot.py --dry-run  # same, but nothing is saved
"""

import argparse
import json
import logging
import os
import sys
import time
import tomllib
from pathlib import Path

import pandas as pd

from backtest_futures import MIN_HISTORY, breakout, build_indicators, ma_crossover, momentum
from paper_futures import BASE_DIR, FuturesAccount, get_candles, get_markets, now_ms
from trading_bot import setup_logging

DAY_MS = 86_400_000
STRATEGIES = {
    "ma_crossover": ("MA crossover 20/50", ma_crossover),
    "breakout": ("Breakout 20/10", breakout),
    "momentum": ("Momentum 14d, 5 long/5 short", momentum),
}
UNIVERSE_FILE = BASE_DIR / "state" / "futures_universe.json"
HISTORY_DAYS = 70  # enough finished days for the 50-day average plus the day before
PREFILTER = 60  # rank only the 60 busiest markets by 24h volume when refreshing (keeps API calls down)

log = logging.getLogger("futures_bot")


def load_config(path):
    with open(path, "rb") as f:
        config = tomllib.load(f)
    required = ("universe_size", "universe_exclude", "leverage", "margin_usd", "stop_pct",
                "starting_balance", "taker_fee", "strategies")
    missing = [key for key in required if key not in config]
    if missing:
        raise ValueError(f"{path} is missing: {', '.join(missing)}")
    unknown = [s for s in config["strategies"] if s not in STRATEGIES]
    if unknown:
        raise ValueError(f"unknown strategies {unknown}; choose from {list(STRATEGIES)}")
    return config


def today_start_ms():
    return now_ms() // DAY_MS * DAY_MS  # 00:00 UTC today: candles before this are finished


def refresh_universe(markets, size, exclude):
    """The `size` most-traded perps over the last 7 finished days with at least MIN_HISTORY days of history."""
    end = today_start_ms()
    busiest = sorted((c for c in markets if c not in exclude), key=lambda c: markets[c]["day_volume"], reverse=True)
    ranked = []
    for coin in busiest[:PREFILTER]:
        candles = get_candles(coin, "1d", end - (MIN_HISTORY + 10) * DAY_MS, end - 1)
        candles = [c for c in candles if c["end"] < end]
        if len(candles) >= MIN_HISTORY:
            ranked.append((sum(c["v"] * c["c"] for c in candles[-7:]), coin))
        time.sleep(0.5)  # stay well under Hyperliquid's rate limit
    return [coin for _, coin in sorted(ranked, reverse=True)[:size]]


def load_universe(markets, config, dry_run):
    """Returns (coins, refresh) where refresh is None, "initial" (first ever) or "weekly"."""
    today = pd.Timestamp.now(tz="UTC").normalize()
    saved = json.loads(UNIVERSE_FILE.read_text(encoding="utf-8")) if UNIVERSE_FILE.exists() else None
    if saved is None:
        refresh = "initial"
    elif (today.dayofweek == 0 and saved["refreshed"] != str(today.date())) or \
            pd.Timestamp(saved["refreshed"], tz="UTC") <= today - pd.Timedelta(days=7):  # Monday, or a missed Monday
        refresh = "weekly"
    else:
        return saved["coins"], None

    coins = refresh_universe(markets, config["universe_size"], set(config["universe_exclude"]))
    log.info("Universe refreshed (%s, %d coins): %s", refresh, len(coins), ", ".join(coins))
    if not dry_run:
        UNIVERSE_FILE.parent.mkdir(parents=True, exist_ok=True)
        UNIVERSE_FILE.write_text(json.dumps({"refreshed": str(today.date()), "coins": coins}, indent=2), encoding="utf-8")
    return coins, refresh


def daily_frames(coins):
    """Closes, highs and lows of the last HISTORY_DAYS finished days, one column per coin."""
    end = today_start_ms()
    closes, highs, lows = {}, {}, {}
    for coin in coins:
        candles = [c for c in get_candles(coin, "1d", end - HISTORY_DAYS * DAY_MS, end - 1) if c["end"] < end]
        index = pd.to_datetime([c["t"] for c in candles], unit="ms", utc=True)
        closes[coin] = pd.Series([c["c"] for c in candles], index=index)
        highs[coin] = pd.Series([c["h"] for c in candles], index=index)
        lows[coin] = pd.Series([c["l"] for c in candles], index=index)
        time.sleep(0.3)
    return pd.DataFrame(closes).sort_index(), pd.DataFrame(highs).sort_index(), pd.DataFrame(lows).sort_index()


def run_strategy(key, config, markets, universe, refresh, closes, ind, day, dry_run):
    name, signals = STRATEGIES[key]
    account = FuturesAccount(config["starting_balance"], config["taker_fee"], path=f"state/futures_{key}.json")
    account.sync()
    tag = f"[{name}]"

    # Coins no longer listed on Hyperliquid can't be filled from the order book: close at their last close.
    for coin in [c for c in account.positions if c not in markets]:
        price = closes[coin].dropna().iloc[-1] if coin in closes else account.positions[coin]["entry"]
        account.close(coin, "delisted", price=price)
    if refresh:
        for coin in [c for c in account.positions if c not in universe]:
            account.close(coin, "left universe")

    # Weekly strategies (momentum) rebalance on weekly refreshes only, as in the backtest, not on the very first run.
    held = {coin: pos["side"] for coin, pos in account.positions.items()}
    actions = signals(day, universe, closes, ind, held, refresh == "weekly")
    for action, coin, side in actions:
        signal_id = f"{key}-{coin}-{side}-{day.date()}"
        try:
            if action == "close" and coin in account.positions:
                account.close(coin, "signal", signal_id=signal_id)
            elif action == "open":
                account.open(coin, side, config["margin_usd"], config["leverage"], markets[coin],
                             stop_pct=config["stop_pct"], signal_id=signal_id)
        except Exception as error:  # e.g. not enough balance or a thin book: log it and carry on
            log.warning("%s %s %s %s skipped: %s", tag, action, side, coin, error)

    marks = {coin: markets[coin]["mark"] for coin in account.positions}
    equity = account.equity(marks)
    history = account.state.setdefault("equity_history", [])
    history[:] = [h for h in history if h["date"] != str(day.date())] + [{"date": str(day.date()), "equity": round(equity, 2)}]
    peak = max(h["equity"] for h in history + [{"equity": config["starting_balance"]}])
    open_list = ", ".join(f"{c} {p['side']}" for c, p in account.positions.items()) or "none"
    log.info(
        "%s %d signal(s) | equity %s (%+.1f%%, %.1f%% below peak) | cash %s | open: %s",
        tag, len(actions), f"{equity:,.2f}", (equity / config["starting_balance"] - 1) * 100,
        (1 - equity / peak) * 100, f"{account.balance:,.2f}", open_list,
    )
    if not dry_run:
        account.save()
    return equity


def main():
    parser = argparse.ArgumentParser(description="Paper trade the shortlisted futures strategies side by side.")
    parser.add_argument("--config", default=BASE_DIR / "futures_config.toml", type=Path, help="path to config file")
    parser.add_argument("--dry-run", action="store_true", help="run everything but save nothing")
    args = parser.parse_args()

    setup_logging(os.getenv("FUTURES_BOT_LOG", "futures_bot.log"))
    log.info("---- Futures run started%s ----", " (dry run)" if args.dry_run else "")
    try:
        config = load_config(args.config)
        markets = get_markets()
        universe, refresh = load_universe(markets, config, args.dry_run)
        universe = [c for c in universe if c in markets]
        held_anywhere = set()
        for key in config["strategies"]:
            path = BASE_DIR / f"state/futures_{key}.json"
            if path.exists():
                held_anywhere |= set(json.loads(path.read_text(encoding="utf-8"))["positions"])
        closes, highs, lows = daily_frames(sorted(set(universe) | (held_anywhere & set(markets))))
        ind = build_indicators(closes, highs, lows)
        day = closes.index[-1]
        log.info("Signals use the day ending %s 00:00 UTC; %d coins in the universe", (day + pd.Timedelta(days=1)).date(), len(universe))

        failed = False
        results = {}
        for key in config["strategies"]:
            try:
                results[key] = run_strategy(key, config, markets, universe, refresh, closes, ind, day, args.dry_run)
            except Exception:
                log.exception("[%s] run failed", STRATEGIES[key][0])
                failed = True
        log.info("Scoreboard: %s", " | ".join(f"{STRATEGIES[k][0]} {v:,.0f}" for k, v in results.items()))
        if "evaluation_until" in config:
            log.info("Evaluation runs until %s; then the best strategy is kept.", config["evaluation_until"])
    except Exception:
        log.exception("Futures bot run failed")
        return 1
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
