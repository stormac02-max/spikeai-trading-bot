# SpikeAI paper trading

_Updated **Sun 22 Nov 2026, 11:54 PKT** (Sun 01:54 ET). Refreshed after every daily run. Paper trading only: no real money._

## Strategy test: MA crossover vs breakout vs momentum

**35 days left** in the evaluation (until 2026-12-27), then the best strategy is kept.  
Each simulated account started with $10,000. Futures: 2x, long and short, $500 margin per trade. Spot: 1x, buy-only, $500 per buy, copied to Alpaca for coins it lists. Both use an 8% stop.

### Futures

| Strategy | Value | Return | Below peak | Open | Closed (won) | Fees | Funding |
|---|--:|--:|--:|--:|--:|--:|--:|
| 🔵 MA crossover 20/50 | **$11,252.19** | +12.52% | −1.72% | 5 | 0 | $2.25 | −$0.82 |
| 🟠 Breakout 20/10 | **$13,270.64** | +32.71% | −3.40% | 19 | 7 (2) | $14.82 | +$8.06 |
| 🟢 Momentum 14d, 5 long/5 short | **$11,002.77** | +10.03% | −0.01% | 5 | 20 (6) | $19.48 | −$8.71 |

**Futures leader:** 🟠 Breakout 20/10, $2,018.45 ahead of MA crossover 20/50.

### Spot

| Strategy | Value | Return | Below peak | Held | Closed (won) | Fees | On Alpaca |
|---|--:|--:|--:|--:|--:|--:|--:|
| 🔵 MA crossover 20/50 | **$10,000.00** | 0.00% | at peak | 0 | 0 | $0.00 | 0 |
| 🟠 Breakout 20/10 | **$9,998.52** | −0.01% | −0.01% | 1 | 0 | $1.25 | 0 |
| 🟢 Momentum 14d, 5 long/5 short | **$9,612.09** | −3.88% | −3.88% | 1 | 12 (0) | $30.02 | 0 |

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
| 2026-11-20 | $11,449.50 | $13,737.30 | $10,920.02 | $10,000.00 | $10,000.00 | $9,645.85 |
| 2026-11-21 | $11,254.31 | $13,278.13 | $11,004.09 | $10,000.00 | $9,998.52 | $9,612.09 |
| now | $11,252.19 | $13,270.64 | $11,002.77 | $10,000.00 | $9,998.52 | $9,612.09 |

</details>

### Open positions

| Strategy | Coin | Side | Entry → now | Profit | To stop | To liquidation / Alpaca |
|---|---|---|---|--:|--:|--:|
| 🔵 MA | **SUI** | ▼ Short | 0.89681 → 0.63978 | +$286.60 (+57.3%) | ✅ 51.4% | ✅ 100.3% |
| 🔵 MA | **WLD** | ▼ Short | 0.38553 → 0.22532 | +$415.56 (+84.4%) | ✅ 84.8% | ✅ 143.2% |
| 🔵 MA | **NEAR** | ▼ Short | 4.0459 → 2.8757 | +$289.23 (+57.6%) | ✅ 51.9% | ✅ 101.3% |
| 🔵 MA | **ZRO** | ▼ Short | 1.6048 → 1.161 | +$276.56 (+55.0%) | ✅ 49.3% | ✅ 88.9% |
| 🔵 MA | **XMR** | ▼ Short | 479.04 → 485.12 | −$12.69 (−2.5%) | ✅ 6.6% | ✅ 34.7% |
| 🟠 Breakout | **SOL** | ▼ Short | 91.244 → 69.123 | +$242.44 (+48.4%) | ✅ 42.6% | ✅ 93.2% |
| 🟠 Breakout | **NEAR** | ▼ Short | 3.6822 → 2.8757 | +$219.03 (+43.6%) | ✅ 38.3% | ✅ 83.2% |
| 🟠 Breakout | **ENA** | ▼ Short | 0.1646 → 0.098125 | +$403.85 (+80.4%) | ✅ 81.2% | ✅ 140.0% |
| 🟠 Breakout | **WLD** | ▼ Short | 0.34441 → 0.22532 | +$345.79 (+70.2%) | ✅ 65.1% | ✅ 117.3% |
| 🟠 Breakout | **XRP** | ▼ Short | 1.1619 → 0.91595 | +$211.68 (+42.3%) | ✅ 37.0% | ✅ 85.6% |
| 🟠 Breakout | **PUMP** | ▼ Short | 0.003674 → 0.00232 | +$368.54 (+73.4%) | ✅ 71.0% | ✅ 126.5% |
| 🟠 Breakout | **SUI** | ▼ Short | 0.81988 → 0.63978 | +$219.67 (+44.1%) | ✅ 38.4% | ✅ 82.9% |
| 🟠 Breakout | **HYPE** | ▼ Short | 71.8649 → 60.061 | +$164.25 (+32.7%) | ✅ 29.2% | ✅ 71.2% |
| 🟠 Breakout | **ZEC** | ▼ Short | 1,003.70 → 785.92 | +$216.98 (+43.2%) | ✅ 37.9% | ✅ 82.8% |
| 🟠 Breakout | **UNI** | ▼ Short | 6.1326 → 4.6164 | +$247.24 (+49.5%) | ✅ 43.5% | ✅ 89.7% |
| 🟠 Breakout | **BNB** | ▼ Short | 632.05 → 538.79 | +$147.56 (+29.5%) | ✅ 26.7% | ✅ 67.7% |
| 🟠 Breakout | **AAVE** | ▼ Short | 111.00 → 95.6894 | +$137.96 (+27.6%) | ✅ 25.3% | ✅ 65.8% |
| 🟠 Breakout | **XMR** | ▼ Short | 490.83 → 485.12 | +$11.64 (+2.3%) | ✅ 9.3% | ✅ 38.0% |
| 🟠 Breakout | **kPEPE** | ▼ Short | 0.003924 → 0.003335 | +$150.10 (+30.0%) | ✅ 27.1% | ✅ 68.1% |
| 🟠 Breakout | **ZRO** | ▼ Short | 1.4562 → 1.161 | +$202.72 (+40.4%) | ✅ 35.5% | ✅ 71.2% |
| 🟠 Breakout | **AVAX** | ▼ Short | 6.3055 → 6.5137 | −$33.02 (−6.6%) | ⚠️ 4.5% | ✅ 38.3% |
| 🟠 Breakout | **DOGE** | ▼ Short | 0.053331 → 0.054151 | −$15.38 (−3.1%) | ✅ 6.4% | ✅ 40.7% |
| 🟠 Breakout | **GRAM** | ▼ Short | 0.91872 → 0.94023 | −$23.41 (−4.7%) | ✅ 5.5% | ✅ 33.1% |
| 🟠 Breakout | **VVV** | ▲ Long | 24.993 → 24.9867 | −$0.25 (−0.1%) | ✅ 8.0% | ✅ 40.0% |
| 🟢 Momentum | **WLD** | ▼ Short | 0.38553 → 0.22532 | +$415.56 (+84.4%) | ✅ 84.8% | ✅ 143.2% |
| 🟢 Momentum | **ENA** | ▼ Short | 0.14951 → 0.098125 | +$343.70 (+68.5%) | ✅ 64.6% | ✅ 117.9% |
| 🟢 Momentum | **VVV** | ▲ Long | 20.0544 → 24.9867 | +$245.95 (+49.6%) | ✅ 26.2% | ✅ 51.5% |
| 🟢 Momentum | **PUMP** | ▼ Short | 0.00287 → 0.00232 | +$191.64 (+38.3%) | ✅ 33.6% | ✅ 76.8% |
| 🟢 Momentum | **UNI** | ▼ Short | 5.1601 → 4.6164 | +$105.37 (+21.1%) | ✅ 20.7% | ✅ 59.7% |
| 🟠 Breakout (spot) | **VVV** | ▲ Long | 24.9223 → 24.911 | −$2.72 (−0.5%) | ✅ 8.0% | not on Alpaca |
| 🟢 Momentum (spot) | **VVV** | ▲ Long | 20.0503 → 24.911 | +$118.11 (+23.6%) | ✅ 26.0% | not on Alpaca |

_Distance = how far the price can still move against the position. ✅ over 5% · ⚠️ 2–5% · 🔴 under 2%. Spot can't be liquidated; its last column shows whether the trade is copied to Alpaca._

### Recent trades

| Time (PKT) | Strategy | Coin | What | Price | Result |
|---|---|---|---|--:|--:|
| Sun 22 Nov, 11:54 | 🟠 Breakout | **VVV** | Opened long | 24.993 | fee $0.45 |
| Sun 22 Nov, 11:54 | 🟠 Breakout (spot) | **VVV** | Bought | 24.9223 | fee $1.25 |
| Sat 21 Nov, 20:00 | 🟢 Momentum (spot) | **LIT** | Stopped out | 0.070261 | −$42.30 |
| Sat 21 Nov, 12:14 | 🟠 Breakout | **AVAX** | Opened short | 6.3055 | fee $0.45 |
| Sat 21 Nov, 12:14 | 🟠 Breakout | **DOGE** | Opened short | 0.053331 | fee $0.45 |
| Sat 21 Nov, 12:14 | 🟠 Breakout | **GRAM** | Opened short | 0.91872 | fee $0.45 |
| Fri 20 Nov, 23:00 | 🟢 Momentum | **GRAM** | Stopped out | 0.96735 | −$79.79 |
| Fri 20 Nov, 21:00 | 🟢 Momentum | **BNB** | Stopped out | 542.71 | −$81.10 |
| Fri 20 Nov, 21:00 | 🟢 Momentum (spot) | **BNB** | Stopped out | 542.63 | −$42.30 |
| Fri 20 Nov, 20:00 | 🟢 Momentum | **AVAX** | Stopped out | 6.5338 | −$80.28 |
| Fri 20 Nov, 20:00 | 🟢 Momentum (spot) | **AVAX** | Stopped out (Alpaca: stopped on Alpaca) | 6.5375 | −$42.30 |
| Fri 20 Nov, 12:21 | 🔵 MA | **XMR** | Opened short | 479.04 | fee $0.45 |
| Tue 17 Nov, 17:00 | 🟢 Momentum | **ZEC** | Stopped out | 957.52 | −$80.13 |
| Tue 17 Nov, 08:00 | 🟠 Breakout | **VVV** | Stopped out | 21.0006 | −$79.62 |
| Mon 16 Nov, 15:00 | 🟢 Momentum | **LIT** | Stopped out | 2.4855 | −$80.38 |

### Signal board (daily candle of 2026-11-21)

What each strategy sees per coin. 🔔 = the condition for a trade is met.

| Coin | MA: 20d vs 50d | Breakout: vs 20-day range | Momentum: 14d return |
|---|---|---|---|
| **HYPE** | below (−8.1%) | +45.3% to high / −2.6% to low | −21.2% (#6) |
| **ZEC** | below (−10.3%) | +78.3% to high / −6.9% to low | −38.2% (#20) 🔔 bottom 5: short |
| **SOL** | below (−15.6%) | +39.7% to high / −4.5% to low | −21.7% (#8) |
| **XRP** | below (−13.7%) | +44.1% to high / −5.1% to low | −19.9% (#4) 🔔 top 5: long |
| **NEAR** | below (−19.7%) | +55.5% to high / −4.4% to low | −22.6% (#9) |
| **kPEPE** | above (+0.9%) | +64.9% to high / −2.2% to low | −29.8% (#15) |
| **XMR** | below (−2.3%) | +31.6% to high / −10.6% to low | −18.1% (#3) 🔔 top 5: long |
| **PUMP** | below (−22.3%) | +94.2% to high / −0.9% to low | −36.8% (#18) 🔔 bottom 5: short |
| **LIT** | below (−5.0%) | +53.1% to high / −1.8% to low | −29.4% (#14) |
| **AVAX** | below (−13.2%) | +39.5% to high / −2.8% to low | −20.0% (#5) 🔔 top 5: long |
| **UNI** | below (−12.1%) | +64.9% to high / −9.1% to low | −34.4% (#17) 🔔 bottom 5: short |
| **ENA** | below (−23.2%) | +93.6% to high / −3.4% to low | −38.0% (#19) 🔔 bottom 5: short |
| **DOGE** | below (−13.4%) | +41.7% to high / −4.9% to low | −22.8% (#10) |
| **SUI** | below (−14.9%) | +47.5% to high / −2.7% to low | −24.3% (#11) |
| **BNB** | below (−8.5%) | +31.9% to high / −3.3% to low | −21.2% (#7) |
| **GRAM** | below (−12.8%) | 🔔 below 20d low | −10.6% (#2) 🔔 top 5: long |
| **VVV** | below (−9.9%) | 🔔 above 20d high | +20.8% (#1) 🔔 top 5: long |
| **WLD** | below (−28.4%) | +77.4% to high / −1.7% to low | −31.9% (#16) 🔔 bottom 5: short |
| **AAVE** | below (−15.6%) | +44.3% to high / −3.8% to low | −25.9% (#12) |
| **ZRO** | below (−13.5%) | +66.0% to high / −3.1% to low | −28.6% (#13) |

_Momentum trades its top/bottom 5 at the Monday rebalance; MA and breakout act at each daily run. Spot uses the same signals but only buys: a short signal just sells what it holds._

### This week's coins (chosen 2026-11-16)

HYPE · ZEC · SOL · XRP · NEAR · kPEPE · XMR · PUMP · LIT · AVAX · UNI · ENA · DOGE · SUI · BNB · GRAM · VVV · WLD · AAVE · ZRO

_The 20 most-traded Hyperliquid futures over the past week, excluding BTC and ETH. Refreshed Mondays 00:00 UTC (5:00 AM PKT)._

## Alpaca paper account

Value **$49,172.90** · cash $46,961.88 · account ending YUU8  
Holding: 2 MU (−$689.84), 7e-09 PEPEUSD ($0.00)

**0** simulated spot trade(s) copied and open. Copies use the same number of coins as the simulation, with a real stop order on Alpaca.

Crypto spot bot: no coins on its watchlist yet (daily 00:15 UTC). Stock bot: stopped.

---
✅ Last run OK · [futures log](logs/futures_bot.log) · [spot log](logs/spot_bot.log) · [project log](PROJECT_LOG.md) · on the PC: `python dashboard.py`

<sub>This page is written by summary.py; edits by hand are overwritten.</sub>
