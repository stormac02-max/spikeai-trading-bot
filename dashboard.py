"""Local dashboard for the simulated futures accounts.

Run it with `python dashboard.py`; it opens http://127.0.0.1:8765 in your browser.

It reads the accounts in state/, futures_config.toml and the bot logs, and prices open positions live
from Hyperliquid. "Pull latest" runs `git pull` to fetch the accounts the daily GitHub run committed,
and the signal board shows what each strategy currently sees for every coin. It only listens on this
PC (127.0.0.1) and never changes the accounts.
"""

import argparse
import json
import os
import re
import subprocess
import threading
import time
import tomllib
import webbrowser
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from backtest_futures import build_indicators
from futures_bot import STRATEGIES, UNIVERSE_FILE, daily_frames
from paper_futures import BASE_DIR, get_markets, liquidation_price, unrealized_pnl

PAGE = BASE_DIR / "dashboard" / "index.html"
LOGS = {"GitHub": BASE_DIR / "logs" / "futures_bot.log", "This PC": BASE_DIR / "futures_bot.log"}
RUN_START = re.compile(r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}),\d+ INFO ---- Futures run started")

_cache, _lock = {}, threading.Lock()


def cached(key, seconds, compute):
    with _lock:
        hit = _cache.get(key)
        if hit and time.time() - hit[0] < seconds:
            return hit[1]
    value = compute()
    with _lock:
        _cache[key] = (time.time(), value)
    return value


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else None


def read_config():
    with open(BASE_DIR / "futures_config.toml", "rb") as f:
        return tomllib.load(f)


def distance_pct(pos, mark, level):
    """How far the price can still move against the position before reaching `level`, in % of the price."""
    if level is None or not mark:
        return None
    return ((mark - level) if pos["side"] == "long" else (level - mark)) / mark * 100


def account_view(key, state, marks, config):
    start = config["starting_balance"]
    if state is None:
        return {"key": key, "name": STRATEGIES[key][0], "exists": False}

    positions, open_value = [], 0.0
    for coin, pos in state["positions"].items():
        mark = marks.get(coin)
        pnl = unrealized_pnl(pos, mark) if mark else 0.0
        open_value += pos["margin"] + pnl
        liq = liquidation_price(pos)
        positions.append({
            "coin": coin, "side": pos["side"], "size": pos["size"], "entry": pos["entry"], "mark": mark,
            "value": pos["size"] * (mark or pos["entry"]), "margin": pos["margin"], "leverage": pos["leverage"],
            "pnl": pnl, "pnl_pct": pnl / pos["margin"] * 100 if pos["margin"] else 0.0,
            "stop": pos.get("stop"), "to_stop_pct": distance_pct(pos, mark, pos.get("stop")),
            "liquidation": liq, "to_liq_pct": distance_pct(pos, mark, liq),
            "funding": pos.get("funding", 0.0),
            "opened": datetime.fromtimestamp(pos["opened"] / 1000, tz=timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        })

    equity = state["balance"] + open_value
    history = state.get("history", [])
    closed = [h for h in history if h["action"] in ("close", "liquidation")]
    net = [h["pnl"] - h["fee"] + h.get("funding", 0.0) for h in closed]
    curve = [{"date": h["date"], "equity": h["equity"]} for h in state.get("equity_history", [])]
    curve.append({"date": "now", "equity": round(equity, 2)})
    peak = max([start] + [p["equity"] for p in curve])
    return {
        "key": key, "name": STRATEGIES[key][0], "exists": True,
        "created": state.get("created"), "balance": state["balance"], "equity": equity,
        "return_pct": (equity / start - 1) * 100, "drawdown_pct": (1 - equity / peak) * 100,
        "positions": positions, "closed_trades": len(closed),
        "wins": sum(1 for n in net if n > 0), "realized": sum(net),
        "fees": sum(h["fee"] for h in history),
        "funding": sum(h.get("funding", 0.0) for h in closed) + sum(p["funding"] for p in positions),
        "stops": sum(1 for h in closed if h.get("reason") == "stop-loss"),
        "liquidations": sum(1 for h in closed if h["action"] == "liquidation"),
        "history": history[-60:], "curve": curve,
    }


def last_runs():
    runs, newest = {}, (None, None)
    for where, path in LOGS.items():
        if not path.exists():
            continue
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        starts = [i for i, line in enumerate(lines) if RUN_START.match(line)]
        if starts:
            stamp = RUN_START.match(lines[starts[-1]]).group(1)
            runs[where] = stamp + " PKT"
            if newest[0] is None or stamp > newest[0]:
                newest = (stamp, lines[starts[-1]:][-60:])
    return runs, newest[1] or []


def git_updated():
    try:
        out = subprocess.run(["git", "log", "-1", "--format=%cd", "--date=format-local:%Y-%m-%d %H:%M", "--", "state"],
                             cwd=BASE_DIR, capture_output=True, text=True, timeout=15)
        return out.stdout.strip() or None
    except Exception:
        return None


def status():
    config = read_config()
    marks = cached("marks", 20, lambda: {c: m["mark"] for c, m in get_markets().items()})
    accounts = [account_view(key, read_json(BASE_DIR / f"state/futures_{key}.json"), marks, config)
                for key in config["strategies"]]
    runs, log_tail = last_runs()
    until = config.get("evaluation_until")
    return {
        "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "settings": {k: config[k] for k in ("leverage", "stop_pct", "margin_usd", "starting_balance",
                                            "taker_fee", "universe_size", "universe_exclude")},
        "evaluation_until": str(until) if until else None,
        "days_left": (until - datetime.now(timezone.utc).date()).days if until else None,
        "universe": read_json(UNIVERSE_FILE),
        "accounts": accounts,
        "last_runs": runs, "accounts_committed": git_updated(),
        "log_tail": log_tail,
    }


def signal_board():
    universe = (read_json(UNIVERSE_FILE) or {}).get("coins", [])
    if not universe:
        return {"day": None, "rows": []}
    closes, highs, lows = daily_frames(universe)
    ind = build_indicators(closes, highs, lows)
    day = closes.index[-1]
    i = closes.index.get_loc(day)
    ret = ind["ret14"].loc[day, universe].dropna().sort_values(ascending=False)
    picks = min(5, len(ret) // 2)
    longs, shorts = set(ret.index[:picks]), set(ret.index[len(ret) - picks:])

    def num(x):
        return None if x != x else float(x)  # NaN -> None

    rows = []
    for coin in universe:
        s20, s50 = ind["sma20"][coin], ind["sma50"][coin]
        cur_s, cur_l, prev_s, prev_l = num(s20.iloc[i]), num(s50.iloc[i]), num(s20.iloc[i - 1]), num(s50.iloc[i - 1])
        crossed = None
        if None not in (cur_s, cur_l, prev_s, prev_l):
            crossed = "up" if prev_s <= prev_l and cur_s > cur_l else "down" if prev_s >= prev_l and cur_s < cur_l else None
        close = num(closes.loc[day, coin])
        hh20, ll20 = num(ind["hh20"].loc[day, coin]), num(ind["ll20"].loc[day, coin])
        hh10, ll10 = num(ind["hh10"].loc[day, coin]), num(ind["ll10"].loc[day, coin])
        rows.append({
            "coin": coin, "close": close,
            "sma20": cur_s, "sma50": cur_l, "ma_gap_pct": (cur_s / cur_l - 1) * 100 if cur_s and cur_l else None,
            "crossed": crossed,
            "hh20": hh20, "ll20": ll20, "hh10": hh10, "ll10": ll10,
            "to_high_pct": (hh20 / close - 1) * 100 if close and hh20 else None,
            "to_low_pct": (1 - ll20 / close) * 100 if close and ll20 else None,
            "breakout": ("above" if close > hh20 else "below" if close < ll20 else "inside") if close and hh20 and ll20 else None,
            "ret14_pct": num(ret.get(coin)) * 100 if coin in ret else None,
            "rank": list(ret.index).index(coin) + 1 if coin in ret else None,
            "momentum": "long" if coin in longs else "short" if coin in shorts else None,
        })
    return {"day": str(day.date()), "rows": rows}


def pull_latest():
    env = dict(os.environ, GIT_TERMINAL_PROMPT="0")
    result = subprocess.run(["git", "pull", "--rebase"], cwd=BASE_DIR, capture_output=True, text=True, timeout=90, env=env)
    with _lock:
        _cache.pop("signals", None)
    return {"ok": result.returncode == 0, "output": (result.stdout + result.stderr).strip()[-2000:]}


class Handler(BaseHTTPRequestHandler):
    def _send(self, code, body, content_type="application/json"):
        data = body if isinstance(body, bytes) else json.dumps(body, default=str).encode()
        self.send_response(code)
        self.send_header("Content-Type", content_type)
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        try:
            if self.path in ("/", "/index.html"):
                self._send(200, PAGE.read_bytes(), "text/html; charset=utf-8")
            elif self.path == "/api/status":
                self._send(200, status())
            elif self.path == "/api/signals":
                self._send(200, cached("signals", 900, signal_board))
            else:
                self._send(404, {"error": "not found"})
        except Exception as error:
            self._send(500, {"error": str(error)})

    def do_POST(self):
        try:
            if self.path == "/api/pull":
                self._send(200, pull_latest())
            else:
                self._send(404, {"error": "not found"})
        except Exception as error:
            self._send(500, {"error": str(error)})

    def log_message(self, *args):
        pass  # keep the console quiet


def main():
    parser = argparse.ArgumentParser(description="Local dashboard for the simulated futures accounts.")
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument("--no-browser", action="store_true", help="don't open the browser automatically")
    args = parser.parse_args()
    server = ThreadingHTTPServer(("127.0.0.1", args.port), Handler)
    url = f"http://127.0.0.1:{args.port}"
    print(f"Futures dashboard running at {url}  (Ctrl+C to stop)")
    if not args.no_browser:
        threading.Timer(1.0, webbrowser.open, [url]).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
