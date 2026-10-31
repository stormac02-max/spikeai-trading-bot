"""Moving average crossover bot for crypto on an Alpaca paper trading account.

For each coin on the watchlist, fetches daily prices from Alpaca's crypto
market data, computes a short and a long simple moving average, and places a
market order when the short average crosses the long average between the
last two completed days:

  short crosses above long -> buy trade_usd dollars' worth of the coin
  short crosses below long -> sell the coin's whole position (if any is held)

Crypto trades around the clock and Alpaca's daily candles close at 00:00 UTC,
so this is meant to run once a day shortly after that (see
.github/workflows/crypto-bot.yml). The crossover logic, Alpaca client and
logging are shared with trading_bot.py. Settings live in crypto_config.toml.
Orders always go to the paper trading endpoint. The log goes to
crypto_bot.log, or to the path in the CRYPTO_BOT_LOG environment variable.

Usage:
  python crypto_bot.py            # check for crossovers and trade on them
  python crypto_bot.py --dry-run  # report the signals without placing orders
"""

import argparse
import logging
import math
import os
import sys
import tomllib
from pathlib import Path

import pandas as pd
from alpaca.common.exceptions import APIError
from alpaca.data.historical import CryptoHistoricalDataClient
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame
from alpaca.trading.enums import AssetClass, OrderSide, TimeInForce
from alpaca.trading.requests import MarketOrderRequest

from trading_bot import BASE_DIR, detect_crossover, make_client, setup_logging

log = logging.getLogger("crypto_bot")


def load_config(path):
    with open(path, "rb") as f:
        config = tomllib.load(f)

    required = ("symbols", "short_window", "long_window", "trade_usd", "lookback_days")
    missing = [key for key in required if key not in config]
    if missing:
        raise ValueError(f"{path} is missing: {', '.join(missing)}")
    symbols = config["symbols"]
    if not isinstance(symbols, list) or not all(isinstance(s, str) and "/" in s for s in symbols):
        raise ValueError('symbols must be a list of Alpaca crypto pairs, e.g. symbols = ["BTC/USD"]')
    if not 0 < config["short_window"] < config["long_window"]:
        raise ValueError("short_window must be positive and smaller than long_window")
    if config["lookback_days"] <= config["long_window"]:
        raise ValueError("lookback_days must be greater than long_window")
    if config["trade_usd"] <= 0:
        raise ValueError("trade_usd must be positive")
    # Uppercase and drop repeats, keeping the order they were listed in.
    config["symbols"] = list(dict.fromkeys(s.strip().upper() for s in symbols))
    return config


def price(value):
    """Format a price readably for both $77,000 coins and $0.000003 coins."""
    if value == 0 or abs(value) >= 1:
        return f"{value:,.2f}"
    decimals = 4 - math.floor(math.log10(abs(value)))  # about 5 significant digits, no scientific notation
    return f"{value:.{decimals}f}".rstrip("0")


def fetch_closes(data_client, symbol, lookback_days):
    """Return daily closes for the last `lookback_days` completed days (UTC)."""
    now = pd.Timestamp.now(tz="UTC")
    request = CryptoBarsRequest(
        symbol_or_symbols=symbol,
        timeframe=TimeFrame.Day,
        start=now - pd.Timedelta(days=lookback_days + 10),
    )
    bars = data_client.get_crypto_bars(request).df
    if bars.empty:
        raise RuntimeError(f"Alpaca returned no price data for {symbol}")
    closes = bars.xs(symbol, level="symbol")["close"]

    # Each daily bar starts at 00:00 UTC; today's is still forming, so keep only finished days.
    closes = closes[closes.index + pd.Timedelta(days=1) <= now]
    return closes.tail(lookback_days)


def place_order(client, symbol, side, signal_date, notional=None, qty=None):
    # One order per coin, side and signal day: Alpaca rejects a reused
    # client_order_id, so running the bot twice on the same day can't double up.
    client_order_id = f"macross-{symbol.replace('/', '')}-{side.value}-{signal_date:%Y%m%d}"
    request = MarketOrderRequest(
        symbol=symbol,
        side=side,
        notional=notional,
        qty=qty,
        time_in_force=TimeInForce.GTC,  # crypto orders only accept GTC or IOC
        client_order_id=client_order_id,
    )
    try:
        order = client.submit_order(request)
    except APIError as error:
        if "client_order_id" in str(error):
            log.info("%s: order %s was already placed for this signal; skipping.", symbol, client_order_id)
            return None
        raise
    amount = f"${notional:,.2f}" if notional else f"{qty:g}"
    log.info("%s: order submitted, %s %s, id %s, status %s", symbol, side.value, amount, order.id, order.status.value)
    return order


def check_coin(client, data_client, config, symbol, position, dry_run):
    """Check one coin for a crossover and trade it. Returns the action taken."""
    short_window = config["short_window"]
    long_window = config["long_window"]
    held = float(position.qty_available or position.qty) if position else 0.0

    closes = fetch_closes(data_client, symbol, config["lookback_days"])
    signal, d = detect_crossover(closes, short_window, long_window)

    log.info(
        "%s: %d days of data through %s, close %s, holding %g",
        symbol, len(closes), d["curr_date"], price(d["close"]), held,
    )
    log.info(
        "%s: %s SMA%d %s vs SMA%d %s  ->  %s SMA%d %s vs SMA%d %s",
        symbol,
        d["prev_date"], short_window, price(d["prev_short"]), long_window, price(d["prev_long"]),
        d["curr_date"], short_window, price(d["curr_short"]), long_window, price(d["curr_long"]),
    )

    if signal is None:
        trend = "above" if d["curr_short"] > d["curr_long"] else "below"
        log.info("%s: no crossover (SMA%d is %s SMA%d); nothing to do.", symbol, short_window, trend, long_window)
        return "no signal"

    log.info(
        "%s: crossover on %s, SMA%d crossed %s SMA%d -> %s signal.",
        symbol, d["curr_date"], short_window, "above" if signal == "buy" else "below", long_window, signal.upper(),
    )

    if signal == "sell":
        if held <= 0:
            log.info("%s: sell signal, but none held; nothing to sell.", symbol)
            return "sell skipped (not held)"
        if dry_run:
            log.info("%s: dry run, would sell the whole position (%g).", symbol, held)
            return "would sell"
        order = place_order(client, symbol, OrderSide.SELL, d["curr_date"], qty=held)
        return "sell order placed" if order else "already ordered"

    if dry_run:
        log.info("%s: dry run, would buy $%s worth at market.", symbol, f"{config['trade_usd']:,.2f}")
        return "would buy"
    order = place_order(client, symbol, OrderSide.BUY, d["curr_date"], notional=config["trade_usd"])
    return "buy order placed" if order else "already ordered"


def run(config, dry_run):
    """Check every coin on the watchlist. Returns False if any of them failed."""
    client = make_client()

    # Checked on every run, so bad or expired keys fail loudly even on quiet days.
    account = client.get_account()
    # Alpaca lists crypto positions without the slash (BTCUSD), so match on that form.
    positions = {
        p.symbol.replace("/", ""): p for p in client.get_all_positions() if p.asset_class == AssetClass.CRYPTO
    }
    log.info(
        "Paper account ending %s: cash %s, crypto buying power %s",
        account.account_number[-4:], account.cash, account.non_marginable_buying_power,
    )
    if not config["symbols"]:
        log.info("No coins on the watchlist yet; add them to symbols in crypto_config.toml.")
        return True
    log.info("Crypto watchlist: %s", ", ".join(config["symbols"]))

    data_client = CryptoHistoricalDataClient(os.getenv("APCA_API_KEY_ID"), os.getenv("APCA_API_SECRET_KEY"))
    results = {}
    for symbol in config["symbols"]:
        # One bad coin or data hiccup shouldn't stop the rest of the watchlist.
        try:
            position = positions.get(symbol.replace("/", ""))
            results[symbol] = check_coin(client, data_client, config, symbol, position, dry_run)
        except Exception:
            log.exception("%s: check failed", symbol)
            results[symbol] = "FAILED"

    log.info("Summary: %s", "; ".join(f"{s} {r}" for s, r in results.items()))
    return "FAILED" not in results.values()


def main():
    parser = argparse.ArgumentParser(description="Crypto moving average crossover bot (Alpaca paper trading).")
    parser.add_argument(
        "--config", default=BASE_DIR / "crypto_config.toml", type=Path, help="path to config file"
    )
    parser.add_argument("--dry-run", action="store_true", help="report the signals without placing orders")
    args = parser.parse_args()

    setup_logging(os.getenv("CRYPTO_BOT_LOG", "crypto_bot.log"))
    log.info("---- Crypto run started%s ----", " (dry run)" if args.dry_run else "")
    try:
        ok = run(load_config(args.config), args.dry_run)
    except Exception:
        log.exception("Crypto bot run failed")
        return 1
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
