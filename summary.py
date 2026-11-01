"""Write the daily summary page: README.md plus the chart in reports/equity.svg.

GitHub shows README.md on the repository's front page, in a browser and in the GitHub mobile app, so
the paper test can be checked from a phone. The futures workflow runs this right after the bot, so the
page refreshes every day. It reuses the dashboard's data (dashboard.status and signal_board) and adds
the Alpaca spot account. It only reads; it never trades or changes an account.

Usage:
  python summary.py
"""

import math
import os
import sys
import tomllib
from datetime import datetime, timezone

import pandas as pd

import dashboard
from paper_futures import BASE_DIR

README = BASE_DIR / "README.md"
CHART = BASE_DIR / "reports" / "equity.svg"
PKT = "Asia/Karachi"
DOT = {"ma_crossover": "🔵", "breakout": "🟠", "momentum": "🟢"}
LIGHT = {"ma_crossover": "#2a78d6", "breakout": "#eb6834", "momentum": "#1baf7a"}
DARK = {"ma_crossover": "#3987e5", "breakout": "#d95926", "momentum": "#199e70"}


# ---- formatting ------------------------------------------------------------------

def money(x, signed=False, decimals=2):
    if x is None:
        return "–"
    sign = "+" if signed and x > 0 else "−" if x < 0 else ""
    return f"{sign}${abs(x):,.{decimals}f}"


def pct(x, decimals=1):
    if x is None:
        return "–"
    sign = "+" if x > 0 else "−" if x < 0 else ""
    return f"{sign}{abs(x):.{decimals}f}%"


def price(x):
    if x is None:
        return "–"
    if abs(x) >= 1:
        return f"{x:,.4f}".rstrip("0").rstrip(".") if abs(x) < 100 else f"{x:,.2f}"
    return f"{x:.{min(10, 4 - math.floor(math.log10(abs(x))))}f}".rstrip("0")


def local(utc_text, fmt="%a %d %b, %H:%M"):
    """'2026-10-31 20:46 UTC' -> 'Sun 01 Nov, 01:46' in Pakistan time."""
    stamp = pd.Timestamp(utc_text.replace(" UTC", ""), tz="UTC")
    return stamp.tz_convert(PKT).strftime(fmt)


def distance(d):
    if d is None:
        return "–"
    return f"{'✅' if d >= 5 else '⚠️' if d >= 2 else '🔴'} {d:.1f}%"


# ---- chart -----------------------------------------------------------------------

def equity_svg(accounts, start):
    """Line chart of each account's value, light and dark aware, with direct labels."""
    dates = sorted({p["date"] for a in accounts for p in a["curve"]}, key=lambda d: (d == "now", d))
    W, H, ml, mr, mt, mb = 720, 260, 64, 110, 16, 30
    values = [p["equity"] for a in accounts for p in a["curve"]] + [start]
    lo, hi = min(values), max(values)
    pad = max((hi - lo) * 0.15, hi * 0.005)
    lo, hi = lo - pad, hi + pad
    x = (lambda i: ml + (W - ml - mr) / 2) if len(dates) == 1 else (lambda i: ml + i * (W - ml - mr) / (len(dates) - 1))
    y = lambda v: mt + (hi - v) / (hi - lo) * (H - mt - mb)

    style = ["text{font:11px system-ui,-apple-system,'Segoe UI',sans-serif;fill:#898781}",
             ".bg{fill:#fcfcfb}.grid{stroke:#e1e0d9}.base{stroke:#c3c2b7}.lbl{fill:#52514e;font-size:12px}"]
    style += [f".{k}{{stroke:{c};fill:{c}}}" for k, c in LIGHT.items()]
    dark = [".bg{fill:#1a1a19}.grid{stroke:#2c2c2a}.base{stroke:#383835}.lbl{fill:#c3c2b7}"]
    dark += [f".{k}{{stroke:{c};fill:{c}}}" for k, c in DARK.items()]
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
             f'aria-label="Account value over time for each strategy">',
             f"<style>{''.join(style)}@media (prefers-color-scheme: dark){{{''.join(dark)}}}</style>",
             f'<rect class="bg" width="{W}" height="{H}" rx="10"/>']
    for k in range(5):
        v = lo + (hi - lo) * k / 4
        parts.append(f'<line class="grid" x1="{ml}" x2="{W - mr}" y1="{y(v):.1f}" y2="{y(v):.1f}"/>')
        parts.append(f'<text x="{ml - 8}" y="{y(v) + 4:.1f}" text-anchor="end">${v:,.0f}</text>')
    parts.append(f'<line class="base" x1="{ml}" x2="{W - mr}" y1="{y(start):.1f}" y2="{y(start):.1f}" stroke-dasharray="4 4"/>')
    parts.append(f'<text x="{ml + 4}" y="{y(start) - 5:.1f}">start</text>')
    step = max(1, -(-len(dates) // 7))
    for i, d in enumerate(dates):
        if i % step == 0 or i == len(dates) - 1:
            parts.append(f'<text x="{x(i):.1f}" y="{H - 10}" text-anchor="middle">{d}</text>')

    ends = []
    for a in accounts:
        pts = [(x(dates.index(p["date"])), y(p["equity"])) for p in a["curve"]]
        pts.sort()
        if len(pts) > 1:
            path = "M" + "L".join(f"{px:.1f},{py:.1f}" for px, py in pts)
            parts.append(f'<path class="{a["key"]}" d="{path}" fill="none" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>')
        for px, py in pts:
            parts.append(f'<circle class="{a["key"]}" cx="{px:.1f}" cy="{py:.1f}" r="4" stroke="none"/>')
        if pts:
            ends.append([pts[-1][1], a["name"].split(" ")[0]])
    ends.sort()
    for k in range(1, len(ends)):  # nudge direct labels apart
        ends[k][0] = max(ends[k][0], ends[k - 1][0] + 14)
    for ly, label in ends:
        parts.append(f'<text class="lbl" x="{W - mr + 10}" y="{ly + 4:.1f}">{label}</text>')
    parts.append("</svg>")
    return "\n".join(parts)


# ---- page sections -----------------------------------------------------------------

def futures_section(s, signals):
    st, accounts = s["settings"], [a for a in s["accounts"] if a["exists"]]
    out = ["## Futures test: MA crossover vs breakout vs momentum", ""]
    if s["days_left"] is not None:
        out.append(f"**{max(0, s['days_left'])} days left** in the evaluation (until {s['evaluation_until']}), then the best strategy is kept.  ")
    out.append(f"Each simulated account started with {money(st['starting_balance'], decimals=0)}: "
               f"{st['leverage']}x leverage, {st['stop_pct'] * 100:.0f}% stop-loss, {money(st['margin_usd'], decimals=0)} margin per trade, long and short.")
    out += ["", "| Strategy | Value | Return | Below peak | Open | Closed (won) | Fees | Funding |",
            "|---|--:|--:|--:|--:|--:|--:|--:|"]
    for a in accounts:
        won = f"{a['closed_trades']} ({a['wins']})" if a["closed_trades"] else "0"
        below = f"−{a['drawdown_pct']:.2f}%" if a["drawdown_pct"] > 0.005 else "at peak"
        out.append(f"| {DOT[a['key']]} {a['name']} | **{money(a['equity'])}** | {pct(a['return_pct'], 2)} | {below} | "
                   f"{len(a['positions'])} | {won} | {money(a['fees'])} | {money(a['funding'], signed=True)} |")
    ranked = sorted(accounts, key=lambda a: a["equity"], reverse=True)
    if len(ranked) > 1 and ranked[0]["history"] and ranked[0]["equity"] - ranked[1]["equity"] > 1:
        out += ["", f"**Leading:** {DOT[ranked[0]['key']]} {ranked[0]['name']}, "
                    f"{money(ranked[0]['equity'] - ranked[1]['equity'])} ahead of {ranked[1]['name']}."]
    else:
        out += ["", "_No clear leader yet._"]

    out += ["", "![Account value over time](reports/equity.svg)", "",
            "<details><summary>Account values as a table</summary>", "",
            "| Date | " + " | ".join(a["name"] for a in accounts) + " |", "|---|" + "--:|" * len(accounts)]
    dates = sorted({p["date"] for a in accounts for p in a["curve"]}, key=lambda d: (d == "now", d))
    for d in dates:
        row = [money(next((p["equity"] for p in a["curve"] if p["date"] == d), None)) for a in accounts]
        out.append(f"| {d} | " + " | ".join(row) + " |")
    out += ["", "</details>", ""]

    out += ["### Open positions", ""]
    positions = [(a, p) for a in accounts for p in a["positions"]]
    if positions:
        out += ["| Strategy | Coin | Side | Entry → now | Profit | To stop | To liquidation |", "|---|---|---|---|--:|--:|--:|"]
        for a, p in positions:
            side = "▲ Long" if p["side"] == "long" else "▼ Short"
            out.append(f"| {DOT[a['key']]} {a['name'].split(' ')[0]} | **{p['coin']}** | {side} | {price(p['entry'])} → {price(p['mark'])} | "
                       f"{money(p['pnl'], signed=True)} ({pct(p['pnl_pct'])}) | {distance(p['to_stop_pct'])} | {distance(p['to_liq_pct'])} |")
        out += ["", "_Distance = how far the price can still move against the position. ✅ over 5% · ⚠️ 2–5% · 🔴 under 2%._"]
    else:
        out.append("_No open positions._")

    out += ["", "### Recent trades", ""]
    trades = sorted(((a, h) for a in accounts for h in a["history"]), key=lambda t: t[1]["time"], reverse=True)[:15]
    if trades:
        out += ["| Time (PKT) | Strategy | Coin | What | Price | Result |", "|---|---|---|---|--:|--:|"]
        for a, h in trades:
            what = {"open": "Opened", "liquidation": "Liquidated"}.get(h["action"], "Stopped out" if h.get("reason") == "stop-loss" else "Closed")
            what += " " + ("long" if h["side"] == "long" else "short")
            result = f"fee {money(h['fee'])}" if h["action"] == "open" else money(h["pnl"] - h["fee"] + h.get("funding", 0.0), signed=True)
            out.append(f"| {local(h['time'])} | {DOT[a['key']]} {a['name'].split(' ')[0]} | **{h['coin']}** | {what} | {price(h['price'])} | {result} |")
    else:
        out.append("_No trades yet._")

    if signals and signals["rows"]:
        out += ["", f"### Signal board (daily candle of {signals['day']})", "",
                "What each strategy sees per coin. 🔔 = the condition for a trade is met.", "",
                "| Coin | MA: 20d vs 50d | Breakout: vs 20-day range | Momentum: 14d return |", "|---|---|---|---|"]
        for r in signals["rows"]:
            ma = "–" if r["ma_gap_pct"] is None else f"{'above' if r['ma_gap_pct'] > 0 else 'below'} ({pct(r['ma_gap_pct'])})"
            if r["crossed"]:
                ma += f" 🔔 crossed {r['crossed']}"
            if r["breakout"] == "above":
                bo = "🔔 above 20d high"
            elif r["breakout"] == "below":
                bo = "🔔 below 20d low"
            else:
                bo = "–" if r["to_high_pct"] is None else f"{pct(r['to_high_pct'])} to high / {pct(-r['to_low_pct'])} to low"
            mo = "–" if r["ret14_pct"] is None else f"{pct(r['ret14_pct'])} (#{r['rank']})"
            if r["momentum"]:
                mo += " 🔔 " + ("top 5: long" if r["momentum"] == "long" else "bottom 5: short")
            out.append(f"| **{r['coin']}** | {ma} | {bo} | {mo} |")
        out += ["", "_Momentum trades its top/bottom 5 at the Monday rebalance; MA and breakout act at each daily run._"]

    if s["universe"]:
        out += ["", f"### This week's coins (chosen {s['universe']['refreshed']})", "",
                " · ".join(s["universe"]["coins"]),
                "", f"_The {st['universe_size']} most-traded Hyperliquid futures over the past week, excluding "
                    f"{' and '.join(st['universe_exclude'])}. Refreshed Mondays 00:00 UTC (5:00 AM PKT)._"]
    return out


def alpaca_section():
    out = ["## Alpaca paper account (spot)", ""]
    try:
        from trading_bot import make_client
        client = make_client()
        account, positions = client.get_account(), client.get_all_positions()
        out.append(f"Value **{money(float(account.equity))}** · cash {money(float(account.cash))} · account ending {account.account_number[-4:]}  ")
        if positions:
            held = [f"{float(p.qty):g} {p.symbol} ({money(float(p.unrealized_pl), signed=True)})" for p in positions]
            out.append("Holding: " + ", ".join(held))
        else:
            out.append("No positions.")
    except Exception as error:
        out.append(f"_Couldn't reach the Alpaca account this run ({type(error).__name__})._")
    try:
        with open(BASE_DIR / "crypto_config.toml", "rb") as f:
            coins = tomllib.load(f)["symbols"]
        out += ["", f"Crypto spot bot: {'watching ' + ', '.join(coins) if coins else 'no coins on its watchlist yet'} (daily 00:15 UTC). "
                    "Stock bot: stopped."]
    except Exception:
        pass
    return out


def main():
    s = dashboard.status()
    try:
        signals = dashboard.signal_board()
    except Exception:
        signals = None  # the summary still gets written without the board
    now = datetime.now(timezone.utc)
    outcome = os.getenv("BOT_OUTCOME")
    run_line = {"success": "✅ Last run OK", "failure": "❌ **Last run failed:** see the log"}.get(outcome, "Generated on the PC")

    lines = ["# SpikeAI paper trading", "",
             f"_Updated **{pd.Timestamp(now).tz_convert(PKT).strftime('%a %d %b %Y, %H:%M')} PKT** "
             f"({pd.Timestamp(now).tz_convert('America/New_York').strftime('%a %H:%M')} ET). "
             "Refreshed after every daily run. Paper trading only: no real money._", ""]
    lines += futures_section(s, signals) + [""] + alpaca_section()
    lines += ["", "---", f"{run_line} · [futures log](logs/futures_bot.log) · [crypto log](logs/crypto_bot.log) · "
                         "[project log](PROJECT_LOG.md) · on the PC: `python dashboard.py`", "",
              "<sub>This page is written by summary.py; edits by hand are overwritten.</sub>", ""]
    README.write_text("\n".join(lines), encoding="utf-8")
    CHART.parent.mkdir(exist_ok=True)
    CHART.write_text(equity_svg([a for a in s["accounts"] if a["exists"]], s["settings"]["starting_balance"]), encoding="utf-8")
    print(f"Wrote {README.name} and {CHART.relative_to(BASE_DIR)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
