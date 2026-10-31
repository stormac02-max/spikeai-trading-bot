# SpikeAI Project Log

The running record of everything done on this project: the backup of our work and Claude's memory between
sessions. Claude reads it at the start of each session and adds a dated entry under **History** after every
significant action, keeping **Current state** up to date.

**Never put API keys, secrets or passwords in this file.** It is committed to GitHub.

Times: the user is in Pakistan (PKT, UTC+5, no daylight saving). The US market is 9:30 AM–4:00 PM ET, which is
6:30 PM–1:00 AM PKT while the US is on EDT and 7:30 PM–2:00 AM PKT on EST (from Nov 1, 2026 until Mar 14, 2027).

---

## Current state (updated 2026-10-31)

**Alpaca paper account** ending `YUU8`: opened 2026-10-14 with $50,000. Crypto trading is enabled on it.
- Cash $48,121.13 (last seen in the bot log, 2026-10-30).
- Holding 2 MU (Micron), bought by hand on 2026-10-14 at $939.93 and $938.93.
- The old $500 paper account ending `DUM9` was deleted by the user on 2026-10-14. Its keys are dead.

**Stock bot** (`trading_bot.py`): 20/50-day simple moving average crossover on daily closes. Watchlist
`symbols = ["AAPL"]`, 1 share per trade, long-only (sells only shares it holds, never shorts). No bot trades
yet: AAPL's 20-day average has been above its 50-day since the buy crossover on 2026-09-15, so every run so
far has ended in "no signal".

**Automation**
- **GitHub Actions** (main runner): private repo `stormac02-max/spikeai-trading-bot`, workflow
  `.github/workflows/trading-bot.yml`. Cron is weekdays 13:20 UTC and the bot waits for the 9:30 ET open, but
  GitHub has started every run late, between 1:27 and 3:21 PM ET. After each run the log is committed to
  `logs/trading_bot.log` (times in ET since 2026-10-16; the first two days are in UTC). Secrets:
  `APCA_API_KEY_ID`, `APCA_API_SECRET_KEY`. Manual runs: Actions tab → MA crossover bot → Run workflow
  (dry run is ticked by default).
- **Windows Task Scheduler** (backup on this PC): task `SpikeAI MA Crossover Bot`, weekdays at 13:30 UTC
  (6:30 PM PKT). It runs `pythonw.exe trading_bot.py --wait-for-open`, which skips market holidays and waits
  for 9:30 ET. It only runs when the PC is on and the user is signed in, and catches up on a missed run when
  the PC comes back on. Its log is `trading_bot.log` in the project folder, which is not in git.
- **No double orders:** each order uses client_order_id `macross-{SYMBOL}-{buy|sell}-{signal date}`, and
  Alpaca rejects a reused ID, so the GitHub and PC runs can't both trade the same signal.

**Claude Code MCP:** the `alpaca` MCP server (`uvx alpaca-mcp-server` v2) is registered at user scope with the
YUU8 keys. Its read tools work, but `place_stock_order` fails with "request body format is invalid", so orders
are placed with the REST API or alpaca-py instead.

**Open items**
- Crypto paper trading: the user asked for it on 2026-10-31. Details still to be agreed.
- GitHub runs start about 4–5 hours late. Possible fixes: a cron-job.org timer that starts the workflow at
  9:30 ET (needs a GitHub token), or a small cloud server. Not decided.
- US daylight saving ends 2026-11-01. From Nov 2 the open is 7:30 PM PKT. The bot already handles this by
  starting at 13:30 UTC and waiting for 9:30 ET.

---

## Key facts

**Environment**
- Project folder: `C:\Users\786\Desktop\SpikeAI`. Windows 10, Python 3.12 at
  `C:\Users\786\AppData\Local\Programs\Python\Python312`.
- Installed packages: alpaca-py, yfinance, python-dotenv, uv (provides `uvx`, for the MCP server), pyyaml.
- Git identity (this repository only): Apfinance <Apfinance@ivgeliquids.com>. GitHub sign-in goes through Git
  Credential Manager. Always run `git pull --rebase` before pushing, because GitHub commits a log every weekday.

**Files**

| File | Purpose |
|---|---|
| `trading_bot.py` | The bot. `--dry-run` reports without ordering; `--wait-for-open` skips holidays and waits for 9:30 ET; `--config` picks a config file. |
| `config.toml` | `symbols`, `short_window` (20), `long_window` (50), `trade_qty` (1), `lookback_days` (100 trading days). |
| `test_alpaca_connection.py` | Read-only check: account and market clock. Auto-detects paper vs live keys. |
| `requirements.txt` | alpaca-py, python-dotenv, yfinance. |
| `.github/workflows/trading-bot.yml` | GitHub schedule. Commits `logs/trading_bot.log` after each run. |
| `.env` | Alpaca keys (`APCA_API_KEY_ID`, `APCA_API_SECRET_KEY`). Git-ignored and never committed. |
| `trading_bot.log` | Log from this PC's runs. Git-ignored. |
| `logs/trading_bot.log` | Log from GitHub's runs, committed by the workflow. |
| `PROJECT_LOG.md` | This file. |
| `CLAUDE.md` | Tells Claude to read and update this log. |

**How the bot decides**
- Uses the last 100 completed trading days from yfinance. Today's bar is dropped while the market is open.
- Buy when SMA20 goes from ≤ SMA50 to > SMA50 between the last two days. Sell when it goes from ≥ to <.
- A sell is skipped if fewer than `trade_qty` shares are held. Market orders, time in force DAY.
- Every run logs the account's cash and buying power. A failing ticker is logged and skipped, and the run exits
  with code 1 so GitHub emails the user.

**Ground rules**
- Paper trading only. The code pins the paper endpoint (`paper=True`).
- Claude does not recommend which stocks or coins to buy, because it is not a licensed advisor. The user chooses
  the tickers. Claude can scan, backtest or run the user's own strategy on the user's list.
- The user makes account changes in the Alpaca dashboard (new paper accounts, API keys) and on GitHub
  (repository, secrets).

**Useful commands** (run in the project folder)
- `python test_alpaca_connection.py`: is the account reachable?
- `python trading_bot.py --dry-run`: what would the bot do right now?
- `python trading_bot.py`: run it for real (paper).

---

## History

### 2026-10-11: Connecting to Alpaca
- Started with an empty folder. Created the `.env` template and `test_alpaca_connection.py`.
- The user registered the Alpaca MCP server with paper keys for account DUM9 ($500). `uvx` was missing, so
  installed uv 0.13.0 with pip, and the MCP server then connected.
- Connection confirmed: paper account DUM9, ACTIVE, $500 cash.
- Tried to buy 1 MU. Rejected for insufficient buying power (about $1,028 a share vs $500). The MCP order tool
  failed with "request body format is invalid", so the order went through the REST API instead.
- Per Alpaca's docs, a paper account's balance can't be changed. The only way is a new paper account from the
  dashboard.

### 2026-10-14: $50k account, Micron, the bot, scheduling, GitHub
- The user opened paper account YUU8 with $50,000 and deleted DUM9. The new keys went into `.env`, and the MCP
  server was re-registered with them.
- Bought 1 MU at market, twice. The user asked twice and confirmed a second share was wanted. Order IDs
  `e9cfe0f3…` and `703d1303…`, both filled at the Oct 14 open, at $939.93 and $938.93.
- Built `trading_bot.py`, `config.toml` and `requirements.txt`. Tested the crossover logic on synthetic prices,
  then dry-ran on live AAPL data: no crossover.
- Created the Windows scheduled task for weekdays at 9:30 ET (13:30 UTC trigger plus waiting, to handle
  daylight saving; skips market holidays). The same day the PC lost power at 5:08 PM PKT, before the run.
- Moved the bot to GitHub Actions. The user created the private repo and added the two secrets. The workflow
  commits the log after each run. The bot was changed to check the account on every run, which proves the keys
  work.
- Told the user that GitHub runs could be a few minutes late. They turned out to be hours late (see Oct 16).

### 2026-10-16: Watchlist, and why nothing traded
- The bot now trades a watchlist (a `symbols` list in `config.toml`). Each ticker is checked on its own, a bad
  ticker doesn't stop the others, and GitHub logs show ET.
- Found that GitHub's runs started about 4.5 hours late (Oct 14 at 2:02 PM ET, Oct 15 at 1:47 PM ET). The PC
  copy missed those days because the PC lost power unexpectedly twice (Oct 14 at 5:08 PM PKT and Oct 15 at
  1:39 AM PKT). GitHub ran fine while the PC was off.
- No trades so far because there's no crossover. AAPL had 14 SMA20/50 crossovers in the past two years; the
  latest was a BUY on 2026-09-15.
- The user asked which stocks to buy. Declined (not a licensed advisor) and offered a scan, a backtest or a
  watchlist. The user chose the watchlist but hasn't added tickers beyond AAPL.

### 2026-10-16 to 2026-10-30: Daily runs
- GitHub ran on every weekday: Oct 16, 19–23, 26–30. Start times were 1:27–3:21 PM ET.
- The PC task ran on days the PC was on: Oct 20, 22, 27, 28 and 29. It correctly skipped the weekends of Oct 17
  and Oct 31.
- Every run: AAPL no signal, no orders. Cash unchanged at $48,121.13.

### 2026-10-31: This log, and crypto next
- The user asked to move on to crypto paper trading, and to keep a backup log that Claude also uses as memory.
  Created `PROJECT_LOG.md` (this file) and `CLAUDE.md`, which tells Claude to read this log at the start of
  every session and update it after every significant action. Also saved a note in Claude's own memory
  pointing here.
- The internet was down at the time (GitHub and Alpaca unreachable), so the account and crypto details could
  not be checked live yet.
