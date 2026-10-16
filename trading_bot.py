"""Moving average crossover bot for an Alpaca paper trading account.

For each stock on the watchlist, fetches recent daily prices from yfinance,
computes a short and a long simple moving average, and places a market order
when the short average crosses the long average between the last two
completed trading days:

  short crosses above long -> buy  trade_qty shares
  short crosses below long -> sell trade_qty shares (only if they are held)

Each stock is checked and traded on its own signal. Settings (including the
watchlist) live in config.toml; API keys are read from .env or, when running on
GitHub Actions, from environment variables. Orders always go to the paper
trading endpoint. The log goes to trading_bot.log, or to the path in the
TRADING_BOT_LOG environment variable.

Usage:
  python trading_bot.py                  # check for a crossover and trade on it
  python trading_bot.py --dry-run        # report the signal without placing orders
  python trading_bot.py --wait-for-open  # skip market holidays, wait for 9:30 AM ET,
                                         # then run (used by the scheduled task)
"""

import argparse
import logging
import os
import sys
import tomllib
from datetime import time
from pathlib import Path
from time import sleep

import pandas as pd
import yfinance as yf
from alpaca.common.exceptions import APIError
from alpaca.trading.client import TradingClient
from alpaca.trading.enums import OrderSide, TimeInForce
from alpaca.trading.requests import GetCalendarRequest, MarketOrderRequest
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
MARKET_TZ = "America/New_York"
MARKET_OPEN = time(9, 30)
MARKET_CLOSE = time(16, 0)

log = logging.getLogger("trading_bot")


def load_config(path):
    with open(path, "rb") as f:
        config = tomllib.load(f)

    required = ("symbols", "short_window", "long_window", "trade_qty", "lookback_days")
    missing = [key for key in required if key not in config]
    if missing:
        raise ValueError(f"{path} is missing: {', '.join(missing)}")
    symbols = config["symbols"]
    if not isinstance(symbols, list) or not symbols or not all(isinstance(s, str) and s.strip() for s in symbols):
        raise ValueError('symbols must be a non-empty list of tickers, e.g. symbols = ["AAPL", "MSFT"]')
    if not 0 < config["short_window"] < config["long_window"]:
        raise ValueError("short_window must be positive and smaller than long_window")
    if config["lookback_days"] <= config["long_window"]:
        raise ValueError("lookback_days must be greater than long_window")
    if config["trade_qty"] <= 0:
        raise ValueError("trade_qty must be positive")
    # Uppercase and drop repeats, keeping the order they were listed in.
    config["symbols"] = list(dict.fromkeys(s.strip().upper() for s in symbols))
    return config


def fetch_closes(symbol, lookback_days):
    """Return closing prices for the last `lookback_days` completed trading days."""
    # A year of history comfortably covers 100+ trading days.
    history = yf.Ticker(symbol).history(period="1y", interval="1d", auto_adjust=True)
    if history.empty:
        raise RuntimeError(f"yfinance returned no data for {symbol}")
    closes = history["Close"].dropna()

    # Drop today's bar while the market is still open; it isn't a final close yet.
    now = pd.Timestamp.now(tz=MARKET_TZ)
    last_bar = closes.index[-1].tz_convert(MARKET_TZ)
    if last_bar.date() == now.date() and now.time() < MARKET_CLOSE:
        closes = closes.iloc[:-1]

    return closes.tail(lookback_days)


def detect_crossover(closes, short_window, long_window):
    """Compare the moving averages on the last two days.

    Returns ("buy" | "sell" | None, details) where details holds the values used.
    """
    if len(closes) < long_window + 1:
        raise ValueError(
            f"need at least {long_window + 1} days of data for a crossover, got {len(closes)}"
        )

    short_ma = closes.rolling(short_window).mean()
    long_ma = closes.rolling(long_window).mean()
    prev_short, prev_long = short_ma.iloc[-2], long_ma.iloc[-2]
    curr_short, curr_long = short_ma.iloc[-1], long_ma.iloc[-1]

    signal = None
    if prev_short <= prev_long and curr_short > curr_long:
        signal = "buy"
    elif prev_short >= prev_long and curr_short < curr_long:
        signal = "sell"

    details = {
        "prev_date": closes.index[-2].date(),
        "curr_date": closes.index[-1].date(),
        "prev_short": prev_short,
        "prev_long": prev_long,
        "curr_short": curr_short,
        "curr_long": curr_long,
        "close": closes.iloc[-1],
    }
    return signal, details


def make_client():
    load_dotenv(BASE_DIR / ".env")
    key_id = os.getenv("APCA_API_KEY_ID")
    secret = os.getenv("APCA_API_SECRET_KEY")
    if not key_id or not secret:
        raise RuntimeError("APCA_API_KEY_ID and APCA_API_SECRET_KEY must be set in .env")
    # paper=True pins every request to https://paper-api.alpaca.markets.
    return TradingClient(key_id, secret, paper=True)


def wait_for_open(client):
    """Return False if the market is closed today; otherwise block until 9:30 AM ET."""
    today = pd.Timestamp.now(tz=MARKET_TZ).date()
    sessions = client.get_calendar(GetCalendarRequest(start=today, end=today))
    if not sessions or sessions[0].date != today:
        log.info("Market is closed today (%s); skipping.", today)
        return False

    open_at = pd.Timestamp.combine(today, MARKET_OPEN).tz_localize(MARKET_TZ)
    remaining = (open_at - pd.Timestamp.now(tz=MARKET_TZ)).total_seconds()
    if remaining > 0:
        log.info("Market opens at 09:30 ET; waiting %.0f minutes.", remaining / 60)
        # Short steps against the wall clock, so a PC that sleeps mid-wait still
        # wakes up to the right time instead of a stale countdown.
        while pd.Timestamp.now(tz=MARKET_TZ) < open_at:
            sleep(min(30, max(1, (open_at - pd.Timestamp.now(tz=MARKET_TZ)).total_seconds())))
        log.info("Market is open.")
    return True


def place_order(client, symbol, side, qty, signal_date):
    # One order per symbol, side and signal day: Alpaca rejects a reused
    # client_order_id, so running the bot twice on the same day can't double up.
    client_order_id = f"macross-{symbol}-{side.value}-{signal_date:%Y%m%d}"
    request = MarketOrderRequest(
        symbol=symbol,
        qty=qty,
        side=side,
        time_in_force=TimeInForce.DAY,
        client_order_id=client_order_id,
    )
    try:
        order = client.submit_order(request)
    except APIError as error:
        if "client_order_id" in str(error):
            log.info("Order %s was already placed for this signal; skipping.", client_order_id)
            return None
        raise
    log.info(
        "Order submitted: %s %s %s, id %s, status %s",
        side.value, qty, symbol, order.id, order.status.value,
    )
    return order


def check_symbol(client, config, symbol, owned, dry_run):
    """Check one stock for a crossover and trade it. Returns the action taken."""
    short_window = config["short_window"]
    long_window = config["long_window"]
    qty = config["trade_qty"]

    closes = fetch_closes(symbol, config["lookback_days"])
    signal, d = detect_crossover(closes, short_window, long_window)

    log.info(
        "%s: %d days of data through %s, close %.2f, holding %g",
        symbol, len(closes), d["curr_date"], d["close"], owned,
    )
    log.info(
        "%s: %s SMA%d %.2f vs SMA%d %.2f  ->  %s SMA%d %.2f vs SMA%d %.2f",
        symbol,
        d["prev_date"], short_window, d["prev_short"], long_window, d["prev_long"],
        d["curr_date"], short_window, d["curr_short"], long_window, d["curr_long"],
    )

    if signal is None:
        trend = "above" if d["curr_short"] > d["curr_long"] else "below"
        log.info("%s: no crossover (SMA%d is %s SMA%d); nothing to do.", symbol, short_window, trend, long_window)
        return "no signal"

    log.info(
        "%s: crossover on %s, SMA%d crossed %s SMA%d -> %s signal.",
        symbol, d["curr_date"], short_window, "above" if signal == "buy" else "below", long_window, signal.upper(),
    )

    if signal == "sell" and owned < qty:
        log.info("%s: sell signal, but only %g held (need %d); not opening a short.", symbol, owned, qty)
        return "sell skipped (not held)"

    side = OrderSide.BUY if signal == "buy" else OrderSide.SELL
    if dry_run:
        log.info("%s: dry run, would %s %d at market.", symbol, side.value, qty)
        return f"would {side.value}"
    order = place_order(client, symbol, side, qty, d["curr_date"])
    return f"{side.value} order placed" if order else "already ordered"


def run(config, dry_run, wait):
    """Check every stock on the watchlist. Returns False if any of them failed."""
    client = make_client()
    if wait and not wait_for_open(client):
        return True

    # Checked on every run, so bad or expired keys fail loudly even on quiet days.
    account = client.get_account()
    holdings = {p.symbol: float(p.qty) for p in client.get_all_positions()}
    log.info(
        "Paper account ending %s: cash %s, buying power %s",
        account.account_number[-4:], account.cash, account.buying_power,
    )
    log.info("Watchlist: %s", ", ".join(config["symbols"]))

    results = {}
    for symbol in config["symbols"]:
        # One bad ticker or data hiccup shouldn't stop the rest of the watchlist.
        try:
            results[symbol] = check_symbol(client, config, symbol, holdings.get(symbol, 0.0), dry_run)
        except Exception:
            log.exception("%s: check failed", symbol)
            results[symbol] = "FAILED"

    log.info("Summary: %s", "; ".join(f"{s} {r}" for s, r in results.items()))
    return "FAILED" not in results.values()


def main():
    parser = argparse.ArgumentParser(description="Moving average crossover bot (Alpaca paper trading).")
    parser.add_argument("--config", default=BASE_DIR / "config.toml", type=Path, help="path to config file")
    parser.add_argument("--dry-run", action="store_true", help="report the signal without placing orders")
    parser.add_argument(
        "--wait-for-open",
        action="store_true",
        help="skip market holidays and wait until 9:30 AM ET before checking",
    )
    args = parser.parse_args()

    log_file = BASE_DIR / os.getenv("TRADING_BOT_LOG", "trading_bot.log")
    log_file.parent.mkdir(parents=True, exist_ok=True)
    handlers = [logging.FileHandler(log_file, encoding="utf-8")]
    if sys.stdout is not None:  # None under pythonw.exe (scheduled runs have no console)
        handlers.append(logging.StreamHandler(sys.stdout))
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s", handlers=handlers)

    log.info("---- Run started%s ----", " (dry run)" if args.dry_run else "")
    try:
        ok = run(load_config(args.config), args.dry_run, args.wait_for_open)
    except Exception:
        log.exception("Bot run failed")
        return 1
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
