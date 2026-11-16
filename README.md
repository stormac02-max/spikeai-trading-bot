# SpikeAI paper trading

_Updated **Mon 16 Nov 2026, 11:36 PKT** (Mon 01:36 ET). Refreshed after every daily run. Paper trading only: no real money._

## Strategy test: MA crossover vs breakout vs momentum

**41 days left** in the evaluation (until 2026-12-27), then the best strategy is kept.  
Each simulated account started with $10,000. Futures: 2x, long and short, $500 margin per trade. Spot: 1x, buy-only, $500 per buy, copied to Alpaca for coins it lists. Both use an 8% stop.

### Futures

| Strategy | Value | Return | Below peak | Open | Closed (won) | Fees | Funding |
|---|--:|--:|--:|--:|--:|--:|--:|
| 🔵 MA crossover 20/50 | **$10,877.83** | +8.78% | −0.02% | 4 | 0 | $1.80 | −$0.21 |
| 🟠 Breakout 20/10 | **$12,054.03** | +20.54% | −0.10% | 16 | 6 (2) | $12.54 | +$5.53 |
| 🟢 Momentum 14d, 5 long/5 short | **$10,633.00** | +6.33% | at peak | 10 | 15 (6) | $17.34 | −$5.28 |

**Futures leader:** 🟠 Breakout 20/10, $1,176.21 ahead of MA crossover 20/50.

### Spot

| Strategy | Value | Return | Below peak | Held | Closed (won) | Fees | On Alpaca |
|---|--:|--:|--:|--:|--:|--:|--:|
| 🔵 MA crossover 20/50 | **$10,000.00** | 0.00% | at peak | 0 | 0 | $0.00 | 0 |
| 🟠 Breakout 20/10 | **$10,000.00** | 0.00% | at peak | 0 | 0 | $0.00 | 0 |
| 🟢 Momentum 14d, 5 long/5 short | **$9,614.19** | −3.86% | −3.86% | 4 | 9 (0) | $26.57 | 1 |

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
| now | $10,877.83 | $12,054.03 | $10,633.00 | $10,000.00 | $10,000.00 | $9,614.19 |

</details>

### Open positions

| Strategy | Coin | Side | Entry → now | Profit | To stop | To liquidation / Alpaca |
|---|---|---|---|--:|--:|--:|
| 🔵 MA | **SUI** | ▼ Short | 0.89681 → 0.71929 | +$197.95 (+39.5%) | ✅ 34.7% | ✅ 78.3% |
| 🔵 MA | **WLD** | ▼ Short | 0.38553 → 0.26418 | +$314.76 (+63.6%) | ✅ 57.6% | ✅ 107.7% |
| 🔵 MA | **NEAR** | ▼ Short | 4.0459 → 3.1465 | +$222.30 (+44.3%) | ✅ 38.9% | ✅ 83.9% |
| 🔵 MA | **ZRO** | ▼ Short | 1.6048 → 1.3724 | +$144.83 (+28.9%) | ✅ 26.3% | ✅ 59.6% |
| 🟠 Breakout | **SOL** | ▼ Short | 91.244 → 71.06 | +$221.21 (+44.2%) | ✅ 38.7% | ✅ 88.0% |
| 🟠 Breakout | **NEAR** | ▼ Short | 3.6822 → 3.1465 | +$145.48 (+29.0%) | ✅ 26.4% | ✅ 67.4% |
| 🟠 Breakout | **ENA** | ▼ Short | 0.1646 → 0.11763 | +$285.35 (+56.9%) | ✅ 51.1% | ✅ 100.1% |
| 🟠 Breakout | **WLD** | ▼ Short | 0.34441 → 0.26418 | +$232.96 (+47.0%) | ✅ 40.8% | ✅ 85.7% |
| 🟠 Breakout | **XRP** | ▼ Short | 1.1619 → 0.95149 | +$181.09 (+36.2%) | ✅ 31.9% | ✅ 78.7% |
| 🟠 Breakout | **PUMP** | ▼ Short | 0.003674 → 0.002871 | +$218.56 (+43.6%) | ✅ 38.2% | ✅ 82.9% |
| 🟠 Breakout | **SUI** | ▼ Short | 0.81988 → 0.71929 | +$122.69 (+24.5%) | ✅ 23.1% | ✅ 62.8% |
| 🟠 Breakout | **HYPE** | ▼ Short | 71.8649 → 66.2828 | +$77.67 (+15.5%) | ✅ 17.1% | ✅ 55.0% |
| 🟠 Breakout | **ZEC** | ▼ Short | 1,003.70 → 887.56 | +$115.71 (+23.1%) | ✅ 22.1% | ✅ 61.7% |
| 🟠 Breakout | **UNI** | ▼ Short | 6.1326 → 5.1605 | +$158.51 (+31.7%) | ✅ 28.3% | ✅ 69.7% |
| 🟠 Breakout | **BNB** | ▼ Short | 632.05 → 589.94 | +$66.63 (+13.3%) | ✅ 15.7% | ✅ 53.1% |
| 🟠 Breakout | **AAVE** | ▼ Short | 111.00 → 109.59 | +$12.73 (+2.5%) | ✅ 9.4% | ✅ 44.7% |
| 🟠 Breakout | **XMR** | ▼ Short | 490.83 → 481.72 | +$18.56 (+3.7%) | ✅ 10.0% | ✅ 39.0% |
| 🟠 Breakout | **kPEPE** | ▼ Short | 0.003924 → 0.003775 | +$37.97 (+7.6%) | ✅ 12.3% | ✅ 48.5% |
| 🟠 Breakout | **ZRO** | ▼ Short | 1.4562 → 1.3724 | +$57.54 (+11.5%) | ✅ 14.6% | ✅ 44.7% |
| 🟠 Breakout | **VVV** | ▼ Short | 19.445 → 20.061 | −$31.68 (−6.3%) | ⚠️ 4.7% | ✅ 24.6% |
| 🟢 Momentum | **WLD** | ▼ Short | 0.38553 → 0.26418 | +$314.76 (+63.6%) | ✅ 57.6% | ✅ 107.7% |
| 🟢 Momentum | **ENA** | ▼ Short | 0.14951 → 0.11763 | +$213.24 (+42.6%) | ✅ 37.3% | ✅ 81.7% |
| 🟢 Momentum | **BNB** | ▲ Long | 589.91 → 589.94 | +$0.06 (+0.0%) | ✅ 8.0% | ✅ 47.4% |
| 🟢 Momentum | **AVAX** | ▲ Long | 7.102 → 7.1043 | +$0.32 (+0.1%) | ✅ 8.0% | ✅ 47.4% |
| 🟢 Momentum | **GRAM** | ▲ Long | 1.0515 → 1.0512 | −$0.25 (−0.1%) | ✅ 8.0% | ✅ 44.4% |
| 🟢 Momentum | **VVV** | ▲ Long | 20.0544 → 20.061 | +$0.33 (+0.1%) | ✅ 8.0% | ✅ 40.0% |
| 🟢 Momentum | **LIT** | ▲ Long | 2.7016 → 2.7014 | −$0.07 (−0.0%) | ✅ 8.0% | ✅ 44.4% |
| 🟢 Momentum | **PUMP** | ▼ Short | 0.00287 → 0.002871 | −$0.35 (−0.1%) | ✅ 8.0% | ✅ 42.8% |
| 🟢 Momentum | **UNI** | ▼ Short | 5.1601 → 5.1605 | −$0.08 (−0.0%) | ✅ 8.0% | ✅ 42.8% |
| 🟢 Momentum | **ZEC** | ▼ Short | 886.59 → 887.56 | −$1.09 (−0.2%) | ✅ 7.9% | ✅ 42.7% |
| 🟢 Momentum (spot) | **BNB** | ▲ Long | 589.82 → 589.49 | −$2.77 (−0.6%) | ✅ 7.9% | not on Alpaca |
| 🟢 Momentum (spot) | **AVAX** | ▲ Long | 7.106 → 7.097 | −$3.13 (−0.6%) | ✅ 7.9% | ✅ copied |
| 🟢 Momentum (spot) | **VVV** | ▲ Long | 20.0503 → 20.021 | −$3.22 (−0.6%) | ✅ 7.9% | not on Alpaca |
| 🟢 Momentum (spot) | **LIT** | ▲ Long | 0.07637 → 0.0766 | −$1.00 (−0.2%) | ✅ 8.3% | not on Alpaca |

_Distance = how far the price can still move against the position. ✅ over 5% · ⚠️ 2–5% · 🔴 under 2%. Spot can't be liquidated; its last column shows whether the trade is copied to Alpaca._

### Recent trades

| Time (PKT) | Strategy | Coin | What | Price | Result |
|---|---|---|---|--:|--:|
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
| Mon 16 Nov, 11:36 | 🟢 Momentum | **PUMP** | Opened short | 0.00287 | fee $0.45 |
| Mon 16 Nov, 11:36 | 🟢 Momentum | **UNI** | Opened short | 5.1601 | fee $0.45 |
| Mon 16 Nov, 11:36 | 🟢 Momentum | **ZEC** | Opened short | 886.59 | fee $0.45 |
| Mon 16 Nov, 11:36 | 🟢 Momentum (spot) | **BNB** | Bought | 589.82 | fee $1.25 |

### Signal board (daily candle of 2026-11-15)

What each strategy sees per coin. 🔔 = the condition for a trade is met.

| Coin | MA: 20d vs 50d | Breakout: vs 20-day range | Momentum: 14d return |
|---|---|---|---|
| **HYPE** | below (−3.8%) | +42.6% to high / −12.3% to low | −22.5% (#13) |
| **ZEC** | below (−5.4%) | +52.8% to high / −12.5% to low | −25.8% (#16) 🔔 bottom 5: short |
| **SOL** | below (−12.8%) | +42.8% to high / −5.7% to low | −23.0% (#14) |
| **XRP** | below (−10.5%) | +38.1% to high / −8.4% to low | −22.1% (#11) |
| **NEAR** | below (−15.1%) | +50.0% to high / −10.9% to low | −25.0% (#15) |
| **kPEPE** | above (+7.0%) | +47.4% to high / −5.1% to low | −20.7% (#10) |
| **XMR** | above (+2.3%) | +32.2% to high / −8.9% to low | −16.9% (#6) |
| **PUMP** | below (−17.6%) | +56.8% to high / −8.2% to low | −29.2% (#18) 🔔 bottom 5: short |
| **LIT** | below (−7.1%) | +26.3% to high / −9.4% to low | −10.3% (#1) 🔔 top 5: long |
| **AVAX** | below (−12.1%) | +25.6% to high / −5.1% to low | −16.0% (#4) 🔔 top 5: long |
| **UNI** | below (−9.5%) | +50.9% to high / −11.0% to low | −28.2% (#17) 🔔 bottom 5: short |
| **ENA** | below (−17.1%) | +79.6% to high / −9.4% to low | −33.8% (#20) 🔔 bottom 5: short |
| **DOGE** | below (−11.0%) | +36.1% to high / −7.5% to low | −20.7% (#9) |
| **SUI** | below (−13.5%) | +30.7% to high / −8.5% to low | −18.1% (#7) |
| **BNB** | below (−5.4%) | +27.8% to high / −4.7% to low | −16.3% (#5) 🔔 top 5: long |
| **GRAM** | below (−12.7%) | +20.2% to high / −7.7% to low | −11.8% (#3) 🔔 top 5: long |
| **VVV** | below (−10.3%) | +28.8% to high / −18.5% to low | −10.7% (#2) 🔔 top 5: long |
| **WLD** | below (−23.0%) | +66.8% to high / −10.6% to low | −30.8% (#19) 🔔 bottom 5: short |
| **AAVE** | below (−14.4%) | +28.4% to high / −11.6% to low | −18.5% (#8) |
| **ZRO** | below (−9.1%) | +38.6% to high / −5.2% to low | −22.4% (#12) |

_Momentum trades its top/bottom 5 at the Monday rebalance; MA and breakout act at each daily run. Spot uses the same signals but only buys: a short signal just sells what it holds._

### This week's coins (chosen 2026-11-16)

HYPE · ZEC · SOL · XRP · NEAR · kPEPE · XMR · PUMP · LIT · AVAX · UNI · ENA · DOGE · SUI · BNB · GRAM · VVV · WLD · AAVE · ZRO

_The 20 most-traded Hyperliquid futures over the past week, excluding BTC and ETH. Refreshed Mondays 00:00 UTC (5:00 AM PKT)._

## Alpaca paper account

Value **$49,519.57** · cash $46,504.43 · account ending YUU8  
Holding: 70.1872 AVAXUSD (+$0.30), 2 MU (−$385.10), 7e-09 PEPEUSD ($0.00)

**1** simulated spot trade(s) copied and open. Copies use the same number of coins as the simulation, with a real stop order on Alpaca.

Crypto spot bot: no coins on its watchlist yet (daily 00:15 UTC). Stock bot: stopped.

---
✅ Last run OK · [futures log](logs/futures_bot.log) · [spot log](logs/spot_bot.log) · [project log](PROJECT_LOG.md) · on the PC: `python dashboard.py`

<sub>This page is written by summary.py; edits by hand are overwritten.</sub>
