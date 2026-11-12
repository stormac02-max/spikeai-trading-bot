# SpikeAI paper trading

_Updated **Thu 12 Nov 2026, 12:17 PKT** (Thu 02:17 ET). Refreshed after every daily run. Paper trading only: no real money._

## Strategy test: MA crossover vs breakout vs momentum

**45 days left** in the evaluation (until 2026-12-27), then the best strategy is kept.  
Each simulated account started with $10,000. Futures: 2x, long and short, $500 margin per trade. Spot: 1x, buy-only, $500 per buy, copied to Alpaca for coins it lists. Both use an 8% stop.

### Futures

| Strategy | Value | Return | Below peak | Open | Closed (won) | Fees | Funding |
|---|--:|--:|--:|--:|--:|--:|--:|
| 🔵 MA crossover 20/50 | **$10,463.55** | +4.64% | −0.02% | 4 | 0 | $1.80 | +$1.56 |
| 🟠 Breakout 20/10 | **$10,586.46** | +5.86% | −0.05% | 11 | 3 (0) | $7.73 | +$6.87 |
| 🟢 Momentum 14d, 5 long/5 short | **$10,001.82** | +0.02% | −2.85% | 6 | 11 (3) | $12.24 | −$0.48 |

**Futures leader:** 🟠 Breakout 20/10, $122.91 ahead of MA crossover 20/50.

### Spot

| Strategy | Value | Return | Below peak | Held | Closed (won) | Fees | On Alpaca |
|---|--:|--:|--:|--:|--:|--:|--:|
| 🔵 MA crossover 20/50 | **$10,000.00** | 0.00% | at peak | 0 | 0 | $0.00 | 0 |
| 🟠 Breakout 20/10 | **$10,000.00** | 0.00% | at peak | 0 | 0 | $0.00 | 0 |
| 🟢 Momentum 14d, 5 long/5 short | **$9,639.79** | −3.60% | −3.60% | 1 | 8 (0) | $20.43 | 0 |

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
| now | $10,463.55 | $10,586.46 | $10,001.82 | $10,000.00 | $10,000.00 | $9,639.79 |

</details>

### Open positions

| Strategy | Coin | Side | Entry → now | Profit | To stop | To liquidation / Alpaca |
|---|---|---|---|--:|--:|--:|
| 🔵 MA | **SUI** | ▼ Short | 0.89681 → 0.814 | +$92.34 (+18.4%) | ✅ 19.0% | ✅ 57.6% |
| 🔵 MA | **WLD** | ▼ Short | 0.38553 → 0.307 | +$203.69 (+40.9%) | ✅ 35.6% | ✅ 79.1% |
| 🔵 MA | **NEAR** | ▼ Short | 4.0459 → 3.5218 | +$129.54 (+25.8%) | ✅ 24.1% | ✅ 64.3% |
| 🔵 MA | **ZRO** | ▼ Short | 1.6048 → 1.5435 | +$38.21 (+7.6%) | ✅ 12.3% | ✅ 41.9% |
| 🟠 Breakout | **SOL** | ▼ Short | 91.244 → 82.773 | +$92.84 (+18.5%) | ✅ 19.1% | ✅ 61.4% |
| 🟠 Breakout | **XPL** | ▼ Short | 0.062812 → 0.05104 | +$187.41 (+37.3%) | ✅ 32.9% | ✅ 76.0% |
| 🟠 Breakout | **NEAR** | ▼ Short | 3.6822 → 3.5218 | +$43.56 (+8.7%) | ✅ 12.9% | ✅ 49.5% |
| 🟠 Breakout | **ENA** | ▼ Short | 0.1646 → 0.1428 | +$132.45 (+26.4%) | ✅ 24.5% | ✅ 64.8% |
| 🟠 Breakout | **WLD** | ▼ Short | 0.34441 → 0.307 | +$108.63 (+21.8%) | ✅ 21.2% | ✅ 60.1% |
| 🟠 Breakout | **XRP** | ▼ Short | 1.1619 → 1.0435 | +$101.86 (+20.4%) | ✅ 20.2% | ✅ 63.0% |
| 🟠 Breakout | **PUMP** | ▼ Short | 0.003674 → 0.003437 | +$64.51 (+12.9%) | ✅ 15.4% | ✅ 52.8% |
| 🟠 Breakout | **SUI** | ▼ Short | 0.81988 → 0.814 | +$7.18 (+1.4%) | ✅ 8.8% | ✅ 43.9% |
| 🟠 Breakout | **HYPE** | ▼ Short | 71.8649 → 71.106 | +$10.56 (+2.1%) | ✅ 9.2% | ✅ 44.4% |
| 🟠 Breakout | **ZEC** | ▼ Short | 1,003.70 → 986.48 | +$17.16 (+3.4%) | ✅ 9.9% | ✅ 45.4% |
| 🟠 Breakout | **UNI** | ▼ Short | 6.1326 → 6.1355 | −$0.47 (−0.1%) | ✅ 7.9% | ✅ 42.8% |
| 🟢 Momentum | **WLD** | ▼ Short | 0.38553 → 0.307 | +$203.69 (+40.9%) | ✅ 35.6% | ✅ 79.1% |
| 🟢 Momentum | **NEAR** | ▼ Short | 4.202 → 3.5218 | +$161.87 (+32.3%) | ✅ 28.9% | ✅ 70.7% |
| 🟢 Momentum | **HYPE** | ▲ Long | 74.024 → 71.106 | −$39.42 (−7.9%) | ⚠️ 4.2% | ✅ 45.1% |
| 🟢 Momentum | **TRUMP** | ▼ Short | 1.1454 → 1.1171 | +$24.68 (+4.9%) | ✅ 10.7% | ✅ 46.5% |
| 🟢 Momentum | **XPL** | ▼ Short | 0.051503 → 0.05104 | +$8.98 (+1.8%) | ✅ 9.0% | ✅ 44.2% |
| 🟢 Momentum | **ENA** | ▼ Short | 0.14951 → 0.1428 | +$44.91 (+9.0%) | ✅ 13.1% | ✅ 49.7% |
| 🟢 Momentum (spot) | **HYPE** | ▲ Long | 74.1398 → 71.08 | −$23.03 (−4.6%) | ⚠️ 4.0% | 🔴 copy failed |

_Distance = how far the price can still move against the position. ✅ over 5% · ⚠️ 2–5% · 🔴 under 2%. Spot can't be liquidated; its last column shows whether the trade is copied to Alpaca._

### Recent trades

| Time (PKT) | Strategy | Coin | What | Price | Result |
|---|---|---|---|--:|--:|
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
| Tue 10 Nov, 15:00 | 🟢 Momentum | **XMR** | Stopped out | 546.31 | −$82.08 |
| Tue 10 Nov, 15:00 | 🟢 Momentum (spot) | **XMR** | Stopped out | 545.98 | −$42.30 |
| Mon 09 Nov, 11:40 | 🟢 Momentum (spot) | **UNI** | Bought | 6.7758 | fee $1.25 |
| Mon 09 Nov, 11:40 | 🟢 Momentum (spot) | **ZEC** | Bought | 1,222.38 | fee $1.25 |

### Signal board (daily candle of 2026-11-11)

What each strategy sees per coin. 🔔 = the condition for a trade is met.

| Coin | MA: 20d vs 50d | Breakout: vs 20-day range | Momentum: 14d return |
|---|---|---|---|
| **HYPE** | below (−4.1%) | +34.8% to high / −2.5% to low | −10.6% (#7) |
| **ZEC** | below (−4.7%) | 🔔 below 20d low | −26.5% (#16) 🔔 bottom 5: short |
| **SOL** | below (−10.7%) | +29.1% to high / −2.4% to low | −18.7% (#11) |
| **NEAR** | below (−11.7%) | +48.8% to high / −3.9% to low | −24.3% (#15) |
| **XRP** | below (−8.8%) | +30.2% to high / −2.0% to low | −20.6% (#13) |
| **XMR** | above (+4.6%) | +13.8% to high / −7.3% to low | −2.9% (#2) 🔔 top 5: long |
| **PUMP** | below (−14.3%) | +50.4% to high / −3.6% to low | −23.6% (#14) |
| **LIT** | below (−10.7%) | +20.3% to high / −21.2% to low | +10.8% (#1) 🔔 top 5: long |
| **kPEPE** | above (+7.6%) | +26.2% to high / −7.0% to low | −10.1% (#4) 🔔 top 5: long |
| **WLD** | below (−17.7%) | +92.3% to high / −1.4% to low | −29.9% (#17) 🔔 bottom 5: short |
| **ENA** | below (−13.5%) | +49.8% to high / −0.8% to low | −30.6% (#18) 🔔 bottom 5: short |
| **UNI** | below (−9.3%) | 🔔 below 20d low | −14.1% (#10) |
| **TRUMP** | below (−16.5%) | +65.6% to high / −2.6% to low | −35.0% (#20) 🔔 bottom 5: short |
| **XPL** | below (−17.6%) | +67.2% to high / −3.3% to low | −32.8% (#19) 🔔 bottom 5: short |
| **BNB** | below (−3.6%) | +12.2% to high / −1.4% to low | −10.6% (#6) |
| **SUI** | below (−12.3%) | +26.1% to high / −2.5% to low | −12.9% (#8) |
| **AAVE** | below (−12.3%) | +29.4% to high / −4.5% to low | −10.1% (#5) 🔔 top 5: long |
| **ZRO** | below (−6.8%) | +28.7% to high / −8.0% to low | −9.2% (#3) 🔔 top 5: long |
| **LINK** | below (−10.3%) | +23.8% to high / −1.0% to low | −13.8% (#9) |
| **VVV** | below (−8.8%) | +44.1% to high / −7.1% to low | −18.8% (#12) |

_Momentum trades its top/bottom 5 at the Monday rebalance; MA and breakout act at each daily run. Spot uses the same signals but only buys: a short signal just sells what it holds._

### This week's coins (chosen 2026-11-09)

HYPE · ZEC · SOL · NEAR · XRP · XMR · PUMP · LIT · kPEPE · WLD · ENA · UNI · TRUMP · XPL · BNB · SUI · AAVE · ZRO · LINK · VVV

_The 20 most-traded Hyperliquid futures over the past week, excluding BTC and ETH. Refreshed Mondays 00:00 UTC (5:00 AM PKT)._

## Alpaca paper account

Value **$49,597.16** · cash $47,004.76 · account ending YUU8  
Holding: 2 MU (−$308.46), 7e-09 PEPEUSD ($0.00)

**0** simulated spot trade(s) copied and open · 🔴 1 copy error(s): see the spot log. Copies use the same number of coins as the simulation, with a real stop order on Alpaca.

Crypto spot bot: no coins on its watchlist yet (daily 00:15 UTC). Stock bot: stopped.

---
✅ Last run OK · [futures log](logs/futures_bot.log) · [spot log](logs/spot_bot.log) · [project log](PROJECT_LOG.md) · on the PC: `python dashboard.py`

<sub>This page is written by summary.py; edits by hand are overwritten.</sub>
