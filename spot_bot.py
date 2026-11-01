"""Paper trade the three strategies on spot (buy-only, no leverage) and copy the trades to Alpaca.

Runs right after futures_bot.py (same workflow), on the same weekly coins and the same signals, so spot
and futures results can be compared directly. For each strategy in spot_config.toml:
  1. Replay the hours since the last run in that strategy's simulated spot account (stop-losses), and
     close the matching Alpaca lots.
  2. Check open Alpaca lots for stops that already filled on Alpaca.
  3. On universe-refresh days, sell coins that left the universe.
  4. Apply the strategy's signals for the last finished day. Shorts are skipped: a short signal only
     closes a held coin. Fills come from Kraken's live order books, and coins Alpaca lists are also
     bought or sold on the Alpaca paper account.

Accounts: state/spot_<strategy>.json. Log: spot_bot.log, or the path in SPOT_BOT_LOG.

Usage:
  python spot_bot.py            # run every strategy, save accounts, copy trades to Alpaca
  python spot_bot.py --dry-run  # same signals and simulated fills, but nothing is saved or sent to Alpaca
"""

import argparse
import json
import logging
import os
import sys
import tomllib
from pathlib import Path

import pandas as pd

from backtest_futures import build_indicators
from futures_bot import STRATEGIES, UNIVERSE_FILE, daily_frames
from paper_futures import BASE_DIR
from paper_spot import SpotAccount, get_prices, kraken_pairs, spot_name
from trading_bot import make_client, setup_logging

log = logging.getLogger("spot_bot")


def load_config(path):
    with open(path, "rb") as f:
        config = tomllib.load(f)
    required = ("strategies", "trade_usd", "stop_pct", "starting_balance", "fee", "alpaca_mirror")
    missing = [key for key in required if key not in config]
    if missing:
        raise ValueError(f"{path} is missing: {', '.join(missing)}")
    unknown = [s for s in config["strategies"] if s not in STRATEGIES]
    if unknown:
        raise ValueError(f"unknown strategies {unknown}; choose from {list(STRATEGIES)}")
    return config


def mirror_sell(mirror, pos, entry, signal_id, dry_run):
    """Close the Alpaca lot behind a simulated sell, and note the result in the sell's history entry."""
    lot = pos.get("alpaca")
    if not lot or lot.get("status") != "open" or mirror is None or dry_run:
        return
    try:
        mirror.sell(lot, signal_id)
    except Exception as error:
        lot["error"] = str(error)
        log.warning("Alpaca sell for %s failed: %s", lot["symbol"], error)
    entry["alpaca"] = lot


def run_strategy(key, config, universe, refresh_today, closes, ind, day, mirror, dry_run):
    name, signals = STRATEGIES[key]
    tag = f"[{name}, spot]"
    account = SpotAccount(config["starting_balance"], config["fee"], f"state/spot_{key}.json")

    # 1. Stops hit since the last run (replayed hour by hour), and their Alpaca lots.
    for pos, entry in account.sync():
        mirror_sell(mirror, pos, entry, f"{key}-{entry['coin']}-stop-{entry['time'][:10]}", dry_run)

    # 2. Stops that filled on Alpaca while the simulation still holds the coin (prices differ slightly).
    if mirror and not dry_run:
        for coin, pos in account.positions.items():
            lot = pos.get("alpaca")
            try:
                if lot and mirror.refresh(lot):
                    lot["diverged"] = True
                    log.warning("%s %s: Alpaca's stop filled @ %.6g but the simulation still holds", tag, coin, lot["exit"])
            except Exception as error:
                log.warning("%s %s: couldn't check the Alpaca stop: %s", tag, coin, error)

    # 3. Weekly refresh: sell coins that left the universe (spot names, e.g. PEPE for kPEPE).
    spot_universe = {spot_name(c) for c in universe}
    if refresh_today:
        for coin in [c for c in account.positions if c not in spot_universe]:
            pos, entry = account.sell(coin, "left universe")
            mirror_sell(mirror, pos, entry, f"{key}-{coin}-left-{day.date()}", dry_run)

    # 4. Today's signals: the futures signal code, buy side only.
    weekly = refresh_today == "weekly" and account.state.get("last_rebalance") != str(day.date())
    held = {next((c for c in universe if spot_name(c) == coin), coin): "long" for coin in account.positions}
    actions = [a for a in signals(day, universe, closes, ind, held, weekly) if not (a[0] == "open" and a[2] == "short")]
    if weekly:
        account.state["last_rebalance"] = str(day.date())
    for action, coin_hl, side in actions:
        coin = spot_name(coin_hl)
        signal_id = f"{key}-{coin}-{side}-{day.date()}"
        try:
            if action == "close" and coin in account.positions:
                pos, entry = account.sell(coin, "signal", signal_id=signal_id)
                mirror_sell(mirror, pos, entry, signal_id, dry_run)
            elif action == "open":
                if coin not in kraken_pairs():
                    log.info("%s %s: no Kraken spot market; skipped", tag, coin)
                    continue
                pos = account.buy(coin, config["trade_usd"], stop_pct=config["stop_pct"], signal_id=signal_id)
                if pos and mirror and mirror.supports(coin):
                    if dry_run:
                        log.info("%s %s: would also buy %.8g on Alpaca", tag, coin, pos["gross"])
                    else:
                        try:
                            pos["alpaca"] = mirror.buy(coin, pos["gross"], config["stop_pct"], signal_id)
                        except Exception as error:
                            pos["alpaca"] = {"symbol": f"{coin}/USD", "status": "error", "error": str(error)}
                            log.warning("%s %s: Alpaca copy failed: %s", tag, coin, error)
        except Exception as error:  # e.g. not enough cash or a thin book: log it and carry on
            log.warning("%s %s %s skipped: %s", tag, action, coin, error)

    prices = get_prices(list(account.positions))
    equity = account.equity(prices)
    history = account.state.setdefault("equity_history", [])
    history[:] = [h for h in history if h["date"] != str(day.date())] + [{"date": str(day.date()), "equity": round(equity, 2)}]
    on_alpaca = sum(1 for p in account.positions.values() if (p.get("alpaca") or {}).get("status") == "open")
    log.info("%s %d signal(s) | equity %s (%+.1f%%) | cash %s | holding: %s | on Alpaca: %d",
             tag, len(actions), f"{equity:,.2f}", (equity / config["starting_balance"] - 1) * 100,
             f"{account.balance:,.2f}", ", ".join(account.positions) or "none", on_alpaca)
    if not dry_run:
        account.save()
    return equity


def main():
    parser = argparse.ArgumentParser(description="Paper trade the strategies on spot and copy trades to Alpaca.")
    parser.add_argument("--config", default=BASE_DIR / "spot_config.toml", type=Path, help="path to config file")
    parser.add_argument("--dry-run", action="store_true", help="run everything but save nothing and send nothing to Alpaca")
    args = parser.parse_args()

    setup_logging(os.getenv("SPOT_BOT_LOG", "spot_bot.log"))
    log.info("---- Spot run started%s ----", " (dry run)" if args.dry_run else "")
    try:
        config = load_config(args.config)
        if not UNIVERSE_FILE.exists():
            log.info("No universe yet: run futures_bot.py first.")
            return 0
        saved = json.loads(UNIVERSE_FILE.read_text(encoding="utf-8"))
        universe = saved["coins"]
        today = str(pd.Timestamp.now(tz="UTC").date())
        refresh_today = saved.get("kind", "initial") if saved["refreshed"] == today else None

        mirror = None
        if config["alpaca_mirror"]:
            from alpaca_mirror import AlpacaMirror
            mirror = AlpacaMirror(make_client())
            on_alpaca = [spot_name(c) for c in universe if mirror.supports(spot_name(c))]
            log.info("Alpaca lists %d of this week's coins: %s", len(on_alpaca), ", ".join(on_alpaca) or "none")

        held_anywhere = set()
        for key in config["strategies"]:
            path = BASE_DIR / f"state/spot_{key}.json"
            if path.exists():
                held_anywhere |= set(json.loads(path.read_text(encoding="utf-8"))["positions"])
        frames_for = sorted(set(universe) | {c for c in universe if spot_name(c) in held_anywhere})
        closes, highs, lows = daily_frames(frames_for)
        ind = build_indicators(closes, highs, lows)
        day = closes.index[-1]

        failed, results = False, {}
        for key in config["strategies"]:
            try:
                results[key] = run_strategy(key, config, universe, refresh_today, closes, ind, day, mirror, args.dry_run)
            except Exception:
                log.exception("[%s, spot] run failed", STRATEGIES[key][0])
                failed = True
        log.info("Spot scoreboard: %s", " | ".join(f"{STRATEGIES[k][0]} {v:,.0f}" for k, v in results.items()))
    except Exception:
        log.exception("Spot bot run failed")
        return 1
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
