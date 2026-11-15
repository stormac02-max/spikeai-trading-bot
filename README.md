# SpikeAI paper trading

_Updated **Sun 15 Nov 2026, 11:38 PKT** (Sun 01:38 ET). Refreshed after every daily run. Paper trading only: no real money._

## Strategy test: MA crossover vs breakout vs momentum

**42 days left** in the evaluation (until 2026-12-27), then the best strategy is kept.  
Each simulated account started with $10,000. Futures: 2x, long and short, $500 margin per trade. Spot: 1x, buy-only, $500 per buy, copied to Alpaca for coins it lists. Both use an 8% stop.

### Futures

| Strategy | Value | Return | Below peak | Open | Closed (won) | Fees | Funding |
|---|--:|--:|--:|--:|--:|--:|--:|
| 🔵 MA crossover 20/50 | **$10,841.87** | +8.42% | −0.01% | 4 | 0 | $1.80 | +$0.88 |
| 🟠 Breakout 20/10 | **$12,027.23** | +20.27% | −0.03% | 19 | 3 (0) | $11.33 | +$7.10 |
| 🟢 Momentum 14d, 5 long/5 short | **$10,628.66** | +6.29% | −0.01% | 5 | 12 (3) | $12.66 | −$3.40 |

**Futures leader:** 🟠 Breakout 20/10, $1,185.36 ahead of MA crossover 20/50.

### Spot

| Strategy | Value | Return | Below peak | Held | Closed (won) | Fees | On Alpaca |
|---|--:|--:|--:|--:|--:|--:|--:|
| 🔵 MA crossover 20/50 | **$10,000.00** | 0.00% | at peak | 0 | 0 | $0.00 | 0 |
| 🟠 Breakout 20/10 | **$10,000.00** | 0.00% | at peak | 0 | 0 | $0.00 | 0 |
| 🟢 Momentum 14d, 5 long/5 short | **$9,619.33** | −3.81% | −3.81% | 0 | 9 (0) | $21.57 | 0 |

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
| 2026-11-05 | $10,238.48 | $9,996.69 | $10,194.43 | $10,000.00 | $10,000.00 | $9,837.02 |
| 2026-11-06 | $10,220.57 | $9,970.30 | $10,178.96 | $10,000.00 | $10,000.00 | $9,837.64 |
| 2026-11-07 | $10,276.98 | $10,108.40 | $10,188.26 | $10,000.00 | $10,000.00 | $9,834.86 |
| 2026-11-08 | $10,442.05 | $10,440.36 | $10,294.79 | $10,000.00 | $10,000.00 | $9,844.28 |
| 2026-11-09 | $10,397.12 | $10,331.10 | $10,239.06 | $10,000.00 | $10,000.00 | $9,837.31 |
| 2026-11-10 | $10,416.71 | $10,474.48 | $10,101.45 | $10,000.00 | $10,000.00 | $9,752.48 |
| 2026-11-11 | $10,465.16 | $10,591.82 | $10,003.86 | $10,000.00 | $10,000.00 | $9,639.79 |
| 2026-11-12 | $10,502.65 | $10,863.61 | $10,142.84 | $10,000.00 | $10,000.00 | $9,643.96 |
| 2026-11-13 | $10,569.20 | $11,143.10 | $10,203.16 | $10,000.00 | $10,000.00 | $9,619.33 |
| 2026-11-14 | $10,842.64 | $12,031.38 | $10,629.43 | $10,000.00 | $10,000.00 | $9,619.33 |
| now | $10,841.87 | $12,027.23 | $10,628.66 | $10,000.00 | $10,000.00 | $9,619.33 |

</details>

### Open positions

| Strategy | Coin | Side | Entry → now | Profit | To stop | To liquidation / Alpaca |
|---|---|---|---|--:|--:|--:|
| 🔵 MA | **SUI** | ▼ Short | 0.89681 → 0.71848 | +$198.85 (+39.6%) | ✅ 34.8% | ✅ 78.5% |
| 🔵 MA | **WLD** | ▼ Short | 0.38553 → 0.25977 | +$326.20 (+65.8%) | ✅ 60.3% | ✅ 111.4% |
| 🔵 MA | **NEAR** | ▼ Short | 4.0459 → 3.1348 | +$225.19 (+44.9%) | ✅ 39.4% | ✅ 84.6% |
| 🔵 MA | **ZRO** | ▼ Short | 1.6048 → 1.4563 | +$92.55 (+18.5%) | ✅ 19.0% | ✅ 50.4% |
| 🟠 Breakout | **SOL** | ▼ Short | 91.244 → 70.395 | +$228.50 (+45.6%) | ✅ 40.0% | ✅ 89.8% |
| 🟠 Breakout | **XPL** | ▼ Short | 0.062812 → 0.043906 | +$300.99 (+59.9%) | ✅ 54.5% | ✅ 104.7% |
| 🟠 Breakout | **NEAR** | ▼ Short | 3.6822 → 3.1348 | +$148.66 (+29.6%) | ✅ 26.9% | ✅ 68.0% |
| 🟠 Breakout | **ENA** | ▼ Short | 0.1646 → 0.11846 | +$280.31 (+55.9%) | ✅ 50.1% | ✅ 98.7% |
| 🟠 Breakout | **WLD** | ▼ Short | 0.34441 → 0.25977 | +$245.76 (+49.5%) | ✅ 43.2% | ✅ 89.0% |
| 🟠 Breakout | **XRP** | ▼ Short | 1.1619 → 0.95735 | +$176.05 (+35.2%) | ✅ 31.1% | ✅ 77.7% |
| 🟠 Breakout | **PUMP** | ▼ Short | 0.003674 → 0.002922 | +$204.68 (+40.9%) | ✅ 35.8% | ✅ 79.7% |
| 🟠 Breakout | **SUI** | ▼ Short | 0.81988 → 0.71848 | +$123.68 (+24.7%) | ✅ 23.2% | ✅ 63.0% |
| 🟠 Breakout | **HYPE** | ▼ Short | 71.8649 → 65.23 | +$92.32 (+18.4%) | ✅ 19.0% | ✅ 57.5% |
| 🟠 Breakout | **ZEC** | ▼ Short | 1,003.70 → 891.63 | +$111.66 (+22.3%) | ✅ 21.6% | ✅ 60.9% |
| 🟠 Breakout | **UNI** | ▼ Short | 6.1326 → 4.9993 | +$184.80 (+37.0%) | ✅ 32.5% | ✅ 75.2% |
| 🟠 Breakout | **BNB** | ▼ Short | 632.05 → 590.83 | +$65.22 (+13.0%) | ✅ 15.5% | ✅ 52.8% |
| 🟠 Breakout | **AAVE** | ▼ Short | 111.00 → 105.77 | +$47.15 (+9.4%) | ✅ 13.3% | ✅ 49.9% |
| 🟠 Breakout | **XMR** | ▼ Short | 490.83 → 491.01 | −$0.36 (−0.1%) | ✅ 8.0% | ✅ 36.3% |
| 🟠 Breakout | **kPEPE** | ▼ Short | 0.003924 → 0.003922 | +$0.51 (+0.1%) | ✅ 8.1% | ✅ 42.9% |
| 🟠 Breakout | **TRUMP** | ▼ Short | 0.93969 → 0.93974 | −$0.05 (−0.0%) | ✅ 8.0% | ✅ 42.8% |
| 🟠 Breakout | **ZRO** | ▼ Short | 1.4562 → 1.4563 | −$0.07 (−0.0%) | ✅ 8.0% | ✅ 36.4% |
| 🟠 Breakout | **LINK** | ▼ Short | 9.0847 → 9.0837 | +$0.11 (+0.0%) | ✅ 8.0% | ✅ 42.9% |
| 🟠 Breakout | **VVV** | ▼ Short | 19.445 → 19.4467 | −$0.09 (−0.0%) | ✅ 8.0% | ✅ 28.6% |
| 🟢 Momentum | **WLD** | ▼ Short | 0.38553 → 0.25977 | +$326.20 (+65.8%) | ✅ 60.3% | ✅ 111.4% |
| 🟢 Momentum | **NEAR** | ▼ Short | 4.202 → 3.1348 | +$253.97 (+50.6%) | ✅ 44.8% | ✅ 91.8% |
| 🟢 Momentum | **TRUMP** | ▼ Short | 1.1454 → 0.93974 | +$179.53 (+36.0%) | ✅ 31.6% | ✅ 73.9% |
| 🟢 Momentum | **XPL** | ▼ Short | 0.051503 → 0.043906 | +$147.50 (+29.4%) | ✅ 26.7% | ✅ 67.7% |
| 🟢 Momentum | **ENA** | ▼ Short | 0.14951 → 0.11846 | +$207.69 (+41.5%) | ✅ 36.3% | ✅ 80.4% |

_Distance = how far the price can still move against the position. ✅ over 5% · ⚠️ 2–5% · 🔴 under 2%. Spot can't be liquidated; its last column shows whether the trade is copied to Alpaca._

### Recent trades

| Time (PKT) | Strategy | Coin | What | Price | Result |
|---|---|---|---|--:|--:|
| Sun 15 Nov, 11:38 | 🟠 Breakout | **XMR** | Opened short | 490.83 | fee $0.45 |
| Sun 15 Nov, 11:38 | 🟠 Breakout | **kPEPE** | Opened short | 0.003924 | fee $0.45 |
| Sun 15 Nov, 11:38 | 🟠 Breakout | **TRUMP** | Opened short | 0.93969 | fee $0.45 |
| Sun 15 Nov, 11:38 | 🟠 Breakout | **ZRO** | Opened short | 1.4562 | fee $0.45 |
| Sun 15 Nov, 11:38 | 🟠 Breakout | **LINK** | Opened short | 9.0847 | fee $0.45 |
| Sun 15 Nov, 11:38 | 🟠 Breakout | **VVV** | Opened short | 19.445 | fee $0.45 |
| Sat 14 Nov, 08:00 | 🟢 Momentum | **HYPE** | Stopped out | 68.1021 | −$81.48 |
| Sat 14 Nov, 08:00 | 🟢 Momentum (spot) | **HYPE** | Stopped out | 68.2086 | −$42.30 |
| Fri 13 Nov, 11:49 | 🟠 Breakout | **BNB** | Opened short | 632.05 | fee $0.45 |
| Fri 13 Nov, 11:49 | 🟠 Breakout | **AAVE** | Opened short | 111.00 | fee $0.45 |
| Thu 12 Nov, 12:16 | 🟠 Breakout | **UNI** | Opened short | 6.1326 | fee $0.45 |
| Thu 12 Nov, 11:00 | 🟢 Momentum | **kPEPE** | Stopped out | 0.0044574 | −$81.03 |
| Thu 12 Nov, 11:00 | 🟢 Momentum (spot) | **PEPE** | Stopped out (Alpaca: stopped on Alpaca) | 0.0000044561 | −$42.30 |
| Thu 12 Nov, 04:00 | 🟢 Momentum | **UNI** | Stopped out | 6.2396 | −$81.07 |
| Thu 12 Nov, 04:00 | 🟢 Momentum (spot) | **UNI** | Stopped out (Alpaca: stopped on Alpaca) | 6.2337 | −$42.30 |

### Signal board (daily candle of 2026-11-14)

What each strategy sees per coin. 🔔 = the condition for a trade is met.

| Coin | MA: 20d vs 50d | Breakout: vs 20-day range | Momentum: 14d return |
|---|---|---|---|
| **HYPE** | below (−3.8%) | 🔔 below 20d low | −26.9% (#11) |
| **ZEC** | below (−5.3%) | 🔔 below 20d low | −31.0% (#14) |
| **SOL** | below (−12.2%) | 🔔 below 20d low | −26.4% (#10) |
| **NEAR** | below (−14.4%) | 🔔 below 20d low | −31.7% (#16) 🔔 bottom 5: short |
| **XRP** | below (−10.0%) | 🔔 below 20d low | −27.0% (#12) |
| **XMR** | above (+2.9%) | 🔔 below 20d low | −21.6% (#3) 🔔 top 5: long |
| **PUMP** | below (−16.7%) | 🔔 below 20d low | −30.7% (#13) |
| **LIT** | below (−7.9%) | +24.3% to high / −10.8% to low | −8.8% (#1) 🔔 top 5: long |
| **kPEPE** | above (+7.2%) | 🔔 below 20d low | −21.7% (#4) 🔔 top 5: long |
| **WLD** | below (−22.0%) | 🔔 below 20d low | −36.0% (#17) 🔔 bottom 5: short |
| **ENA** | below (−16.1%) | 🔔 below 20d low | −39.1% (#18) 🔔 bottom 5: short |
| **UNI** | below (−9.3%) | 🔔 below 20d low | −31.1% (#15) |
| **TRUMP** | below (−19.1%) | 🔔 below 20d low | −40.0% (#19) 🔔 bottom 5: short |
| **XPL** | below (−19.2%) | 🔔 below 20d low | −46.7% (#20) 🔔 bottom 5: short |
| **BNB** | below (−4.8%) | 🔔 below 20d low | −17.3% (#2) 🔔 top 5: long |
| **SUI** | below (−13.3%) | 🔔 below 20d low | −22.1% (#5) 🔔 top 5: long |
| **AAVE** | below (−14.0%) | 🔔 below 20d low | −24.7% (#8) |
| **ZRO** | below (−8.7%) | 🔔 below 20d low | −23.8% (#6) |
| **LINK** | below (−11.2%) | 🔔 below 20d low | −23.8% (#7) |
| **VVV** | below (−10.0%) | 🔔 below 20d low | −25.8% (#9) |

_Momentum trades its top/bottom 5 at the Monday rebalance; MA and breakout act at each daily run. Spot uses the same signals but only buys: a short signal just sells what it holds._

### This week's coins (chosen 2026-11-09)

HYPE · ZEC · SOL · NEAR · XRP · XMR · PUMP · LIT · kPEPE · WLD · ENA · UNI · TRUMP · XPL · BNB · SUI · AAVE · ZRO · LINK · VVV

_The 20 most-traded Hyperliquid futures over the past week, excluding BTC and ETH. Refreshed Mondays 00:00 UTC (5:00 AM PKT)._

## Alpaca paper account

Value **$49,583.38** · cash $47,004.76 · account ending YUU8  
Holding: 2 MU (−$322.24), 7e-09 PEPEUSD ($0.00)

**0** simulated spot trade(s) copied and open. Copies use the same number of coins as the simulation, with a real stop order on Alpaca.

Crypto spot bot: no coins on its watchlist yet (daily 00:15 UTC). Stock bot: stopped.

---
✅ Last run OK · [futures log](logs/futures_bot.log) · [spot log](logs/spot_bot.log) · [project log](PROJECT_LOG.md) · on the PC: `python dashboard.py`

<sub>This page is written by summary.py; edits by hand are overwritten.</sub>
