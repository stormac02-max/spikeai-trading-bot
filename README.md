# SpikeAI paper trading

_Updated **Sat 14 Nov 2026, 11:29 PKT** (Sat 01:29 ET). Refreshed after every daily run. Paper trading only: no real money._

## Strategy test: MA crossover vs breakout vs momentum

**43 days left** in the evaluation (until 2026-12-27), then the best strategy is kept.  
Each simulated account started with $10,000. Futures: 2x, long and short, $500 margin per trade. Spot: 1x, buy-only, $500 per buy, copied to Alpaca for coins it lists. Both use an 8% stop.

### Futures

| Strategy | Value | Return | Below peak | Open | Closed (won) | Fees | Funding |
|---|--:|--:|--:|--:|--:|--:|--:|
| 🔵 MA crossover 20/50 | **$10,569.92** | +5.70% | at peak | 4 | 0 | $1.80 | +$2.41 |
| 🟠 Breakout 20/10 | **$11,146.57** | +11.47% | at peak | 13 | 3 (0) | $8.63 | +$9.55 |
| 🟢 Momentum 14d, 5 long/5 short | **$10,203.67** | +2.04% | −0.89% | 5 | 12 (3) | $12.66 | −$0.58 |

**Futures leader:** 🟠 Breakout 20/10, $576.65 ahead of MA crossover 20/50.

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
| now | $10,569.92 | $11,146.57 | $10,203.67 | $10,000.00 | $10,000.00 | $9,619.33 |

</details>

### Open positions

| Strategy | Coin | Side | Entry → now | Profit | To stop | To liquidation / Alpaca |
|---|---|---|---|--:|--:|--:|
| 🔵 MA | **SUI** | ▼ Short | 0.89681 → 0.78292 | +$126.99 (+25.3%) | ✅ 23.7% | ✅ 63.9% |
| 🔵 MA | **WLD** | ▼ Short | 0.38553 → 0.28623 | +$257.57 (+51.8%) | ✅ 45.5% | ✅ 92.0% |
| 🔵 MA | **NEAR** | ▼ Short | 4.0459 → 3.3842 | +$163.55 (+32.6%) | ✅ 29.1% | ✅ 71.0% |
| 🔵 MA | **ZRO** | ▼ Short | 1.6048 → 1.5708 | +$21.20 (+4.2%) | ✅ 10.3% | ✅ 39.5% |
| 🟠 Breakout | **SOL** | ▼ Short | 91.244 → 75.694 | +$170.42 (+34.0%) | ✅ 30.2% | ✅ 76.5% |
| 🟠 Breakout | **XPL** | ▼ Short | 0.062812 → 0.049099 | +$218.32 (+43.5%) | ✅ 38.2% | ✅ 83.0% |
| 🟠 Breakout | **NEAR** | ▼ Short | 3.6822 → 3.3842 | +$80.93 (+16.1%) | ✅ 17.5% | ✅ 55.6% |
| 🟠 Breakout | **ENA** | ▼ Short | 0.1646 → 0.13104 | +$203.88 (+40.7%) | ✅ 35.7% | ✅ 79.6% |
| 🟠 Breakout | **WLD** | ▼ Short | 0.34441 → 0.28623 | +$168.94 (+33.9%) | ✅ 30.0% | ✅ 71.7% |
| 🟠 Breakout | **XRP** | ▼ Short | 1.1619 → 0.99734 | +$141.63 (+28.3%) | ✅ 25.8% | ✅ 70.6% |
| 🟠 Breakout | **PUMP** | ▼ Short | 0.003674 → 0.003432 | +$65.87 (+13.1%) | ✅ 15.6% | ✅ 53.1% |
| 🟠 Breakout | **SUI** | ▼ Short | 0.81988 → 0.78292 | +$45.08 (+9.0%) | ✅ 13.1% | ✅ 49.7% |
| 🟠 Breakout | **HYPE** | ▼ Short | 71.8649 → 69.635 | +$31.03 (+6.2%) | ✅ 11.5% | ✅ 47.5% |
| 🟠 Breakout | **ZEC** | ▼ Short | 1,003.70 → 922.61 | +$80.79 (+16.1%) | ✅ 17.5% | ✅ 55.5% |
| 🟠 Breakout | **UNI** | ▼ Short | 6.1326 → 5.6081 | +$85.53 (+17.1%) | ✅ 18.1% | ✅ 56.2% |
| 🟠 Breakout | **BNB** | ▼ Short | 632.05 → 620.36 | +$18.50 (+3.7%) | ✅ 10.0% | ✅ 45.6% |
| 🟠 Breakout | **AAVE** | ▼ Short | 111.00 → 109.55 | +$13.09 (+2.6%) | ✅ 9.4% | ✅ 44.7% |
| 🟢 Momentum | **WLD** | ▼ Short | 0.38553 → 0.28623 | +$257.57 (+51.8%) | ✅ 45.5% | ✅ 92.0% |
| 🟢 Momentum | **NEAR** | ▼ Short | 4.202 → 3.3842 | +$194.62 (+38.7%) | ✅ 34.1% | ✅ 77.7% |
| 🟢 Momentum | **TRUMP** | ▼ Short | 1.1454 → 1.0713 | +$64.67 (+12.9%) | ✅ 15.5% | ✅ 52.7% |
| 🟢 Momentum | **XPL** | ▼ Short | 0.051503 → 0.049099 | +$46.67 (+9.3%) | ✅ 13.3% | ✅ 50.0% |
| 🟢 Momentum | **ENA** | ▼ Short | 0.14951 → 0.13104 | +$123.55 (+24.7%) | ✅ 23.2% | ✅ 63.1% |

_Distance = how far the price can still move against the position. ✅ over 5% · ⚠️ 2–5% · 🔴 under 2%. Spot can't be liquidated; its last column shows whether the trade is copied to Alpaca._

### Recent trades

| Time (PKT) | Strategy | Coin | What | Price | Result |
|---|---|---|---|--:|--:|
| Sat 14 Nov, 08:00 | 🟢 Momentum | **HYPE** | Stopped out | 68.1021 | −$81.48 |
| Sat 14 Nov, 08:00 | 🟢 Momentum (spot) | **HYPE** | Stopped out | 68.2086 | −$42.30 |
| Fri 13 Nov, 11:49 | 🟠 Breakout | **BNB** | Opened short | 632.05 | fee $0.45 |
| Fri 13 Nov, 11:49 | 🟠 Breakout | **AAVE** | Opened short | 111.00 | fee $0.45 |
| Thu 12 Nov, 12:16 | 🟠 Breakout | **UNI** | Opened short | 6.1326 | fee $0.45 |
| Thu 12 Nov, 11:00 | 🟢 Momentum | **kPEPE** | Stopped out | 0.0044574 | −$81.03 |
| Thu 12 Nov, 11:00 | 🟢 Momentum (spot) | **PEPE** | Stopped out (Alpaca: stopped on Alpaca) | 0.0000044561 | −$42.30 |
| Thu 12 Nov, 04:00 | 🟢 Momentum | **UNI** | Stopped out | 6.2396 | −$81.07 |
| Thu 12 Nov, 04:00 | 🟢 Momentum (spot) | **UNI** | Stopped out (Alpaca: stopped on Alpaca) | 6.2337 | −$42.30 |
| Wed 11 Nov, 22:00 | 🟠 Breakout | **VVV** | Stopped out | 20.5203 | −$80.45 |
| Wed 11 Nov, 11:29 | 🟠 Breakout | **HYPE** | Opened short | 71.8649 | fee $0.45 |
| Wed 11 Nov, 11:29 | 🟠 Breakout | **ZEC** | Opened short | 1,003.70 | fee $0.45 |
| Wed 11 Nov, 11:29 | 🟠 Breakout | **VVV** | Opened short | 19.0003 | fee $0.45 |
| Tue 10 Nov, 20:00 | 🟢 Momentum | **ZEC** | Stopped out | 1,123.82 | −$80.79 |
| Tue 10 Nov, 20:00 | 🟢 Momentum (spot) | **ZEC** | Stopped out | 1,124.59 | −$42.30 |

### Signal board (daily candle of 2026-11-13)

What each strategy sees per coin. 🔔 = the condition for a trade is met.

| Coin | MA: 20d vs 50d | Breakout: vs 20-day range | Momentum: 14d return |
|---|---|---|---|
| **HYPE** | below (−3.7%) | +35.5% to high / −3.1% to low | −20.4% (#15) |
| **ZEC** | below (−4.9%) | +49.9% to high / −0.3% to low | −26.5% (#16) 🔔 bottom 5: short |
| **SOL** | below (−11.6%) | 🔔 below 20d low | −18.9% (#11) |
| **NEAR** | below (−13.4%) | +40.0% to high / −3.0% to low | −19.7% (#14) |
| **XRP** | below (−9.5%) | 🔔 below 20d low | −19.5% (#12) |
| **XMR** | above (+3.7%) | +24.7% to high / −0.0% to low | −10.2% (#3) 🔔 top 5: long |
| **PUMP** | below (−15.8%) | +35.3% to high / −4.5% to low | −17.5% (#10) |
| **LIT** | below (−8.5%) | +10.4% to high / −20.8% to low | +16.8% (#1) 🔔 top 5: long |
| **kPEPE** | above (+7.4%) | +29.6% to high / −4.5% to low | −10.4% (#4) 🔔 top 5: long |
| **WLD** | below (−20.7%) | 🔔 below 20d low | −27.5% (#17) 🔔 bottom 5: short |
| **ENA** | below (−15.2%) | 🔔 below 20d low | −29.2% (#18) 🔔 bottom 5: short |
| **UNI** | below (−9.1%) | 🔔 below 20d low | −19.6% (#13) |
| **TRUMP** | below (−18.2%) | +62.4% to high / −1.8% to low | −31.6% (#19) 🔔 bottom 5: short |
| **XPL** | below (−18.7%) | +72.1% to high / −4.4% to low | −38.4% (#20) 🔔 bottom 5: short |
| **BNB** | below (−4.2%) | 🔔 below 20d low | −10.5% (#5) 🔔 top 5: long |
| **SUI** | below (−13.1%) | +21.7% to high / −1.7% to low | −12.0% (#6) |
| **AAVE** | below (−13.5%) | +30.1% to high / −0.8% to low | −13.4% (#7) |
| **ZRO** | below (−7.9%) | +23.7% to high / −10.0% to low | −7.8% (#2) 🔔 top 5: long |
| **LINK** | below (−10.9%) | +21.9% to high / −0.9% to low | −13.9% (#8) |
| **VVV** | below (−9.4%) | +38.8% to high / −3.7% to low | −16.3% (#9) |

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
