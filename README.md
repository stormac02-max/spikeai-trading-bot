# SpikeAI paper trading

_Updated **Fri 27 Nov 2026, 13:40 PKT** (Fri 03:40 ET). Refreshed after every daily run. Paper trading only: no real money._

## Strategy test: MA crossover vs breakout vs momentum

**30 days left** in the evaluation (until 2026-12-27), then the best strategy is kept.  
Each simulated account started with $10,000. Futures: 2x, long and short, $500 margin per trade. Spot: 1x, buy-only, $500 per buy, copied to Alpaca for coins it lists. Both use an 8% stop.

### Futures

| Strategy | Value | Return | Below peak | Open | Closed (won) | Fees | Funding |
|---|--:|--:|--:|--:|--:|--:|--:|
| 🔵 MA crossover 20/50 | **$10,966.64** | +9.67% | −4.22% | 3 | 3 (1) | $4.01 | −$1.20 |
| 🟠 Breakout 20/10 | **$12,630.58** | +26.31% | −8.06% | 16 | 10 (2) | $16.28 | +$9.95 |
| 🟢 Momentum 14d, 5 long/5 short | **$10,806.26** | +8.06% | −1.80% | 5 | 20 (6) | $19.48 | −$11.47 |

**Futures leader:** 🟠 Breakout 20/10, $1,663.93 ahead of MA crossover 20/50.

### Spot

| Strategy | Value | Return | Below peak | Held | Closed (won) | Fees | On Alpaca |
|---|--:|--:|--:|--:|--:|--:|--:|
| 🔵 MA crossover 20/50 | **$10,000.00** | 0.00% | at peak | 0 | 0 | $0.00 | 0 |
| 🟠 Breakout 20/10 | **$10,036.95** | +0.37% | −0.04% | 1 | 0 | $1.25 | 0 |
| 🟢 Momentum 14d, 5 long/5 short | **$9,710.70** | −2.89% | −2.89% | 4 | 13 (0) | $36.16 | 2 |

**Spot leader:** 🟠 Breakout 20/10, $36.95 ahead of MA crossover 20/50.

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
| now | $10,966.64 | $12,630.58 | $10,806.26 | $10,000.00 | $10,036.95 | $9,710.70 |

</details>

### Open positions

| Strategy | Coin | Side | Entry → now | Profit | To stop | To liquidation / Alpaca |
|---|---|---|---|--:|--:|--:|
| 🔵 MA | **WLD** | ▼ Short | 0.38553 → 0.25199 | +$346.38 (+70.6%) | ✅ 65.2% | ✅ 117.2% |
| 🔵 MA | **NEAR** | ▼ Short | 4.0459 → 3.0995 | +$233.92 (+46.5%) | ✅ 41.0% | ✅ 86.9% |
| 🔵 MA | **ZRO** | ▼ Short | 1.6048 → 1.1303 | +$295.69 (+58.7%) | ✅ 53.3% | ✅ 94.1% |
| 🟠 Breakout | **SOL** | ▼ Short | 91.244 → 73.157 | +$198.23 (+39.6%) | ✅ 34.7% | ✅ 82.6% |
| 🟠 Breakout | **NEAR** | ▼ Short | 3.6822 → 3.0995 | +$158.25 (+31.5%) | ✅ 28.3% | ✅ 70.1% |
| 🟠 Breakout | **ENA** | ▼ Short | 0.1646 → 0.1059 | +$356.62 (+70.9%) | ✅ 67.9% | ✅ 122.5% |
| 🟠 Breakout | **WLD** | ▼ Short | 0.34441 → 0.25199 | +$268.35 (+54.7%) | ✅ 47.6% | ✅ 94.0% |
| 🟠 Breakout | **XRP** | ▼ Short | 1.1619 → 0.97939 | +$157.08 (+31.4%) | ✅ 28.1% | ✅ 73.6% |
| 🟠 Breakout | **PUMP** | ▼ Short | 0.003674 → 0.00265 | +$278.72 (+55.5%) | ✅ 49.7% | ✅ 98.4% |
| 🟠 Breakout | **SUI** | ▼ Short | 0.81988 → 0.68621 | +$163.04 (+32.7%) | ✅ 29.0% | ✅ 70.5% |
| 🟠 Breakout | **HYPE** | ▼ Short | 71.8649 → 65.547 | +$87.91 (+17.5%) | ✅ 18.4% | ✅ 57.0% |
| 🟠 Breakout | **ZEC** | ▼ Short | 1,003.70 → 747.83 | +$254.93 (+50.6%) | ✅ 45.0% | ✅ 92.2% |
| 🟠 Breakout | **UNI** | ▼ Short | 6.1326 → 4.8819 | +$203.94 (+40.8%) | ✅ 35.7% | ✅ 79.4% |
| 🟠 Breakout | **BNB** | ▼ Short | 632.05 → 564.35 | +$107.12 (+21.4%) | ✅ 21.0% | ✅ 60.1% |
| 🟠 Breakout | **AAVE** | ▼ Short | 111.00 → 96.6 | +$129.76 (+26.0%) | ✅ 24.1% | ✅ 64.1% |
| 🟠 Breakout | **XMR** | ▼ Short | 490.83 → 455.48 | +$72.02 (+14.3%) | ✅ 16.4% | ✅ 47.4% |
| 🟠 Breakout | **kPEPE** | ▼ Short | 0.003924 → 0.003602 | +$82.06 (+16.5%) | ✅ 17.7% | ✅ 55.4% |
| 🟠 Breakout | **ZRO** | ▼ Short | 1.4562 → 1.1303 | +$223.80 (+44.5%) | ✅ 39.1% | ✅ 76.0% |
| 🟠 Breakout | **VVV** | ▲ Long | 24.993 → 26.869 | +$75.06 (+15.1%) | ✅ 14.4% | ✅ 44.0% |
| 🟢 Momentum | **WLD** | ▼ Short | 0.38553 → 0.25199 | +$346.38 (+70.6%) | ✅ 65.2% | ✅ 117.2% |
| 🟢 Momentum | **ENA** | ▼ Short | 0.14951 → 0.1059 | +$291.69 (+58.0%) | ✅ 52.5% | ✅ 102.0% |
| 🟢 Momentum | **VVV** | ▲ Long | 20.0544 → 26.869 | +$339.81 (+68.8%) | ✅ 31.3% | ✅ 54.7% |
| 🟢 Momentum | **PUMP** | ▼ Short | 0.00287 → 0.00265 | +$76.66 (+15.3%) | ✅ 17.0% | ✅ 54.9% |
| 🟢 Momentum | **UNI** | ▼ Short | 5.1601 → 4.8819 | +$53.91 (+10.8%) | ✅ 14.2% | ✅ 51.0% |
| 🟠 Breakout (spot) | **VVV** | ▲ Long | 24.9223 → 26.831 | +$35.61 (+7.1%) | ✅ 14.5% | not on Alpaca |
| 🟢 Momentum (spot) | **VVV** | ▲ Long | 20.0503 → 26.831 | +$165.75 (+33.2%) | ✅ 31.3% | not on Alpaca |
| 🟢 Momentum (spot) | **XRP** | ▲ Long | 0.9366 → 0.979 | +$20.03 (+4.0%) | ✅ 12.0% | ✅ copied |
| 🟢 Momentum (spot) | **LINK** | ▲ Long | 8.9148 → 9.5755 | +$34.37 (+6.9%) | ✅ 14.3% | ✅ copied |
| 🟢 Momentum (spot) | **XPL** | ▲ Long | 0.0454 → 0.0488 | +$34.76 (+7.0%) | ✅ 14.4% | not on Alpaca |

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

### Signal board (daily candle of 2026-11-26)

What each strategy sees per coin. 🔔 = the condition for a trade is met.

| Coin | MA: 20d vs 50d | Breakout: vs 20-day range | Momentum: 14d return |
|---|---|---|---|
| **HYPE** | below (−11.0%) | +27.8% to high / −10.5% to low | −14.3% (#7) |
| **ZEC** | below (−16.8%) | +103.8% to high / −1.2% to low | −28.7% (#20) 🔔 bottom 5: short |
| **SOL** | below (−16.9%) | +29.0% to high / −8.6% to low | −13.1% (#6) |
| **XRP** | below (−16.2%) | +29.6% to high / −8.8% to low | −9.4% (#4) 🔔 top 5: long |
| **NEAR** | below (−20.6%) | +25.5% to high / −16.4% to low | −10.9% (#5) 🔔 top 5: long |
| **LIT** | below (−8.1%) | +44.1% to high / −12.7% to low | −23.1% (#14) |
| **XMR** | below (−7.0%) | +36.7% to high / −7.9% to low | −16.3% (#11) |
| **PUMP** | below (−24.4%) | +61.8% to high / −15.4% to low | −25.9% (#17) 🔔 bottom 5: short |
| **VVV** | below (−4.0%) | +11.8% to high / −36.3% to low | +38.0% (#1) 🔔 top 5: long |
| **kPEPE** | below (−5.5%) | +61.9% to high / −8.8% to low | −23.3% (#16) 🔔 bottom 5: short |
| **AAVE** | below (−16.6%) | +42.4% to high / −5.1% to low | −17.1% (#12) |
| **UNI** | below (−16.0%) | +55.6% to high / −10.1% to low | −23.3% (#15) |
| **ENA** | below (−27.2%) | +71.3% to high / −10.5% to low | −28.6% (#19) 🔔 bottom 5: short |
| **DOGE** | below (−15.2%) | +29.9% to high / −10.1% to low | −15.1% (#9) |
| **WLD** | below (−30.3%) | +47.0% to high / −13.4% to low | −19.8% (#13) |
| **BNB** | below (−10.8%) | +26.7% to high / −9.2% to low | −15.6% (#10) |
| **ZRO** | below (−17.6%) | +50.0% to high / −17.2% to low | −27.1% (#18) 🔔 bottom 5: short |
| **LINK** | below (−13.4%) | +19.0% to high / −14.3% to low | −8.5% (#3) 🔔 top 5: long |
| **ADA** | below (−17.4%) | +27.7% to high / −10.3% to low | −14.8% (#8) |
| **XPL** | below (−26.2%) | +24.9% to high / −16.1% to low | −4.9% (#2) 🔔 top 5: long |

_Momentum trades its top/bottom 5 at the Monday rebalance; MA and breakout act at each daily run. Spot uses the same signals but only buys: a short signal just sells what it holds._

### This week's coins (chosen 2026-11-23)

HYPE · ZEC · SOL · XRP · NEAR · LIT · XMR · PUMP · VVV · kPEPE · AAVE · UNI · ENA · DOGE · WLD · BNB · ZRO · LINK · ADA · XPL

_The 20 most-traded Hyperliquid futures over the past week, excluding BTC and ETH. Refreshed Mondays 00:00 UTC (5:00 AM PKT)._

## Alpaca paper account

Value **$49,317.03** · cash $45,449.84 · account ending YUU8  
Holding: 55.9462 LINKUSD (+$36.97), 2 MU (−$600.86), 7e-09 PEPEUSD ($0.00), 532.511 XRPUSD (+$20.68)

**2** simulated spot trade(s) copied and open. Copies use the same number of coins as the simulation, with a real stop order on Alpaca.

Crypto spot bot: no coins on its watchlist yet (daily 00:15 UTC). Stock bot: stopped.

---
✅ Last run OK · [futures log](logs/futures_bot.log) · [spot log](logs/spot_bot.log) · [project log](PROJECT_LOG.md) · on the PC: `python dashboard.py`

<sub>This page is written by summary.py; edits by hand are overwritten.</sub>
