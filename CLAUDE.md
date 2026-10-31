# SpikeAI

Alpaca paper trading project: a moving average crossover bot that runs on GitHub Actions, with a backup scheduled
task on this PC. Crypto paper trading is next.

## Project memory: PROJECT_LOG.md

- **At the start of every session, read `PROJECT_LOG.md` before doing anything.** It holds the current state,
  key facts and the full history, so work continues from where it left off instead of starting from scratch.
- **After every significant action**, add a dated entry under *History* and update *Current state*. That
  includes trades, code or config changes, automation changes, decisions and findings. Commit the log together
  with the related change and push it. Run `git pull --rebase` first, because GitHub commits a bot log every
  weekday.
- Never write API keys, secrets or passwords into `PROJECT_LOG.md`, `CLAUDE.md` or any committed file. Keys
  live in `.env` (git-ignored) and in GitHub repository secrets.

## Ground rules

- Paper trading only. Keep the paper endpoint pinned (`TradingClient(..., paper=True)`).
- Don't recommend which stocks or coins to buy. The user picks; Claude can scan, backtest or run the user's own
  strategy on the user's list.
- The user is in Pakistan (PKT, UTC+5). Give times in both ET and PKT.
