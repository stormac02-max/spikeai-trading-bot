# SpikeAI paper trading

_Updated **Sat 28 Nov 2026, 12:54 PKT** (Sat 02:54 ET). Refreshed after every daily run. Paper trading only: no real money._

## Strategy test: MA crossover vs breakout vs momentum

**29 days left** in the evaluation (until 2026-12-27), then the best strategy is kept.  
Each simulated account started with $10,000. Futures: 2x, long and short, $500 margin per trade. Spot: 1x, buy-only, $500 per buy, copied to Alpaca for coins it lists. Both use an 8% stop.

### Futures

| Strategy | Value | Return | Below peak | Open | Closed (won) | Fees | Funding |
|---|--:|--:|--:|--:|--:|--:|--:|
| 🔵 MA crossover 20/50 | **$11,033.25** | +10.33% | −3.64% | 3 | 3 (1) | $4.01 | −$1.02 |
| 🟠 Breakout 20/10 | **$12,994.72** | +29.95% | −5.41% | 16 | 10 (2) | $16.28 | +$10.07 |
| 🟢 Momentum 14d, 5 long/5 short | **$10,891.84** | +8.92% | −1.02% | 5 | 20 (6) | $19.48 | −$11.28 |

**Futures leader:** 🟠 Breakout 20/10, $1,961.48 ahead of MA crossover 20/50.

### Spot

| Strategy | Value | Return | Below peak | Held | Closed (won) | Fees | On Alpaca |
|---|--:|--:|--:|--:|--:|--:|--:|
| 🔵 MA crossover 20/50 | **$10,000.00** | 0.00% | at peak | 0 | 0 | $0.00 | 0 |
| 🟠 Breakout 20/10 | **$10,026.90** | +0.27% | −0.14% | 1 | 0 | $1.25 | 0 |
| 🟢 Momentum 14d, 5 long/5 short | **$9,624.13** | −3.76% | −3.76% | 4 | 13 (0) | $36.16 | 2 |

**Spot leader:** 🟠 Breakout 20/10, $26.90 ahead of MA crossover 20/50.

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
| 2026-11-26 | $10,967.35 | $12,633.25 | $10,805.93 | $10,000.00 | $10,036.95 | $9,710.48 |
| 2026-11-27 | $11,032.81 | $12,991.39 | $10,891.11 | $10,000.00 | $10,026.90 | $9,624.13 |
| now | $11,033.25 | $12,994.72 | $10,891.84 | $10,000.00 | $10,026.90 | $9,624.13 |

</details>

### Open positions

| Strategy | Coin | Side | Entry → now | Profit | To stop | To liquidation / Alpaca |
|---|---|---|---|--:|--:|--:|
| 🔵 MA | **WLD** | ▼ Short | 0.38553 → 0.24041 | +$376.42 (+76.8%) | ✅ 73.2% | ✅ 127.6% |
| 🔵 MA | **NEAR** | ▼ Short | 4.0459 → 3.0307 | +$250.92 (+49.9%) | ✅ 44.2% | ✅ 91.1% |
| 🔵 MA | **ZRO** | ▼ Short | 1.6048 → 1.0992 | +$315.07 (+62.5%) | ✅ 57.7% | ✅ 99.6% |
| 🟠 Breakout | **SOL** | ▼ Short | 91.244 → 71.232 | +$219.32 (+43.8%) | ✅ 38.3% | ✅ 87.5% |
| 🟠 Breakout | **NEAR** | ▼ Short | 3.6822 → 3.0307 | +$176.93 (+35.2%) | ✅ 31.2% | ✅ 73.9% |
| 🟠 Breakout | **ENA** | ▼ Short | 0.1646 → 0.10222 | +$378.98 (+75.3%) | ✅ 73.9% | ✅ 130.5% |
| 🟠 Breakout | **WLD** | ▼ Short | 0.34441 → 0.24041 | +$301.97 (+61.6%) | ✅ 54.7% | ✅ 103.4% |
| 🟠 Breakout | **XRP** | ▼ Short | 1.1619 → 0.94466 | +$186.97 (+37.4%) | ✅ 32.8% | ✅ 80.0% |
| 🟠 Breakout | **PUMP** | ▼ Short | 0.003674 → 0.002583 | +$296.95 (+59.1%) | ✅ 53.6% | ✅ 103.5% |
| 🟠 Breakout | **SUI** | ▼ Short | 0.81988 → 0.6693 | +$183.66 (+36.9%) | ✅ 32.3% | ✅ 74.8% |
| 🟠 Breakout | **HYPE** | ▼ Short | 71.8649 → 63.958 | +$110.02 (+21.8%) | ✅ 21.4% | ✅ 60.9% |
| 🟠 Breakout | **ZEC** | ▼ Short | 1,003.70 → 738.15 | +$264.57 (+52.5%) | ✅ 46.9% | ✅ 94.7% |
| 🟠 Breakout | **UNI** | ▼ Short | 6.1326 → 4.7017 | +$233.33 (+46.7%) | ✅ 40.9% | ✅ 86.3% |
| 🟠 Breakout | **BNB** | ▼ Short | 632.05 → 551.70 | +$127.13 (+25.4%) | ✅ 23.7% | ✅ 63.8% |
| 🟠 Breakout | **AAVE** | ▼ Short | 111.00 → 93.658 | +$156.26 (+31.3%) | ✅ 28.0% | ✅ 69.3% |
| 🟠 Breakout | **XMR** | ▼ Short | 490.83 → 424.54 | +$135.06 (+26.8%) | ✅ 24.9% | ✅ 58.0% |
| 🟠 Breakout | **kPEPE** | ▼ Short | 0.003924 → 0.003486 | +$111.62 (+22.4%) | ✅ 21.6% | ✅ 60.6% |
| 🟠 Breakout | **ZRO** | ▼ Short | 1.4562 → 1.0992 | +$245.15 (+48.8%) | ✅ 43.1% | ✅ 81.0% |
| 🟠 Breakout | **VVV** | ▲ Long | 24.993 → 26.317 | +$52.97 (+10.6%) | ✅ 12.6% | ✅ 42.8% |
| 🟢 Momentum | **WLD** | ▼ Short | 0.38553 → 0.24041 | +$376.42 (+76.8%) | ✅ 73.2% | ✅ 127.6% |
| 🟢 Momentum | **ENA** | ▼ Short | 0.14951 → 0.10222 | +$316.31 (+62.9%) | ✅ 58.0% | ✅ 109.3% |
| 🟢 Momentum | **VVV** | ▲ Long | 20.0544 → 26.317 | +$312.28 (+63.2%) | ✅ 29.9% | ✅ 53.7% |
| 🟢 Momentum | **PUMP** | ▼ Short | 0.00287 → 0.002583 | +$100.00 (+19.9%) | ✅ 20.0% | ✅ 58.9% |
| 🟢 Momentum | **UNI** | ▼ Short | 5.1601 → 4.7017 | +$88.84 (+17.7%) | ✅ 18.5% | ✅ 56.8% |
| 🟠 Breakout (spot) | **VVV** | ▲ Long | 24.9223 → 26.329 | +$25.58 (+5.1%) | ✅ 12.9% | not on Alpaca |
| 🟢 Momentum (spot) | **VVV** | ▲ Long | 20.0503 → 26.329 | +$153.29 (+30.7%) | ✅ 29.9% | not on Alpaca |
| 🟢 Momentum (spot) | **XRP** | ▲ Long | 0.9366 → 0.94412 | +$1.50 (+0.3%) | ✅ 8.7% | ✅ copied |
| 🟢 Momentum (spot) | **LINK** | ▲ Long | 8.9148 → 9.1724 | +$11.88 (+2.4%) | ✅ 10.6% | ✅ copied |
| 🟢 Momentum (spot) | **XPL** | ▲ Long | 0.0454 → 0.0458 | +$1.89 (+0.4%) | ✅ 8.8% | not on Alpaca |

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

### Signal board (daily candle of 2026-11-27)

What each strategy sees per coin. 🔔 = the condition for a trade is met.

| Coin | MA: 20d vs 50d | Breakout: vs 20-day range | Momentum: 14d return |
|---|---|---|---|
| **HYPE** | below (−11.5%) | +25.3% to high / −12.2% to low | −11.4% (#7) |
| **ZEC** | below (−18.5%) | +85.6% to high / −9.7% to low | −21.2% (#16) 🔔 bottom 5: short |
| **SOL** | below (−17.2%) | +26.5% to high / −9.4% to low | −8.3% (#5) 🔔 top 5: long |
| **XRP** | below (−16.5%) | +24.6% to high / −9.3% to low | −6.1% (#3) 🔔 top 5: long |
| **NEAR** | below (−20.9%) | +26.5% to high / −15.6% to low | −12.3% (#10) |
| **LIT** | below (−8.6%) | +33.0% to high / −19.4% to low | −17.2% (#14) |
| **XMR** | below (−8.3%) | 🔔 below 20d low | −22.9% (#18) 🔔 bottom 5: short |
| **PUMP** | below (−24.8%) | +52.3% to high / −15.9% to low | −24.5% (#19) 🔔 bottom 5: short |
| **VVV** | below (−3.2%) | +18.6% to high / −35.4% to low | +36.0% (#1) 🔔 top 5: long |
| **kPEPE** | below (−6.9%) | +58.8% to high / −10.5% to low | −19.6% (#15) |
| **AAVE** | below (−17.0%) | +40.9% to high / −6.1% to low | −14.4% (#11) |
| **UNI** | below (−17.2%) | +50.1% to high / −13.3% to low | −16.0% (#12) |
| **ENA** | below (−28.0%) | +58.7% to high / −13.8% to low | −22.5% (#17) 🔔 bottom 5: short |
| **DOGE** | below (−15.6%) | +26.0% to high / −12.0% to low | −10.5% (#6) |
| **WLD** | below (−30.6%) | +39.4% to high / −15.5% to low | −16.1% (#13) |
| **BNB** | below (−11.3%) | +26.5% to high / −9.3% to low | −11.9% (#9) |
| **ZRO** | below (−18.5%) | +53.6% to high / −14.0% to low | −31.0% (#20) 🔔 bottom 5: short |
| **LINK** | below (−13.6%) | +16.9% to high / −15.1% to low | −4.9% (#2) 🔔 top 5: long |
| **ADA** | below (−17.5%) | +25.1% to high / −10.2% to low | −11.9% (#8) |
| **XPL** | below (−26.1%) | +27.3% to high / −14.5% to low | −6.7% (#4) 🔔 top 5: long |

_Momentum trades its top/bottom 5 at the Monday rebalance; MA and breakout act at each daily run. Spot uses the same signals but only buys: a short signal just sells what it holds._

### This week's coins (chosen 2026-11-23)

HYPE · ZEC · SOL · XRP · NEAR · LIT · XMR · PUMP · VVV · kPEPE · AAVE · UNI · ENA · DOGE · WLD · BNB · ZRO · LINK · ADA · XPL

_The 20 most-traded Hyperliquid futures over the past week, excluding BTC and ETH. Refreshed Mondays 00:00 UTC (5:00 AM PKT)._

## Alpaca paper account

Value **$49,293.76** · cash $45,449.84 · account ending YUU8  
Holding: 55.9462 LINKUSD (+$14.17), 2 MU (−$584.96), 7e-09 PEPEUSD ($0.00), 532.511 XRPUSD (+$4.30)

**2** simulated spot trade(s) copied and open. Copies use the same number of coins as the simulation, with a real stop order on Alpaca.

Crypto spot bot: no coins on its watchlist yet (daily 00:15 UTC). Stock bot: stopped.

---
✅ Last run OK · [futures log](logs/futures_bot.log) · [spot log](logs/spot_bot.log) · [project log](PROJECT_LOG.md) · on the PC: `python dashboard.py`

<sub>This page is written by summary.py; edits by hand are overwritten.</sub>
