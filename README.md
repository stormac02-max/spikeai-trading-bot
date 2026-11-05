# SpikeAI paper trading

_Updated **Thu 05 Nov 2026, 11:52 PKT** (Thu 01:52 ET). Refreshed after every daily run. Paper trading only: no real money._

## Strategy test: MA crossover vs breakout vs momentum

**52 days left** in the evaluation (until 2026-12-27), then the best strategy is kept.  
Each simulated account started with $10,000. Futures: 2x, long and short, $500 margin per trade. Spot: 1x, buy-only, $500 per buy, copied to Alpaca for coins it lists. Both use an 8% stop.

### Futures

| Strategy | Value | Return | Below peak | Open | Closed (won) | Fees | Funding |
|---|--:|--:|--:|--:|--:|--:|--:|
| 🔵 MA crossover 20/50 | **$9,986.31** | −0.14% | −1.10% | 3 | 0 | $1.35 | +$1.50 |
| 🟠 Breakout 20/10 | **$9,791.15** | −2.09% | −2.09% | 3 | 1 (0) | $2.29 | +$2.01 |
| 🟢 Momentum 14d, 5 long/5 short | **$9,920.80** | −0.79% | −1.06% | 8 | 2 (0) | $5.33 | +$0.48 |

**Futures leader:** 🔵 MA crossover 20/50, $65.51 ahead of Momentum 14d, 5 long/5 short.

### Spot

| Strategy | Value | Return | Below peak | Held | Closed (won) | Fees | On Alpaca |
|---|--:|--:|--:|--:|--:|--:|--:|
| 🔵 MA crossover 20/50 | **$10,000.00** | 0.00% | at peak | 0 | 0 | $0.00 | 0 |
| 🟠 Breakout 20/10 | **$10,000.00** | 0.00% | at peak | 0 | 0 | $0.00 | 0 |
| 🟢 Momentum 14d, 5 long/5 short | **$9,861.45** | −1.39% | −1.39% | 2 | 3 (0) | $9.69 | 1 |

_Spot: no clear leader yet._

![Account value over time: solid = futures, dashed = spot](reports/equity.svg)

_Solid lines = futures, dashed = spot._

<details><summary>Account values as a table</summary>

| Date | MA | Breakout | Momentum | MA (spot) | Breakout (spot) | Momentum (spot) |
|---|--:|--:|--:|--:|--:|--:|
| 2026-10-30 | $9,999.54 | $10,000.00 | $10,000.00 | – | – | – |
| 2026-10-31 | $9,988.39 | $9,999.78 | $10,000.00 | $10,000.00 | $10,000.00 | $10,000.00 |
| 2026-11-01 | $10,001.28 | $9,989.21 | $9,994.61 | $10,000.00 | $10,000.00 | $9,992.51 |
| 2026-11-02 | $10,096.92 | $9,967.06 | $10,026.63 | $10,000.00 | $10,000.00 | $9,853.76 |
| 2026-11-03 | $10,000.52 | $9,881.85 | $9,970.65 | $10,000.00 | $10,000.00 | $9,867.56 |
| 2026-11-04 | $9,986.04 | $9,792.20 | $9,920.22 | $10,000.00 | $10,000.00 | $9,861.45 |
| now | $9,986.31 | $9,791.15 | $9,920.80 | $10,000.00 | $10,000.00 | $9,861.45 |

</details>

### Open positions

| Strategy | Coin | Side | Entry → now | Profit | To stop | To liquidation / Alpaca |
|---|---|---|---|--:|--:|--:|
| 🔵 MA | **SUI** | ▼ Short | 0.89681 → 0.92712 | −$33.80 (−6.7%) | ⚠️ 4.5% | ✅ 38.3% |
| 🔵 MA | **WLD** | ▼ Short | 0.38553 → 0.37796 | +$19.64 (+3.9%) | ✅ 10.2% | ✅ 45.7% |
| 🔵 MA | **NEAR** | ▼ Short | 4.0459 → 4.0446 | +$0.32 (+0.1%) | ✅ 8.0% | ✅ 42.9% |
| 🟠 Breakout | **TRX** | ▼ Short | 0.31088 → 0.31854 | −$24.64 (−4.9%) | ✅ 5.4% | ✅ 39.5% |
| 🟠 Breakout | **SOL** | ▼ Short | 91.244 → 96.2981 | −$55.39 (−11.1%) | ⚠️ 2.3% | ✅ 38.7% |
| 🟠 Breakout | **XPL** | ▼ Short | 0.062812 → 0.065861 | −$48.54 (−9.7%) | ⚠️ 3.0% | ✅ 36.3% |
| 🟢 Momentum | **LIT** | ▲ Long | 3.1789 → 3.4916 | +$98.37 (+19.7%) | ✅ 16.2% | ✅ 49.4% |
| 🟢 Momentum | **HYPE** | ▲ Long | 87.476 → 83.433 | −$46.22 (−9.3%) | ⚠️ 3.5% | ✅ 44.7% |
| 🟢 Momentum | **kPEPE** | ▲ Long | 0.004845 → 0.00498 | +$27.86 (+5.6%) | ✅ 10.5% | ✅ 48.7% |
| 🟢 Momentum | **WLD** | ▼ Short | 0.38553 → 0.37796 | +$19.64 (+3.9%) | ✅ 10.2% | ✅ 45.7% |
| 🟢 Momentum | **NEAR** | ▼ Short | 4.202 → 4.0446 | +$37.46 (+7.5%) | ✅ 12.2% | ✅ 48.5% |
| 🟢 Momentum | **AAVE** | ▼ Short | 133.43 → 132.98 | +$3.37 (+0.7%) | ✅ 8.4% | ✅ 43.4% |
| 🟢 Momentum | **SUI** | ▼ Short | 0.89362 → 0.92712 | −$37.49 (−7.5%) | ⚠️ 4.1% | ✅ 37.8% |
| 🟢 Momentum | **SOL** | ▼ Short | 94.657 → 96.2981 | −$17.34 (−3.5%) | ✅ 6.2% | ✅ 43.9% |
| 🟢 Momentum (spot) | **HYPE** | ▲ Long | 87.41 → 83.45 | −$25.04 (−5.0%) | ⚠️ 3.6% | 🔴 copy failed |
| 🟢 Momentum (spot) | **PEPE** | ▲ Long | 0.0000048436 → 0.000004974 | +$10.90 (+2.2%) | ✅ 10.4% | ✅ copied |

_Distance = how far the price can still move against the position. ✅ over 5% · ⚠️ 2–5% · 🔴 under 2%. Spot can't be liquidated; its last column shows whether the trade is copied to Alpaca._

### Recent trades

| Time (PKT) | Strategy | Coin | What | Price | Result |
|---|---|---|---|--:|--:|
| Thu 05 Nov, 11:52 | 🔵 MA | **NEAR** | Opened short | 4.0459 | fee $0.45 |
| Wed 04 Nov, 13:00 | 🟠 Breakout | **NEAR** | Stopped out | 4.0584 | −$80.15 |
| Tue 03 Nov, 17:00 | 🟢 Momentum (spot) | **LIT** | Stopped out | 0.090796 | −$42.30 |
| Tue 03 Nov, 13:00 | 🟢 Momentum | **VVV** | Stopped out | 20.9547 | −$80.71 |
| Tue 03 Nov, 13:00 | 🟢 Momentum (spot) | **VVV** | Stopped out | 20.9148 | −$42.30 |
| Tue 03 Nov, 11:52 | 🟠 Breakout | **SOL** | Opened short | 91.244 | fee $0.45 |
| Tue 03 Nov, 11:52 | 🟠 Breakout | **NEAR** | Opened short | 3.7578 | fee $0.45 |
| Tue 03 Nov, 11:52 | 🟠 Breakout | **XPL** | Opened short | 0.062812 | fee $0.45 |
| Mon 02 Nov, 22:00 | 🟢 Momentum | **ZEC** | Stopped out | 1,170.33 | −$80.54 |
| Mon 02 Nov, 22:00 | 🟢 Momentum (spot) | **ZEC** | Stopped out | 1,168.52 | −$42.30 |
| Mon 02 Nov, 11:13 | 🟢 Momentum (spot) | **PEPE** | Bought | 0.0000048436 | fee $1.25 |
| Mon 02 Nov, 11:12 | 🔵 MA | **WLD** | Opened short | 0.38553 | fee $0.45 |
| Mon 02 Nov, 11:12 | 🟢 Momentum | **VVV** | Opened long | 22.7768 | fee $0.45 |
| Mon 02 Nov, 11:12 | 🟢 Momentum | **LIT** | Opened long | 3.1789 | fee $0.45 |
| Mon 02 Nov, 11:12 | 🟢 Momentum | **ZEC** | Opened long | 1,272.10 | fee $0.45 |

### Signal board (daily candle of 2026-11-04)

What each strategy sees per coin. 🔔 = the condition for a trade is met.

| Coin | MA: 20d vs 50d | Breakout: vs 20-day range | Momentum: 14d return |
|---|---|---|---|
| **HYPE** | below (−4.9%) | +15.9% to high / −11.2% to low | +4.0% (#2) 🔔 top 5: long |
| **ZEC** | below (−7.5%) | +7.9% to high / −19.2% to low | −1.4% (#5) 🔔 top 5: long |
| **SOL** | below (−7.6%) | +14.3% to high / −5.0% to low | −10.6% (#12) |
| **NEAR** | below (−1.7%) 🔔 crossed down | +36.2% to high / −6.7% to low | −23.8% (#19) 🔔 bottom 5: short |
| **kPEPE** | above (+4.8%) | +15.0% to high / −24.3% to low | +7.1% (#1) 🔔 top 5: long |
| **ENA** | below (−8.6%) | +25.0% to high / −8.8% to low | −15.4% (#15) |
| **XRP** | below (−6.6%) | +7.2% to high / −8.0% to low | −4.4% (#8) |
| **BNB** | below (−3.0%) | +5.9% to high / −6.9% to low | −3.5% (#7) |
| **PUMP** | below (−8.9%) | +23.1% to high / −11.4% to low | −17.2% (#16) 🔔 bottom 5: short |
| **XMR** | above (+5.7%) | +2.9% to high / −18.0% to low | +3.3% (#3) 🔔 top 5: long |
| **LIT** | below (−15.8%) | +20.2% to high / −22.6% to low | −11.9% (#13) |
| **UNI** | below (−10.1%) | +2.1% to high / −18.1% to low | +2.3% (#4) 🔔 top 5: long |
| **WLD** | below (−4.7%) | +59.6% to high / −3.8% to low | −35.8% (#20) 🔔 bottom 5: short |
| **XPL** | below (−12.6%) | +38.7% to high / −2.6% to low | −22.2% (#18) 🔔 bottom 5: short |
| **ZRO** | above (+3.5%) | +25.2% to high / −22.2% to low | −6.4% (#9) |
| **SUI** | below (−7.0%) | +14.2% to high / −10.9% to low | −9.7% (#11) |
| **TRX** | below (−1.3%) | +14.1% to high / −6.0% to low | −3.3% (#6) |
| **AAVE** | below (−7.4%) | +25.9% to high / −12.6% to low | −14.9% (#14) |
| **LINK** | below (−7.5%) | +12.0% to high / −10.2% to low | −8.5% (#10) |
| **VVV** | below (−7.2%) | +31.8% to high / −5.0% to low | −20.2% (#17) 🔔 bottom 5: short |

_Momentum trades its top/bottom 5 at the Monday rebalance; MA and breakout act at each daily run. Spot uses the same signals but only buys: a short signal just sells what it holds._

### This week's coins (chosen 2026-11-02)

HYPE · ZEC · SOL · NEAR · kPEPE · ENA · XRP · BNB · PUMP · XMR · LIT · UNI · WLD · XPL · ZRO · SUI · TRX · AAVE · LINK · VVV

_The 20 most-traded Hyperliquid futures over the past week, excluding BTC and ETH. Refreshed Mondays 00:00 UTC (5:00 AM PKT)._

## Alpaca paper account

Value **$49,686.92** · cash $47,108.92 · account ending YUU8  
Holding: 2 MU (−$325.86), 1.02972e+08 PEPEUSD (+$14.21)

**1** simulated spot trade(s) copied and open · 🔴 1 copy error(s): see the spot log. Copies use the same number of coins as the simulation, with a real stop order on Alpaca.

Crypto spot bot: no coins on its watchlist yet (daily 00:15 UTC). Stock bot: stopped.

---
✅ Last run OK · [futures log](logs/futures_bot.log) · [spot log](logs/spot_bot.log) · [project log](PROJECT_LOG.md) · on the PC: `python dashboard.py`

<sub>This page is written by summary.py; edits by hand are overwritten.</sub>
