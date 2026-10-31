# SpikeAI Project Log

The running record of everything done on this project: the backup of our work and Claude's memory between
sessions. Claude reads it at the start of each session and adds a dated entry under **History** after every
significant action, keeping **Current state** up to date.

**Never put API keys, secrets or passwords in this file.** It is committed to GitHub.

Times: the user is in Pakistan (PKT, UTC+5, no daylight saving). The US market is 9:30 AM–4:00 PM ET, which is
6:30 PM–1:00 AM PKT while the US is on EDT and 7:30 PM–2:00 AM PKT on EST (from Nov 1, 2026 until Mar 14, 2027).

---

## Current state (updated 2026-10-31)

**Focus: crypto.** Since 2026-10-31 the project trades crypto only. The stock bot is stopped but kept, so it
can be resumed.

**Alpaca paper account** ending `YUU8`: opened 2026-10-14 with $50,000. Crypto trading is enabled on it.
- Cash $48,121.13. Crypto buying power $49,005.87 (crypto can't use margin).
- Holding 2 MU (Micron), bought by hand on 2026-10-14 at $939.93 and $938.93. At $884.74 on 2026-10-31 that's
  down $109.38. The stock bot never traded. No crypto held yet.
- The old $500 paper account ending `DUM9` was deleted by the user on 2026-10-14. Its keys are dead.

**Crypto bot** (`crypto_bot.py` + `crypto_config.toml`): the same 20/50-day simple moving average crossover, on
Alpaca's daily crypto candles. A buy signal buys `trade_usd = 500` dollars' worth. A sell signal sells that
coin's whole position, or is skipped if none is held. Market orders, time in force GTC. **Watchlist is empty
(`symbols = []`) until the user picks coins.** Until then each run only logs the account and "No coins on the
watchlist yet".

**Stock bot** (`trading_bot.py` + `config.toml`): **stopped 2026-10-31.** 20/50-day crossover on yfinance
daily closes, watchlist `["AAPL"]`, 1 share per trade, long-only. It never traded: AAPL's 20-day stayed above
its 50-day from 2026-09-15 through 2026-10-30.

**Automation**
- **GitHub Actions**: private repo `stormac02-max/spikeai-trading-bot`. Secrets: `APCA_API_KEY_ID`,
  `APCA_API_SECRET_KEY`.
  - `crypto-bot.yml` (**active**): every day at 00:15 UTC (5:15 AM PKT), just after Alpaca's daily candle
    closes at 00:00 UTC. GitHub usually starts scheduled runs late, which is fine for a daily signal. The log is
    committed to `logs/crypto_bot.log`, with times in PKT. Manual run: Actions tab → "MA crossover bot
    (crypto)" → Run workflow (dry run is ticked by default).
  - `trading-bot.yml` (stocks): **schedule removed**, manual runs only. The schedule is kept as a comment in
    the file. GitHub ran it every weekday 2026-10-14 to 10-30, starting 1:27–3:21 PM ET. Log is
    `logs/trading_bot.log`.
  - Both workflows share the concurrency group `trading-bot`, so their log commits never collide.
- **Windows Task Scheduler**: task `SpikeAI MA Crossover Bot` (stocks) is **disabled** (2026-10-31), not deleted.
  There is no PC task for crypto.
- **No double orders:** orders use client_order_id `macross-{SYMBOL without slash}-{buy|sell}-{signal date}`,
  and Alpaca rejects a reused ID.

**Claude Code MCP:** the `alpaca` MCP server (`uvx alpaca-mcp-server` v2) is registered at user scope with the
YUU8 keys. Its read tools work, but `place_stock_order` fails with "request body format is invalid", so orders
are placed with the REST API or alpaca-py instead. A Claude session keeps the MCP keys it started with. Sessions
started before 2026-10-14 still send the deleted DUM9 keys and get 401 Unauthorized, so open a new session to
use the Alpaca tools. The bots don't use the MCP server, so they're unaffected.

**Open items**
- **Coins for the crypto watchlist:** waiting on the user. Claude does not pick them. Alpaca has 36 tradable
  USD pairs: AAVE, ADA, ARB, AVAX, BAT, BCH, BONK, BTC, CRV, DOGE, DOT, ETH, FIL, GRT, HYPE, LDO, LINK, LTC,
  ONDO, PAXG, PEPE, POL, RENDER, SHIB, SKY, SOL, SUSHI, TRUMP, UNI, USDC, USDG, USDT, WIF, XRP, XTZ, YFI (each
  `/USD`).
- **Scope decided 2026-11-01:** no BTC or ETH trading (they're still watched as market indicators). Trade
  altcoins, new projects and memecoins, both **spot and futures** (paper only). Alpaca is spot-only and lists
  ~30 non-BTC/ETH/stablecoin pairs, so futures and brand-new DEX tokens need another venue or a simulated
  paper ledger. Not decided yet.
- **More strategies:** the user plans to add more. Each one is to be discussed with the user before it's added.
  Keep the moving average strategy as it is.
- If stocks resume: GitHub runs were 4–5 hours late (fixes: a cron-job.org trigger or a cloud server), and
  from 2026-11-02 the 9:30 ET open is 7:30 PM PKT (already handled by the 13:30 UTC start plus waiting).

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
| `crypto_bot.py` | Crypto bot (active). `--dry-run` reports without ordering; `--config` picks a config file. Reuses `detect_crossover`, `make_client` and `setup_logging` from `trading_bot.py`. |
| `crypto_config.toml` | `symbols` (Alpaca pairs like `"BTC/USD"`), `short_window` (20), `long_window` (50), `trade_usd` (500), `lookback_days` (100 days). |
| `trading_bot.py` | Stock bot (stopped). `--dry-run` reports without ordering; `--wait-for-open` skips holidays and waits for 9:30 ET; `--config` picks a config file. |
| `config.toml` | Stock settings: `symbols`, `short_window` (20), `long_window` (50), `trade_qty` (1 share), `lookback_days` (100 trading days). |
| `test_alpaca_connection.py` | Read-only check: account and market clock. Auto-detects paper vs live keys. |
| `requirements.txt` | alpaca-py, python-dotenv, yfinance. |
| `.github/workflows/crypto-bot.yml` | Crypto schedule (daily, 00:15 UTC). Commits `logs/crypto_bot.log` after each run. |
| `.github/workflows/trading-bot.yml` | Stock workflow, manual runs only. Commits `logs/trading_bot.log` after each run. |
| `.env` | Alpaca keys (`APCA_API_KEY_ID`, `APCA_API_SECRET_KEY`). Git-ignored and never committed. |
| `crypto_bot.log`, `trading_bot.log` | Logs from runs on this PC. Git-ignored. |
| `logs/crypto_bot.log`, `logs/trading_bot.log` | Logs from GitHub's runs, committed by the workflows. |
| `PROJECT_LOG.md` | This file. |
| `CLAUDE.md` | Tells Claude to read and update this log. |

**How the bots decide**
- Both: buy when SMA20 goes from ≤ SMA50 to > SMA50 between the last two completed days. Sell when it goes from
  ≥ to <. Every run logs the account. A failing ticker or coin is logged and skipped, and the run exits with code
  1 so GitHub emails the user.
- **Crypto:** daily candles from Alpaca's crypto data (00:00–24:00 UTC, so 20/50 are calendar days). The
  unfinished current-day candle is dropped. Buy = $`trade_usd` notional. Sell = the whole position
  (`qty_available`). Market, GTC (crypto accepts GTC or IOC only). Alpaca lists crypto positions as `BTCUSD`
  (no slash); the bot matches on that.
- **Stocks:** last 100 completed trading days from yfinance; today's bar is dropped while the market is open.
  Buy/sell `trade_qty` shares, and a sell is skipped if fewer are held. Market, DAY.

**Ground rules**
- Paper trading only. The code pins the paper endpoint (`paper=True`).
- Claude does not recommend which stocks or coins to buy, because it is not a licensed advisor. The user chooses
  the tickers. Claude can scan, backtest or run the user's own strategy on the user's list.
- New strategies are discussed with the user before they're added. The moving average strategy stays as is.
- The user makes account changes in the Alpaca dashboard (new paper accounts, API keys) and on GitHub
  (repository, secrets).

**Useful commands** (run in the project folder)
- `python test_alpaca_connection.py`: is the account reachable?
- `python crypto_bot.py --dry-run`: what would the crypto bot do right now?
- `python crypto_bot.py`: run the crypto bot for real (paper).
- `python trading_bot.py --dry-run`: the same for the stock bot.

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
- The internet dropped for a few minutes. Once it was back, pushed the log to GitHub and checked the account:
  crypto ACTIVE, 36 tradable USD pairs, MU at $884.74.
- User's decisions: the bot trades crypto automatically; **stop the stock bot**; $500 per buy; keep the 20/50
  moving average strategy as is. More strategies will come later, each discussed before it's added.
- Built `crypto_bot.py` and `crypto_config.toml`, using Alpaca's crypto data rather than yfinance (Alpaca's
  pair names match trading, while Yahoo uses odd codes for some coins). Found that Alpaca's daily crypto candles
  start at 00:00 UTC and that the unfinished current-day candle is included, so the bot drops it. Moved
  `setup_logging` into `trading_bot.py` so both bots share it.
- Tests: crypto dry run on a test list of BTC/USD, ETH/USD, BONK/USD and a fake pair (all "no signal"; the fake
  pair failed on its own; duplicates and lowercase cleaned up). Against a fake Alpaca client: a buy sends
  $500 notional GTC, a sell sends the exact held quantity, a sell with nothing held is skipped, and a duplicate
  is skipped. The stock bot still dry-runs fine.
- Added the `crypto-bot.yml` workflow (daily 00:15 UTC). Removed the stock workflow's schedule (manual only
  now). Disabled the PC task. The crypto watchlist is left empty for the user to fill in.

### 2026-11-01: Alpaca MCP "disconnected" in the chat session
- The user reported the Alpaca connection as disconnected. Checks: internet fine; `.env` keys log in
  (YUU8 ACTIVE); `claude mcp list` (a fresh server process) reports Connected with the YUU8 keys. But in the
  long-running chat session, which started 2026-10-11, the Alpaca tools returned **401 Unauthorized**.
- Cause: the session still passes the MCP keys it started with, which are the old DUM9 keys. That account was
  deleted on 2026-10-14, so those keys now return 401. The saved config (`~/.claude.json`) already has the YUU8
  keys. Fix: start a new Claude session. The bots use `.env` and GitHub secrets, so they were never affected.
- Follow-up: after the user reconnected the server inside the same session, it still got 401, so reconnecting
  doesn't pick up the new keys. Verified with a fresh server process started from the saved config: its keys
  match `.env` exactly and `get_account_info` succeeds. Only a new session fixes the old one.

### 2026-11-01: Strategy research (Satoshi Nakamoto, James Fickel, James Wynn)
- The user asked Claude to think like a crypto expert and study these three. Claude agreed to study them but
  won't claim to be real people. Summary, from public reporting (figures vary between sources):
  - **Satoshi:** builder, not trader. An estimated ~1.1M BTC mined in 2009–10 (Lerner's "Patoshi" pattern),
    believed never moved. The "strategy" is fixed rules (21M cap, halvings) and extreme long-term holding.
  - **Fickel:** early ETH buyer (reportedly about $400k near $0.80), founder of Amaranth Foundation (longevity).
    In 2024 he went long ETH/BTC on Aave by borrowing ~3,061 WBTC and swapping it for ETH, betting against the
    ratio's downtrend. Closed Dec 2024 with a reported ~20,600 ETH (~$69M) loss.
  - **Wynn:** high-leverage momentum trader. Memecoins (PEPE), then 40x BTC perps on Hyperliquid, peaking at a
    ~$1.25B notional long and reportedly ~$82M profit in 2025. Lost ~$100M in May 2025. In 2026 he flipped
    to 40x shorts and was liquidated repeatedly (six times in two weeks in April, account down to ~$900; again
    in June and September).
- Constraint: Alpaca crypto is spot only, with no leverage and no shorting, so Wynn-style perps and
  Fickel-style borrowing can't be copied here.
- Candidate strategies to discuss with the user (none added): (a) Satoshi-style accumulation / dollar-cost
  averaging; (b) a ratio trend, such as holding whichever of ETH/BTC is winning on a ratio moving average,
  following the trend Fickel fought; (c) momentum breakouts with hard stops and no leverage; (d) a risk layer
  for every strategy: max size per coin, stop-losses, max daily loss. Backtest each before going live.

### 2026-11-01: New scope (altcoins, memecoins, new projects; spot and futures) and the analysis plan
- User decision: no BTC/ETH. Trade other coins, new projects and memecoins, both spot and futures, paper only.
- Venue findings: Alpaca's broker has no crypto futures or perpetuals; it is spot only, and its lineup grew in May
  2026. Futures paper options to verify, including access from Pakistan: Bybit testnet/demo, OKX demo trading
  (simulated API), Hyperliquid testnet (perps, API supported) and Binance futures testnet. Alternatively, a
  simulated paper ledger on real market data, covering any perp market and DEX-only new tokens, with leverage,
  funding and liquidation modelled. New DEX tokens aren't on any exchange's paper system, so they need the
  simulated ledger either way.
- Analysis plan proposed to the user. Pipeline: universe screen → safety gate (rug checks) → multi-factor
  scoring (price/volume, liquidity, on-chain holders, derivatives funding/OI, social, fundamentals) → market
  regime filter (BTC trend and dominance, Fear & Greed, macro calendar) → strategy signal → risk sizing
  (leverage cap) → execution → log. Sources: CoinGecko/CMC, DexScreener/GeckoTerminal/Birdeye, exchange APIs
  via ccxt, Coinglass, Hyperliquid info API, block explorers and Helius, GoPlus/RugCheck/Honeypot.is/Bubblemaps,
  Arkham/Nansen/Dune, DeFiLlama/Tokenomist/CryptoRank/GitHub, CryptoPanic/LunarCrush/Santiment/X/Telegram,
  Alternative.me Fear & Greed, FRED and the economic calendar, Farside ETF flows. Free sources first.
