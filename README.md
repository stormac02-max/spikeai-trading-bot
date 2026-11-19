# SpikeAI paper trading

_Updated **Thu 19 Nov 2026, 12:30 PKT** (Thu 02:30 ET). Refreshed after every daily run. Paper trading only: no real money._

## Strategy test: MA crossover vs breakout vs momentum

**38 days left** in the evaluation (until 2026-12-27), then the best strategy is kept.  
Each simulated account started with $10,000. Futures: 2x, long and short, $500 margin per trade. Spot: 1x, buy-only, $500 per buy, copied to Alpaca for coins it lists. Both use an 8% stop.

### Futures

| Strategy | Value | Return | Below peak | Open | Closed (won) | Fees | Funding |
|---|--:|--:|--:|--:|--:|--:|--:|
| 🔵 MA crossover 20/50 | **$10,768.11** | +7.68% | −1.03% | 4 | 0 | $1.80 | +$0.58 |
| 🟠 Breakout 20/10 | **$11,789.37** | +17.89% | −2.30% | 15 | 7 (2) | $13.02 | +$11.14 |
| 🟢 Momentum 14d, 5 long/5 short | **$10,711.00** | +7.11% | −0.01% | 8 | 17 (6) | $18.24 | −$4.93 |

**Futures leader:** 🟠 Breakout 20/10, $1,021.26 ahead of MA crossover 20/50.

### Spot

| Strategy | Value | Return | Below peak | Held | Closed (won) | Fees | On Alpaca |
|---|--:|--:|--:|--:|--:|--:|--:|
| 🔵 MA crossover 20/50 | **$10,000.00** | 0.00% | at peak | 0 | 0 | $0.00 | 0 |
| 🟠 Breakout 20/10 | **$10,000.00** | 0.00% | at peak | 0 | 0 | $0.00 | 0 |
| 🟢 Momentum 14d, 5 long/5 short | **$9,874.21** | −1.26% | −1.26% | 4 | 9 (0) | $26.57 | 1 |

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
| now | $10,768.11 | $11,789.37 | $10,711.00 | $10,000.00 | $10,000.00 | $9,874.21 |

</details>

### Open positions

| Strategy | Coin | Side | Entry → now | Profit | To stop | To liquidation / Alpaca |
|---|---|---|---|--:|--:|--:|
| 🔵 MA | **SUI** | ▼ Short | 0.89681 → 0.72641 | +$190.01 (+37.9%) | ✅ 33.3% | ✅ 76.5% |
| 🔵 MA | **WLD** | ▼ Short | 0.38553 → 0.26322 | +$317.25 (+64.2%) | ✅ 58.2% | ✅ 108.4% |
| 🔵 MA | **NEAR** | ▼ Short | 4.0459 → 3.4122 | +$156.63 (+31.2%) | ✅ 28.1% | ✅ 69.7% |
| 🔵 MA | **ZRO** | ▼ Short | 1.6048 → 1.4356 | +$105.45 (+21.0%) | ✅ 20.7% | ✅ 52.7% |
| 🟠 Breakout | **SOL** | ▼ Short | 91.244 → 74.747 | +$180.80 (+36.1%) | ✅ 31.8% | ✅ 78.7% |
| 🟠 Breakout | **NEAR** | ▼ Short | 3.6822 → 3.4122 | +$73.33 (+14.6%) | ✅ 16.5% | ✅ 54.4% |
| 🟠 Breakout | **ENA** | ▼ Short | 0.1646 → 0.11119 | +$324.48 (+64.6%) | ✅ 59.9% | ✅ 111.8% |
| 🟠 Breakout | **WLD** | ▼ Short | 0.34441 → 0.26322 | +$235.75 (+47.6%) | ✅ 41.3% | ✅ 86.3% |
| 🟠 Breakout | **XRP** | ▼ Short | 1.1619 → 0.98 | +$156.55 (+31.3%) | ✅ 28.0% | ✅ 73.5% |
| 🟠 Breakout | **PUMP** | ▼ Short | 0.003674 → 0.002674 | +$272.18 (+54.3%) | ✅ 48.4% | ✅ 96.5% |
| 🟠 Breakout | **SUI** | ▼ Short | 0.81988 → 0.72641 | +$114.01 (+22.8%) | ✅ 21.9% | ✅ 61.2% |
| 🟠 Breakout | **HYPE** | ▼ Short | 71.8649 → 68.155 | +$51.62 (+10.3%) | ✅ 13.9% | ✅ 50.8% |
| 🟠 Breakout | **ZEC** | ▼ Short | 1,003.70 → 938.02 | +$65.44 (+13.0%) | ✅ 15.6% | ✅ 53.1% |
| 🟠 Breakout | **UNI** | ▼ Short | 6.1326 → 5.1894 | +$153.80 (+30.8%) | ✅ 27.6% | ✅ 68.8% |
| 🟠 Breakout | **BNB** | ▼ Short | 632.05 → 588.65 | +$68.67 (+13.7%) | ✅ 16.0% | ✅ 53.5% |
| 🟠 Breakout | **AAVE** | ▼ Short | 111.00 → 109.18 | +$16.43 (+3.3%) | ✅ 9.8% | ✅ 45.3% |
| 🟠 Breakout | **XMR** | ▼ Short | 490.83 → 503.12 | −$25.02 (−5.0%) | ✅ 5.4% | ✅ 33.0% |
| 🟠 Breakout | **kPEPE** | ▼ Short | 0.003924 → 0.00381 | +$29.05 (+5.8%) | ✅ 11.2% | ✅ 47.2% |
| 🟠 Breakout | **ZRO** | ▼ Short | 1.4562 → 1.4356 | +$14.14 (+2.8%) | ✅ 9.5% | ✅ 38.4% |
| 🟢 Momentum | **WLD** | ▼ Short | 0.38553 → 0.26322 | +$317.25 (+64.2%) | ✅ 58.2% | ✅ 108.4% |
| 🟢 Momentum | **ENA** | ▼ Short | 0.14951 → 0.11119 | +$256.31 (+51.1%) | ✅ 45.2% | ✅ 92.3% |
| 🟢 Momentum | **BNB** | ▲ Long | 589.91 → 588.65 | −$2.13 (−0.4%) | ✅ 7.8% | ✅ 47.2% |
| 🟢 Momentum | **AVAX** | ▲ Long | 7.102 → 7.0483 | −$7.56 (−1.5%) | ✅ 7.3% | ✅ 47.0% |
| 🟢 Momentum | **GRAM** | ▲ Long | 1.0515 → 1.028 | −$22.31 (−4.5%) | ✅ 5.9% | ✅ 43.3% |
| 🟢 Momentum | **VVV** | ▲ Long | 20.0544 → 23.2876 | +$161.22 (+32.3%) | ✅ 20.8% | ✅ 48.2% |
| 🟢 Momentum | **PUMP** | ▼ Short | 0.00287 → 0.002674 | +$68.29 (+13.6%) | ✅ 15.9% | ✅ 53.4% |
| 🟢 Momentum | **UNI** | ▼ Short | 5.1601 → 5.1894 | −$5.67 (−1.1%) | ✅ 7.4% | ✅ 42.1% |
| 🟢 Momentum (spot) | **BNB** | ▲ Long | 589.82 → 587.82 | −$4.18 (−0.8%) | ✅ 7.7% | not on Alpaca |
| 🟢 Momentum (spot) | **AVAX** | ▲ Long | 7.106 → 7.042 | −$6.98 (−1.4%) | ✅ 7.2% | ✅ copied |
| 🟢 Momentum (spot) | **VVV** | ▲ Long | 20.0503 → 23.23 | +$76.40 (+15.3%) | ✅ 20.6% | not on Alpaca |
| 🟢 Momentum (spot) | **LIT** | ▲ Long | 0.07637 → 0.105 | +$184.01 (+36.8%) | ✅ 33.1% | not on Alpaca |

_Distance = how far the price can still move against the position. ✅ over 5% · ⚠️ 2–5% · 🔴 under 2%. Spot can't be liquidated; its last column shows whether the trade is copied to Alpaca._

### Recent trades

| Time (PKT) | Strategy | Coin | What | Price | Result |
|---|---|---|---|--:|--:|
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
| Mon 16 Nov, 11:36 | 🟢 Momentum | **PUMP** | Opened short | 0.00287 | fee $0.45 |

### Signal board (daily candle of 2026-11-18)

What each strategy sees per coin. 🔔 = the condition for a trade is met.

| Coin | MA: 20d vs 50d | Breakout: vs 20-day range | Momentum: 14d return |
|---|---|---|---|
| **HYPE** | below (−5.2%) | +45.2% to high / −10.7% to low | −20.2% (#8) |
| **ZEC** | below (−7.2%) | +53.2% to high / −12.3% to low | −29.6% (#16) 🔔 bottom 5: short |
| **SOL** | below (−14.3%) | +40.2% to high / −8.5% to low | −23.0% (#12) |
| **XRP** | below (−12.2%) | +38.8% to high / −7.8% to low | −25.9% (#15) |
| **NEAR** | below (−17.2%) | +43.5% to high / −13.2% to low | −17.7% (#4) 🔔 top 5: long |
| **kPEPE** | above (+4.5%) | +52.1% to high / −2.8% to low | −24.4% (#14) |
| **XMR** | above (+0.0%) | +30.3% to high / −10.2% to low | −21.3% (#9) |
| **PUMP** | below (−19.9%) | 🔔 below 20d low | −38.8% (#20) 🔔 bottom 5: short |
| **LIT** | below (−4.7%) | +31.5% to high / −14.5% to low | −18.0% (#5) 🔔 top 5: long |
| **AVAX** | below (−12.5%) | +30.6% to high / −4.2% to low | −19.5% (#7) |
| **UNI** | below (−10.2%) | +50.8% to high / −11.1% to low | −32.0% (#18) 🔔 bottom 5: short |
| **ENA** | below (−19.9%) | +94.8% to high / −1.7% to low | −38.1% (#19) 🔔 bottom 5: short |
| **DOGE** | below (−12.2%) | +38.7% to high / −5.7% to low | −23.8% (#13) |
| **SUI** | below (−13.9%) | +33.6% to high / −6.3% to low | −22.5% (#10) |
| **BNB** | below (−7.0%) | +30.7% to high / −2.9% to low | −19.1% (#6) |
| **GRAM** | below (−12.5%) | +26.2% to high / −3.1% to low | −13.2% (#2) 🔔 top 5: long |
| **VVV** | below (−10.7%) | +19.4% to high / −23.2% to low | +1.0% (#1) 🔔 top 5: long |
| **WLD** | below (−25.8%) | +70.1% to high / −7.0% to low | −30.4% (#17) 🔔 bottom 5: short |
| **AAVE** | below (−14.7%) | +28.8% to high / −11.7% to low | −17.0% (#3) 🔔 top 5: long |
| **ZRO** | below (−10.2%) | +38.4% to high / −5.3% to low | −22.8% (#11) |

_Momentum trades its top/bottom 5 at the Monday rebalance; MA and breakout act at each daily run. Spot uses the same signals but only buys: a short signal just sells what it holds._

### This week's coins (chosen 2026-11-16)

HYPE · ZEC · SOL · XRP · NEAR · kPEPE · XMR · PUMP · LIT · AVAX · UNI · ENA · DOGE · SUI · BNB · GRAM · VVV · WLD · AAVE · ZRO

_The 20 most-traded Hyperliquid futures over the past week, excluding BTC and ETH. Refreshed Mondays 00:00 UTC (5:00 AM PKT)._

## Alpaca paper account

Value **$49,488.06** · cash $46,504.43 · account ending YUU8  
Holding: 70.1872 AVAXUSD (−$2.91), 2 MU (−$413.40), 7e-09 PEPEUSD ($0.00)

**1** simulated spot trade(s) copied and open. Copies use the same number of coins as the simulation, with a real stop order on Alpaca.

Crypto spot bot: no coins on its watchlist yet (daily 00:15 UTC). Stock bot: stopped.

---
✅ Last run OK · [futures log](logs/futures_bot.log) · [spot log](logs/spot_bot.log) · [project log](PROJECT_LOG.md) · on the PC: `python dashboard.py`

<sub>This page is written by summary.py; edits by hand are overwritten.</sub>
