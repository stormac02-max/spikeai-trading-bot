# SpikeAI paper trading

_Updated **Thu 26 Nov 2026, 13:25 PKT** (Thu 03:25 ET). Refreshed after every daily run. Paper trading only: no real money._

## Strategy test: MA crossover vs breakout vs momentum

**31 days left** in the evaluation (until 2026-12-27), then the best strategy is kept.  
Each simulated account started with $10,000. Futures: 2x, long and short, $500 margin per trade. Spot: 1x, buy-only, $500 per buy, copied to Alpaca for coins it lists. Both use an 8% stop.

### Futures

| Strategy | Value | Return | Below peak | Open | Closed (won) | Fees | Funding |
|---|--:|--:|--:|--:|--:|--:|--:|
| 🔵 MA crossover 20/50 | **$11,042.01** | +10.42% | −3.56% | 3 | 3 (1) | $4.01 | −$1.26 |
| 🟠 Breakout 20/10 | **$12,808.25** | +28.08% | −6.76% | 16 | 10 (2) | $16.28 | +$6.38 |
| 🟢 Momentum 14d, 5 long/5 short | **$10,894.26** | +8.94% | −1.00% | 5 | 20 (6) | $19.48 | −$11.32 |

**Futures leader:** 🟠 Breakout 20/10, $1,766.24 ahead of MA crossover 20/50.

### Spot

| Strategy | Value | Return | Below peak | Held | Closed (won) | Fees | On Alpaca |
|---|--:|--:|--:|--:|--:|--:|--:|
| 🔵 MA crossover 20/50 | **$10,000.00** | 0.00% | at peak | 0 | 0 | $0.00 | 0 |
| 🟠 Breakout 20/10 | **$10,041.11** | +0.41% | at peak | 1 | 0 | $1.25 | 0 |
| 🟢 Momentum 14d, 5 long/5 short | **$9,658.04** | −3.42% | −3.42% | 4 | 13 (0) | $36.16 | 2 |

**Spot leader:** 🟠 Breakout 20/10, $41.11 ahead of MA crossover 20/50.

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
| 2026-11-15 | $10,879.67 | $12,066.42 | $10,633.32 | $10,000.00 | $10,000.00 | $9,614.19 |
| 2026-11-16 | $10,754.52 | $11,659.55 | $10,585.62 | $10,000.00 | $10,000.00 | $9,678.18 |
| 2026-11-17 | $10,822.96 | $11,790.38 | $10,654.51 | $10,000.00 | $10,000.00 | $9,820.39 |
| 2026-11-18 | $10,770.65 | $11,796.49 | $10,712.06 | $10,000.00 | $10,000.00 | $9,874.21 |
| 2026-11-19 | $11,045.66 | $12,571.77 | $10,718.62 | $10,000.00 | $10,000.00 | $9,759.36 |
| 2026-11-20 | $11,449.50 | $13,737.30 | $10,920.02 | $10,000.00 | $10,000.00 | $9,645.85 |
| 2026-11-21 | $11,254.31 | $13,278.13 | $11,004.09 | $10,000.00 | $9,998.52 | $9,612.09 |
| 2026-11-22 | $11,083.23 | – | – | $10,000.00 | $10,021.08 | $9,635.59 |
| 2026-11-23 | $11,088.22 | $12,939.80 | $10,903.60 | $10,000.00 | $10,004.27 | $9,613.54 |
| 2026-11-24 | $11,161.99 | $13,215.80 | $10,981.81 | $10,000.00 | $9,995.08 | $9,550.56 |
| 2026-11-25 | $11,043.46 | $12,812.25 | $10,894.07 | $10,000.00 | $10,041.11 | $9,658.04 |
| now | $11,042.01 | $12,808.25 | $10,894.26 | $10,000.00 | $10,041.11 | $9,658.04 |

</details>

### Open positions

| Strategy | Coin | Side | Entry → now | Profit | To stop | To liquidation / Alpaca |
|---|---|---|---|--:|--:|--:|
| 🔵 MA | **WLD** | ▼ Short | 0.38553 → 0.24265 | +$370.61 (+75.5%) | ✅ 71.6% | ✅ 125.6% |
| 🔵 MA | **NEAR** | ▼ Short | 4.0459 → 3.0585 | +$244.05 (+48.5%) | ✅ 42.9% | ✅ 89.3% |
| 🔵 MA | **ZRO** | ▼ Short | 1.6048 → 1.0644 | +$336.75 (+66.9%) | ✅ 62.8% | ✅ 106.1% |
| 🟠 Breakout | **SOL** | ▼ Short | 91.244 → 70.91 | +$222.85 (+44.5%) | ✅ 39.0% | ✅ 88.4% |
| 🟠 Breakout | **NEAR** | ▼ Short | 3.6822 → 3.0585 | +$169.38 (+33.7%) | ✅ 30.0% | ✅ 72.3% |
| 🟠 Breakout | **ENA** | ▼ Short | 0.1646 → 0.10299 | +$374.30 (+74.4%) | ✅ 72.6% | ✅ 128.7% |
| 🟠 Breakout | **WLD** | ▼ Short | 0.34441 → 0.24265 | +$295.47 (+60.2%) | ✅ 53.3% | ✅ 101.5% |
| 🟠 Breakout | **XRP** | ▼ Short | 1.1619 → 0.95315 | +$179.66 (+35.9%) | ✅ 31.7% | ✅ 78.4% |
| 🟠 Breakout | **PUMP** | ▼ Short | 0.003674 → 0.002633 | +$283.34 (+56.4%) | ✅ 50.7% | ✅ 99.6% |
| 🟠 Breakout | **SUI** | ▼ Short | 0.81988 → 0.67025 | +$182.51 (+36.7%) | ✅ 32.1% | ✅ 74.5% |
| 🟠 Breakout | **HYPE** | ▼ Short | 71.8649 → 61.103 | +$149.75 (+29.8%) | ✅ 27.0% | ✅ 68.4% |
| 🟠 Breakout | **ZEC** | ▼ Short | 1,003.70 → 745.07 | +$257.68 (+51.2%) | ✅ 45.5% | ✅ 92.9% |
| 🟠 Breakout | **UNI** | ▼ Short | 6.1326 → 4.7317 | +$228.43 (+45.7%) | ✅ 40.0% | ✅ 85.1% |
| 🟠 Breakout | **BNB** | ▼ Short | 632.05 → 554.31 | +$123.00 (+24.5%) | ✅ 23.1% | ✅ 63.0% |
| 🟠 Breakout | **AAVE** | ▼ Short | 111.00 → 95.87 | +$136.33 (+27.3%) | ✅ 25.0% | ✅ 65.4% |
| 🟠 Breakout | **XMR** | ▼ Short | 490.83 → 519.28 | −$57.96 (−11.5%) | ⚠️ 2.1% | ✅ 29.1% |
| 🟠 Breakout | **kPEPE** | ▼ Short | 0.003924 → 0.003524 | +$101.94 (+20.5%) | ✅ 20.3% | ✅ 58.9% |
| 🟠 Breakout | **ZRO** | ▼ Short | 1.4562 → 1.0644 | +$269.05 (+53.6%) | ✅ 47.8% | ✅ 86.8% |
| 🟠 Breakout | **VVV** | ▲ Long | 24.993 → 27.052 | +$82.38 (+16.5%) | ✅ 15.0% | ✅ 44.4% |
| 🟢 Momentum | **WLD** | ▼ Short | 0.38553 → 0.24265 | +$370.61 (+75.5%) | ✅ 71.6% | ✅ 125.6% |
| 🟢 Momentum | **ENA** | ▼ Short | 0.14951 → 0.10299 | +$311.16 (+61.9%) | ✅ 56.8% | ✅ 107.7% |
| 🟢 Momentum | **VVV** | ▲ Long | 20.0544 → 27.052 | +$348.93 (+70.6%) | ✅ 31.8% | ✅ 55.0% |
| 🟢 Momentum | **PUMP** | ▼ Short | 0.00287 → 0.002633 | +$82.58 (+16.5%) | ✅ 17.7% | ✅ 55.8% |
| 🟢 Momentum | **UNI** | ▼ Short | 5.1601 → 4.7317 | +$83.02 (+16.6%) | ✅ 17.8% | ✅ 55.8% |
| 🟠 Breakout (spot) | **VVV** | ▲ Long | 24.9223 → 27.039 | +$39.76 (+8.0%) | ✅ 15.2% | not on Alpaca |
| 🟢 Momentum (spot) | **VVV** | ▲ Long | 20.0503 → 27.039 | +$170.91 (+34.2%) | ✅ 31.8% | not on Alpaca |
| 🟢 Momentum (spot) | **XRP** | ▲ Long | 0.9366 → 0.95214 | +$5.76 (+1.2%) | ✅ 9.5% | ✅ copied |
| 🟢 Momentum (spot) | **LINK** | ▲ Long | 8.9148 → 9.1509 | +$10.68 (+2.1%) | ✅ 10.4% | ✅ copied |
| 🟢 Momentum (spot) | **XPL** | ▲ Long | 0.0454 → 0.047 | +$15.04 (+3.0%) | ✅ 11.1% | not on Alpaca |

_Distance = how far the price can still move against the position. ✅ over 5% · ⚠️ 2–5% · 🔴 under 2%. Spot can't be liquidated; its last column shows whether the trade is copied to Alpaca._

### Recent trades

| Time (PKT) | Strategy | Coin | What | Price | Result |
|---|---|---|---|--:|--:|
| Wed 25 Nov, 14:00 | 🟢 Momentum (spot) | **HYPE** | Stopped out | 57.831 | −$42.30 |
| Mon 23 Nov, 19:00 | 🔵 MA | **kPEPE** | Stopped out | 0.0036957 | −$80.59 |
| Mon 23 Nov, 18:00 | 🔵 MA | **XMR** | Stopped out | 517.36 | −$78.99 |
| Mon 23 Nov, 18:00 | 🟠 Breakout | **AVAX** | Stopped out | 6.8099 | −$81.62 |
| Mon 23 Nov, 18:00 | 🟠 Breakout | **DOGE** | Stopped out | 0.057597 | −$80.14 |
| Mon 23 Nov, 12:45 | 🟢 Momentum (spot) | **XRP** | Bought | 0.9366 | fee $1.25 |
| Mon 23 Nov, 12:45 | 🟢 Momentum (spot) | **HYPE** | Bought | 62.8598 | fee $1.25 |
| Mon 23 Nov, 12:45 | 🟢 Momentum (spot) | **LINK** | Bought | 8.9148 | fee $1.25 |
| Mon 23 Nov, 12:45 | 🟢 Momentum (spot) | **XPL** | Bought | 0.0454 | fee $1.25 |
| Mon 23 Nov, 12:44 | 🔵 MA | **SUI** | Closed | 0.66734 | +$255.80 |
| Mon 23 Nov, 12:44 | 🔵 MA | **kPEPE** | Opened short | 0.0034219 | fee $0.45 |
| Mon 23 Nov, 09:00 | 🟠 Breakout | **GRAM** | Stopped out | 0.99222 | −$82.07 |
| Sun 22 Nov, 11:54 | 🟠 Breakout | **VVV** | Opened long | 24.993 | fee $0.45 |
| Sun 22 Nov, 11:54 | 🟠 Breakout (spot) | **VVV** | Bought | 24.9223 | fee $1.25 |
| Sat 21 Nov, 20:00 | 🟢 Momentum (spot) | **LIT** | Stopped out | 0.070261 | −$42.30 |

### Signal board (daily candle of 2026-11-25)

What each strategy sees per coin. 🔔 = the condition for a trade is met.

| Coin | MA: 20d vs 50d | Breakout: vs 20-day range | Momentum: 14d return |
|---|---|---|---|
| **HYPE** | below (−10.6%) | +37.5% to high / −9.7% to low | −14.3% (#6) |
| **ZEC** | below (−14.9%) | +80.2% to high / −11.9% to low | −19.9% (#12) |
| **SOL** | below (−16.7%) | +37.8% to high / −7.9% to low | −15.3% (#8) |
| **XRP** | below (−15.9%) | +41.6% to high / −8.2% to low | −10.9% (#3) 🔔 top 5: long |
| **NEAR** | below (−20.7%) | +33.4% to high / −16.5% to low | −14.8% (#7) |
| **LIT** | below (−7.4%) | +48.5% to high / −10.1% to low | −26.2% (#18) 🔔 bottom 5: short |
| **XMR** | below (−5.9%) | +24.7% to high / −18.4% to low | −11.0% (#4) 🔔 top 5: long |
| **PUMP** | below (−24.2%) | +70.2% to high / −15.2% to low | −25.6% (#17) 🔔 bottom 5: short |
| **VVV** | below (−5.2%) | 🔔 above 20d high | +48.8% (#1) 🔔 top 5: long |
| **kPEPE** | below (−4.0%) | +61.5% to high / −9.0% to low | −23.0% (#15) |
| **AAVE** | below (−16.2%) | +41.2% to high / −4.6% to low | −20.9% (#13) |
| **UNI** | below (−15.1%) | +64.8% to high / −11.8% to low | −23.9% (#16) 🔔 bottom 5: short |
| **ENA** | below (−26.4%) | +82.3% to high / −11.1% to low | −30.6% (#19) 🔔 bottom 5: short |
| **DOGE** | below (−14.9%) | +38.2% to high / −9.4% to low | −17.0% (#10) |
| **WLD** | below (−30.0%) | +59.4% to high / −12.9% to low | −21.8% (#14) |
| **BNB** | below (−10.3%) | +30.3% to high / −9.2% to low | −18.5% (#11) |
| **ZRO** | below (−17.2%) | +81.4% to high / −1.9% to low | −33.6% (#20) 🔔 bottom 5: short |
| **LINK** | below (−13.4%) | +28.9% to high / −12.2% to low | −11.2% (#5) 🔔 top 5: long |
| **ADA** | below (−17.4%) | +36.8% to high / −8.6% to low | −16.4% (#9) |
| **XPL** | below (−26.3%) | +38.7% to high / −15.6% to low | −8.1% (#2) 🔔 top 5: long |

_Momentum trades its top/bottom 5 at the Monday rebalance; MA and breakout act at each daily run. Spot uses the same signals but only buys: a short signal just sells what it holds._

### This week's coins (chosen 2026-11-23)

HYPE · ZEC · SOL · XRP · NEAR · LIT · XMR · PUMP · VVV · kPEPE · AAVE · UNI · ENA · DOGE · WLD · BNB · ZRO · LINK · ADA · XPL

_The 20 most-traded Hyperliquid futures over the past week, excluding BTC and ETH. Refreshed Mondays 00:00 UTC (5:00 AM PKT)._

## Alpaca paper account

Value **$49,210.23** · cash $45,449.84 · account ending YUU8  
Holding: 55.9462 LINKUSD (+$17.34), 2 MU (−$676.36), 7e-09 PEPEUSD ($0.00), 532.511 XRPUSD (+$9.01)

**2** simulated spot trade(s) copied and open. Copies use the same number of coins as the simulation, with a real stop order on Alpaca.

Crypto spot bot: no coins on its watchlist yet (daily 00:15 UTC). Stock bot: stopped.

---
✅ Last run OK · [futures log](logs/futures_bot.log) · [spot log](logs/spot_bot.log) · [project log](PROJECT_LOG.md) · on the PC: `python dashboard.py`

<sub>This page is written by summary.py; edits by hand are overwritten.</sub>
