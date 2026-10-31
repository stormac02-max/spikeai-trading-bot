"""Simulated futures (perpetuals) paper trading account.

No exchange we can use offers paper trading for altcoin and memecoin futures,
so this keeps our own paper account and simulates it against Hyperliquid's
real market data (public API, no account or keys needed):

- Market orders fill at the average price you'd actually get by walking
  Hyperliquid's live order book for the order's size, plus the taker fee.
- Positions use isolated margin: margin = position value / leverage, with
  leverage capped at each coin's exchange maximum.
- Funding is charged or paid every hour from Hyperliquid's real funding rates
  (longs pay shorts when the rate is positive, shorts pay longs when negative).
- sync() replays every finished hour since the last sync using hourly candles,
  so a stop-loss or liquidation that would have happened at 3 AM is applied at
  3 AM at the right price, even if the bot only runs once a day.
- A position is liquidated when its margin falls to the maintenance margin
  (half the initial margin at the coin's max leverage, as on Hyperliquid) and
  loses all its margin. Losses never exceed a position's margin.

Simplification: the partial hour in which a position was opened isn't checked
for stops or liquidation (its candle includes prices from before the entry).

The account is saved as JSON (state/futures_account.json by default, or the
path in FUTURES_ACCOUNT_FILE) so it carries over between runs.
"""

import json
import logging
import os
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

API_URL = "https://api.hyperliquid.xyz/info"
HOUR_MS = 3_600_000
BASE_DIR = Path(__file__).resolve().parent
DEFAULT_ACCOUNT_FILE = "state/futures_account.json"

log = logging.getLogger("paper_futures")


# ---- Hyperliquid market data -------------------------------------------------

def hl_info(body):
    response = requests.post(API_URL, json=body, timeout=30)
    response.raise_for_status()
    return response.json()


def get_markets():
    """Live perp markets: {coin: {max_leverage, mark, funding, open_interest, day_volume}}."""
    meta, contexts = hl_info({"type": "metaAndAssetCtxs"})
    markets = {}
    for asset, ctx in zip(meta["universe"], contexts):
        if asset.get("isDelisted"):
            continue
        markets[asset["name"]] = {
            "max_leverage": asset["maxLeverage"],
            "mark": float(ctx["markPx"]),
            "funding": float(ctx["funding"]),
            "open_interest": float(ctx["openInterest"]),
            "day_volume": float(ctx["dayNtlVlm"]),
        }
    return markets


def get_candles(coin, interval, start_ms, end_ms):
    """Candles as dicts with t (start ms), end (ms), o, h, l, c and v (volume in coins)."""
    rows = hl_info({
        "type": "candleSnapshot",
        "req": {"coin": coin, "interval": interval, "startTime": int(start_ms), "endTime": int(end_ms)},
    })
    return [
        {"t": r["t"], "end": r["T"], "o": float(r["o"]), "h": float(r["h"]), "l": float(r["l"]),
         "c": float(r["c"]), "v": float(r["v"])}
        for r in rows
    ]


def get_funding(coin, start_ms, end_ms):
    """Hourly funding rates as {hour start ms: rate}, keyed by the hour each payment falls on."""
    rates, start = {}, int(start_ms)
    while start < end_ms:
        rows = hl_info({"type": "fundingHistory", "coin": coin, "startTime": start, "endTime": int(end_ms)})
        for r in rows:
            rates[r["time"] // HOUR_MS * HOUR_MS] = float(r["fundingRate"])
        if len(rows) < 500:  # the API returns at most 500 entries per call
            break
        start = rows[-1]["time"] + 1
    return rates


def fill(coin, side, notional=None, size=None):
    """Simulate a market order by walking the live order book.

    Pass `notional` (USDC) to open or `size` (coins) to close. Returns (average price, size filled).
    """
    book = hl_info({"type": "l2Book", "coin": coin})
    levels = book["levels"][1] if side == "buy" else book["levels"][0]  # buys lift asks, sells hit bids
    cost = filled = 0.0
    for level in levels:
        px, available = float(level["px"]), float(level["sz"])
        wanted = (notional - cost) / px if notional is not None else size - filled
        take = min(available, wanted)
        cost += take * px
        filled += take
        if (notional is not None and notional - cost <= 1e-9) or (size is not None and size - filled <= 1e-12):
            return cost / filled, filled
    raise RuntimeError(f"{coin}: the visible order book is too thin to fill this order")


# ---- helpers -----------------------------------------------------------------

def now_ms():
    return int(time.time() * 1000)


def iso(ms):
    return datetime.fromtimestamp(ms / 1000, tz=timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def liquidation_price(pos):
    """Price at which the position's margin falls to the maintenance margin."""
    size, entry, margin, mm = pos["size"], pos["entry"], pos["margin"], pos["mm_rate"]
    if pos["side"] == "long":
        return max(0.0, (entry * size - margin) / (size * (1 - mm)))
    return (entry * size + margin) / (size * (1 + mm))


def unrealized_pnl(pos, price):
    move = price - pos["entry"] if pos["side"] == "long" else pos["entry"] - price
    return move * pos["size"]


# ---- the account -------------------------------------------------------------

class FuturesAccount:
    def __init__(self, starting_balance, taker_fee, path=None):
        self.path = BASE_DIR / (path or os.getenv("FUTURES_ACCOUNT_FILE", DEFAULT_ACCOUNT_FILE))
        self.taker_fee = taker_fee
        if self.path.exists():
            self.state = json.loads(self.path.read_text(encoding="utf-8"))
        else:
            now = now_ms()
            self.state = {
                "created": iso(now),
                "starting_balance": starting_balance,
                "balance": starting_balance,
                "last_sync": now // HOUR_MS * HOUR_MS,
                "positions": {},
                "history": [],
            }
            log.info("Created simulated futures account with %s USDC", f"{starting_balance:,.2f}")

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

    def equity(self, marks):
        """Balance plus every open position's margin and unrealized profit at the given prices."""
        return self.balance + sum(
            pos["margin"] + unrealized_pnl(pos, marks[coin]) for coin, pos in self.positions.items()
        )

    def _record(self, at, coin, action, pos, price, fee=0.0, pnl=0.0, signal_id=None, reason=None):
        entry = {
            "time": iso(at), "coin": coin, "action": action, "side": pos["side"],
            "size": pos["size"], "price": price, "leverage": pos["leverage"],
            "fee": round(fee, 6), "pnl": round(pnl, 6), "funding": round(pos.get("funding", 0.0), 6),
            "balance": round(self.balance, 6),
        }
        if signal_id:
            entry["signal_id"] = signal_id
        if reason:
            entry["reason"] = reason
        self.state["history"].append(entry)

    def open(self, coin, side, margin, leverage, market, stop_pct=None, signal_id=None):
        """Open a long or short at market. Returns the position, or None if this signal was already traded."""
        if signal_id and self.has_signal(signal_id):
            log.info("%s: %s was already traded; skipping.", coin, signal_id)
            return None
        if coin in self.positions:
            raise RuntimeError(f"{coin}: a position is already open")
        leverage = min(leverage, market["max_leverage"])
        notional = margin * leverage
        expected_fee = notional * self.taker_fee
        if margin + expected_fee > self.balance:
            raise RuntimeError(f"{coin}: not enough balance ({self.balance:,.2f}) for {margin:,.2f} margin plus fees")

        price, size = fill(coin, "buy" if side == "long" else "sell", notional=notional)
        fee = price * size * self.taker_fee
        pos = {
            "side": side, "size": size, "entry": price, "leverage": leverage, "margin": margin,
            # Hyperliquid's maintenance margin is half the initial margin at the coin's max leverage.
            "mm_rate": 1 / (2 * market["max_leverage"]),
            "stop": (price * (1 - stop_pct) if side == "long" else price * (1 + stop_pct)) if stop_pct else None,
            "opened": now_ms(), "funding": 0.0,
        }
        if signal_id:
            pos["signal_id"] = signal_id
        self.state["balance"] -= margin + fee
        self.positions[coin] = pos
        self._record(pos["opened"], coin, "open", pos, price, fee=fee, signal_id=signal_id)
        log.info(
            "%s: opened %s %.6g @ %.6g, %gx, margin %.2f, fee %.2f, stop %s, liquidation %.6g",
            coin, side, size, price, leverage, margin, fee,
            f"{pos['stop']:.6g}" if pos["stop"] else "none", liquidation_price(pos),
        )
        return pos

    def close(self, coin, reason, price=None, at=None, signal_id=None):
        """Close a position at market (or at `price`, for stops replayed from candles). Returns the profit."""
        pos = self.positions.pop(coin)
        if price is None:
            price, _ = fill(coin, "sell" if pos["side"] == "long" else "buy", size=pos["size"])
        at = at or now_ms()
        pnl = unrealized_pnl(pos, price)
        fee = price * pos["size"] * self.taker_fee
        if pos["margin"] + pnl - fee <= 0:  # isolated margin: the loss stops at the margin
            self.positions[coin] = pos
            return self._liquidate(coin, price, at)
        self.state["balance"] += pos["margin"] + pnl - fee
        self._record(at, coin, "close", pos, price, fee=fee, pnl=pnl, signal_id=signal_id, reason=reason)
        log.info(
            "%s: closed %s @ %.6g (%s), profit %.2f after %.2f fee, funding %.2f",
            coin, pos["side"], price, reason, pnl - fee, fee, pos["funding"],
        )
        return pnl - fee

    def _liquidate(self, coin, price, at):
        pos = self.positions.pop(coin)
        self._record(at, coin, "liquidation", pos, price, pnl=-pos["margin"], reason="liquidated")
        log.warning("%s: LIQUIDATED %s @ %.6g, lost the %.2f margin", coin, pos["side"], price, pos["margin"])
        return -pos["margin"]

    def _check_exits(self, coin, pos, candle):
        """Apply a stop-loss or liquidation hit during this hourly candle. Returns what happened, if anything."""
        long = pos["side"] == "long"
        levels = [("liquidation", liquidation_price(pos))]
        if pos.get("stop"):
            levels.append(("stop-loss", pos["stop"]))
        # Price moves against a long from above (against a short from below), so the nearest level triggers first.
        levels.sort(key=lambda lv: -lv[1] if long else lv[1])
        for kind, level in levels:
            gapped = candle["o"] <= level if long else candle["o"] >= level
            touched = candle["l"] <= level if long else candle["h"] >= level
            if gapped or touched:
                price = candle["o"] if gapped else level
                if kind == "liquidation":
                    self._liquidate(coin, price, candle["t"])
                else:
                    self.close(coin, "stop-loss", price=price, at=candle["t"])
                return kind
        return None

    def sync(self, now=None):
        """Replay every finished hour since the last sync: stop-losses, liquidations and funding."""
        now = now or now_ms()
        current_hour = now // HOUR_MS * HOUR_MS  # start of the unfinished hour; replay up to here
        for coin in list(self.positions):
            pos = self.positions[coin]
            opened_hour_end = (pos["opened"] // HOUR_MS + 1) * HOUR_MS
            start = max(self.state["last_sync"], opened_hour_end)
            if start >= current_hour:
                continue
            candles = [c for c in get_candles(coin, "1h", start, current_hour - 1) if start <= c["t"] < current_hour]
            rates = get_funding(coin, start, current_hour + HOUR_MS)
            for candle in sorted(candles, key=lambda c: c["t"]):
                if self._check_exits(coin, pos, candle):
                    break
                # Funding is settled at the end of each hour on the position's value.
                rate = rates.get(candle["t"] + HOUR_MS, 0.0)
                payment = pos["size"] * candle["c"] * rate
                change = -payment if pos["side"] == "long" else payment
                pos["margin"] += change
                pos["funding"] += change
        self.state["last_sync"] = max(self.state["last_sync"], current_hour)
