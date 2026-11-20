# SpikeAI paper trading

_Updated **Fri 20 Nov 2026, 12:21 PKT** (Fri 02:21 ET). Refreshed after every daily run. Paper trading only: no real money._

## Strategy test: MA crossover vs breakout vs momentum

**37 days left** in the evaluation (until 2026-12-27), then the best strategy is kept.  
Each simulated account started with $10,000. Futures: 2x, long and short, $500 margin per trade. Spot: 1x, buy-only, $500 per buy, copied to Alpaca for coins it lists. Both use an 8% stop.

### Futures

| Strategy | Value | Return | Below peak | Open | Closed (won) | Fees | Funding |
|---|--:|--:|--:|--:|--:|--:|--:|
| 🔵 MA crossover 20/50 | **$11,046.14** | +10.46% | at peak | 5 | 0 | $2.25 | +$0.23 |
| 🟠 Breakout 20/10 | **$12,573.39** | +25.73% | at peak | 15 | 7 (2) | $13.02 | +$11.92 |
| 🟢 Momentum 14d, 5 long/5 short | **$10,718.89** | +7.19% | at peak | 8 | 17 (6) | $18.24 | −$6.08 |

**Futures leader:** 🟠 Breakout 20/10, $1,527.25 ahead of MA crossover 20/50.

### Spot

| Strategy | Value | Return | Below peak | Held | Closed (won) | Fees | On Alpaca |
|---|--:|--:|--:|--:|--:|--:|--:|
| 🔵 MA crossover 20/50 | **$10,000.00** | 0.00% | at peak | 0 | 0 | $0.00 | 0 |
| 🟠 Breakout 20/10 | **$10,000.00** | 0.00% | at peak | 0 | 0 | $0.00 | 0 |
| 🟢 Momentum 14d, 5 long/5 short | **$9,759.36** | −2.41% | −2.41% | 4 | 9 (0) | $26.57 | 1 |

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
| 2026-11-15 | $10,879.67 | $12,066.42 | $10,633.32 | $10,000.00 | $10,000.00 | $9,614.19 |
| 2026-11-16 | $10,754.52 | $11,659.55 | $10,585.62 | $10,000.00 | $10,000.00 | $9,678.18 |
| 2026-11-17 | $10,822.96 | $11,790.38 | $10,654.51 | $10,000.00 | $10,000.00 | $9,820.39 |
| 2026-11-18 | $10,770.65 | $11,796.49 | $10,712.06 | $10,000.00 | $10,000.00 | $9,874.21 |
| 2026-11-19 | $11,045.66 | $12,571.77 | $10,718.62 | $10,000.00 | $10,000.00 | $9,759.36 |
| now | $11,046.14 | $12,573.39 | $10,718.89 | $10,000.00 | $10,000.00 | $9,759.36 |

</details>

### Open positions

| Strategy | Coin | Side | Entry → now | Profit | To stop | To liquidation / Alpaca |
|---|---|---|---|--:|--:|--:|
| 🔵 MA | **SUI** | ▼ Short | 0.89681 → 0.69758 | +$222.15 (+44.3%) | ✅ 38.8% | ✅ 83.8% |
| 🔵 MA | **WLD** | ▼ Short | 0.38553 → 0.24679 | +$359.87 (+72.9%) | ✅ 68.7% | ✅ 122.3% |
| 🔵 MA | **NEAR** | ▼ Short | 4.0459 → 3.0445 | +$247.51 (+49.3%) | ✅ 43.5% | ✅ 90.2% |
| 🔵 MA | **ZRO** | ▼ Short | 1.6048 → 1.2541 | +$218.54 (+43.5%) | ✅ 38.2% | ✅ 74.8% |
| 🔵 MA | **XMR** | ▼ Short | 479.04 → 479.00 | +$0.08 (+0.0%) | ✅ 8.0% | ✅ 36.4% |
| 🟠 Breakout | **SOL** | ▼ Short | 91.244 → 72.607 | +$204.25 (+40.8%) | ✅ 35.7% | ✅ 84.0% |
| 🟠 Breakout | **NEAR** | ▼ Short | 3.6822 → 3.0445 | +$173.18 (+34.5%) | ✅ 30.6% | ✅ 73.1% |
| 🟠 Breakout | **ENA** | ▼ Short | 0.1646 → 0.10473 | +$363.73 (+72.4%) | ✅ 69.7% | ✅ 124.8% |
| 🟠 Breakout | **WLD** | ▼ Short | 0.34441 → 0.24679 | +$283.45 (+57.3%) | ✅ 50.7% | ✅ 98.6% |
| 🟠 Breakout | **XRP** | ▼ Short | 1.1619 → 0.96607 | +$168.54 (+33.7%) | ✅ 29.9% | ✅ 76.0% |
| 🟠 Breakout | **PUMP** | ▼ Short | 0.003674 → 0.002542 | +$308.11 (+61.4%) | ✅ 56.1% | ✅ 106.7% |
| 🟠 Breakout | **SUI** | ▼ Short | 0.81988 → 0.69758 | +$149.17 (+29.9%) | ✅ 26.9% | ✅ 67.9% |
| 🟠 Breakout | **HYPE** | ▼ Short | 71.8649 → 65.711 | +$85.63 (+17.1%) | ✅ 18.1% | ✅ 56.4% |
| 🟠 Breakout | **ZEC** | ▼ Short | 1,003.70 → 851.81 | +$151.33 (+30.1%) | ✅ 27.3% | ✅ 68.6% |
| 🟠 Breakout | **UNI** | ▼ Short | 6.1326 → 4.8308 | +$212.28 (+42.5%) | ✅ 37.1% | ✅ 81.3% |
| 🟠 Breakout | **BNB** | ▼ Short | 632.05 → 571.65 | +$95.57 (+19.1%) | ✅ 19.4% | ✅ 58.1% |
| 🟠 Breakout | **AAVE** | ▼ Short | 111.00 → 103.07 | +$71.47 (+14.3%) | ✅ 16.3% | ✅ 53.9% |
| 🟠 Breakout | **XMR** | ▼ Short | 490.83 → 479.00 | +$24.11 (+4.8%) | ✅ 10.7% | ✅ 39.7% |
| 🟠 Breakout | **kPEPE** | ▼ Short | 0.003924 → 0.003591 | +$84.86 (+17.0%) | ✅ 18.0% | ✅ 56.2% |
| 🟠 Breakout | **ZRO** | ▼ Short | 1.4562 → 1.2541 | +$138.78 (+27.7%) | ✅ 25.4% | ✅ 58.5% |
| 🟢 Momentum | **WLD** | ▼ Short | 0.38553 → 0.24679 | +$359.87 (+72.9%) | ✅ 68.7% | ✅ 122.3% |
| 🟢 Momentum | **ENA** | ▼ Short | 0.14951 → 0.10473 | +$299.52 (+59.7%) | ✅ 54.2% | ✅ 104.2% |
| 🟢 Momentum | **BNB** | ▲ Long | 589.91 → 571.65 | −$30.95 (−6.2%) | ✅ 5.1% | ✅ 45.6% |
| 🟢 Momentum | **AVAX** | ▲ Long | 7.102 → 6.9 | −$28.44 (−5.7%) | ✅ 5.3% | ✅ 45.8% |
| 🟢 Momentum | **GRAM** | ▲ Long | 1.0515 → 1.0136 | −$36.05 (−7.2%) | ⚠️ 4.6% | ✅ 42.4% |
| 🟢 Momentum | **VVV** | ▲ Long | 20.0544 → 20.704 | +$32.39 (+6.5%) | ✅ 10.9% | ✅ 41.6% |
| 🟢 Momentum | **PUMP** | ▼ Short | 0.00287 → 0.002542 | +$114.29 (+22.8%) | ✅ 21.9% | ✅ 61.4% |
| 🟢 Momentum | **UNI** | ▼ Short | 5.1601 → 4.8308 | +$63.82 (+12.8%) | ✅ 15.4% | ✅ 52.6% |
| 🟢 Momentum (spot) | **BNB** | ▲ Long | 589.82 → 571.77 | −$17.72 (−3.5%) | ✅ 5.1% | not on Alpaca |
| 🟢 Momentum (spot) | **AVAX** | ▲ Long | 7.106 → 6.901 | −$16.85 (−3.4%) | ✅ 5.3% | ✅ copied |
| 🟢 Momentum (spot) | **VVV** | ▲ Long | 20.0503 → 20.659 | +$12.61 (+2.5%) | ✅ 10.7% | not on Alpaca |
| 🟢 Momentum (spot) | **LIT** | ▲ Long | 0.07637 → 0.1008 | +$156.65 (+31.3%) | ✅ 30.3% | not on Alpaca |

_Distance = how far the price can still move against the position. ✅ over 5% · ⚠️ 2–5% · 🔴 under 2%. Spot can't be liquidated; its last column shows whether the trade is copied to Alpaca._

### Recent trades

| Time (PKT) | Strategy | Coin | What | Price | Result |
|---|---|---|---|--:|--:|
| Fri 20 Nov, 12:21 | 🔵 MA | **XMR** | Opened short | 479.04 | fee $0.45 |
| Tue 17 Nov, 17:00 | 🟢 Momentum | **ZEC** | Stopped out | 957.52 | −$80.13 |
| Tue 17 Nov, 08:00 | 🟠 Breakout | **VVV** | Stopped out | 21.0006 | −$79.62 |
| Mon 16 Nov, 15:00 | 🟢 Momentum | **LIT** | Stopped out | 2.4855 | −$80.38 |
| Mon 16 Nov, 11:36 | 🟠 Breakout | **XPL** | Closed | 0.042901 | +$318.85 |
| Mon 16 Nov, 11:36 | 🟠 Breakout | **TRUMP** | Closed | 0.93689 | +$1.64 |
| Mon 16 Nov, 11:36 | 🟠 Breakout | **LINK** | Closed | 9.099 | −$2.15 |
| Mon 16 Nov, 11:36 | 🟢 Momentum | **TRUMP** | Closed | 0.93789 | +$178.43 |
| Mon 16 Nov, 11:36 | 🟢 Momentum | **XPL** | Closed | 0.042926 | +$167.30 |
| Mon 16 Nov, 11:36 | 🟢 Momentum | **NEAR** | Closed | 3.1463 | +$253.49 |
| Mon 16 Nov, 11:36 | 🟢 Momentum | **BNB** | Opened long | 589.91 | fee $0.45 |
| Mon 16 Nov, 11:36 | 🟢 Momentum | **AVAX** | Opened long | 7.102 | fee $0.45 |
| Mon 16 Nov, 11:36 | 🟢 Momentum | **GRAM** | Opened long | 1.0515 | fee $0.45 |
| Mon 16 Nov, 11:36 | 🟢 Momentum | **VVV** | Opened long | 20.0544 | fee $0.45 |
| Mon 16 Nov, 11:36 | 🟢 Momentum | **LIT** | Opened long | 2.7016 | fee $0.45 |

### Signal board (daily candle of 2026-11-19)

What each strategy sees per coin. 🔔 = the condition for a trade is met.

| Coin | MA: 20d vs 50d | Breakout: vs 20-day range | Momentum: 14d return |
|---|---|---|---|
| **HYPE** | below (−6.0%) | +41.0% to high / −10.5% to low | −12.9% (#4) 🔔 top 5: long |
| **ZEC** | below (−7.9%) | +55.5% to high / −10.4% to low | −30.2% (#18) 🔔 bottom 5: short |
| **SOL** | below (−14.7%) | +34.7% to high / −7.8% to low | −18.1% (#9) |
| **XRP** | below (−12.6%) | +39.8% to high / −7.0% to low | −20.5% (#14) |
| **NEAR** | below (−17.6%) | +42.3% to high / −10.6% to low | −12.5% (#3) 🔔 top 5: long |
| **kPEPE** | above (+3.4%) | +51.6% to high / −1.7% to low | −22.6% (#15) |
| **XMR** | below (−0.6%) 🔔 crossed down | +30.2% to high / −8.8% to low | −19.5% (#12) |
| **PUMP** | below (−20.4%) | +72.5% to high / −5.1% to low | −31.6% (#19) 🔔 bottom 5: short |
| **LIT** | below (−4.1%) | +29.7% to high / −15.7% to low | −19.8% (#13) |
| **AVAX** | below (−12.6%) | +31.4% to high / −3.6% to low | −14.5% (#5) 🔔 top 5: long |
| **UNI** | below (−10.7%) | +58.6% to high / −6.5% to low | −27.6% (#17) 🔔 bottom 5: short |
| **ENA** | below (−20.8%) | 🔔 below 20d low | −34.6% (#20) 🔔 bottom 5: short |
| **DOGE** | below (−12.5%) | +34.7% to high / −4.8% to low | −18.2% (#10) |
| **SUI** | below (−14.1%) | +34.7% to high / −5.0% to low | −15.6% (#6) |
| **BNB** | below (−7.3%) | +24.7% to high / −2.5% to low | −15.9% (#7) |
| **GRAM** | below (−12.4%) | +26.9% to high / −2.6% to low | −7.6% (#2) 🔔 top 5: long |
| **VVV** | below (−10.5%) | +12.4% to high / −24.0% to low | +4.7% (#1) 🔔 top 5: long |
| **WLD** | below (−26.6%) | +65.0% to high / −4.1% to low | −24.2% (#16) 🔔 bottom 5: short |
| **AAVE** | below (−14.9%) | +34.5% to high / −7.7% to low | −18.8% (#11) |
| **ZRO** | below (−10.9%) | +48.9% to high / −2.2% to low | −17.7% (#8) |

_Momentum trades its top/bottom 5 at the Monday rebalance; MA and breakout act at each daily run. Spot uses the same signals but only buys: a short signal just sells what it holds._

### This week's coins (chosen 2026-11-16)

HYPE · ZEC · SOL · XRP · NEAR · kPEPE · XMR · PUMP · LIT · AVAX · UNI · ENA · DOGE · SUI · BNB · GRAM · VVV · WLD · AAVE · ZRO

_The 20 most-traded Hyperliquid futures over the past week, excluding BTC and ETH. Refreshed Mondays 00:00 UTC (5:00 AM PKT)._

## Alpaca paper account

Value **$49,358.28** · cash $46,504.43 · account ending YUU8  
Holding: 70.1872 AVAXUSD (−$14.09), 2 MU (−$532.00), 7e-09 PEPEUSD ($0.00)

**1** simulated spot trade(s) copied and open. Copies use the same number of coins as the simulation, with a real stop order on Alpaca.

Crypto spot bot: no coins on its watchlist yet (daily 00:15 UTC). Stock bot: stopped.

---
✅ Last run OK · [futures log](logs/futures_bot.log) · [spot log](logs/spot_bot.log) · [project log](PROJECT_LOG.md) · on the PC: `python dashboard.py`

<sub>This page is written by summary.py; edits by hand are overwritten.</sub>
