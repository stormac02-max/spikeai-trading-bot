# SpikeAI paper trading

_Updated **Sat 21 Nov 2026, 12:14 PKT** (Sat 02:14 ET). Refreshed after every daily run. Paper trading only: no real money._

## Strategy test: MA crossover vs breakout vs momentum

**36 days left** in the evaluation (until 2026-12-27), then the best strategy is kept.  
Each simulated account started with $10,000. Futures: 2x, long and short, $500 margin per trade. Spot: 1x, buy-only, $500 per buy, copied to Alpaca for coins it lists. Both use an 8% stop.

### Futures

| Strategy | Value | Return | Below peak | Open | Closed (won) | Fees | Funding |
|---|--:|--:|--:|--:|--:|--:|--:|
| 🔵 MA crossover 20/50 | **$11,448.38** | +14.48% | −0.01% | 5 | 0 | $2.25 | −$0.88 |
| 🟠 Breakout 20/10 | **$13,730.54** | +37.31% | −0.05% | 18 | 7 (2) | $14.37 | +$10.15 |
| 🟢 Momentum 14d, 5 long/5 short | **$10,921.70** | +9.22% | at peak | 5 | 20 (6) | $19.48 | −$7.41 |

**Futures leader:** 🟠 Breakout 20/10, $2,282.16 ahead of MA crossover 20/50.

### Spot

| Strategy | Value | Return | Below peak | Held | Closed (won) | Fees | On Alpaca |
|---|--:|--:|--:|--:|--:|--:|--:|
| 🔵 MA crossover 20/50 | **$10,000.00** | 0.00% | at peak | 0 | 0 | $0.00 | 0 |
| 🟠 Breakout 20/10 | **$10,000.00** | 0.00% | at peak | 0 | 0 | $0.00 | 0 |
| 🟢 Momentum 14d, 5 long/5 short | **$9,645.85** | −3.54% | −3.54% | 2 | 11 (0) | $28.87 | 0 |

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
| now | $11,448.38 | $13,730.54 | $10,921.70 | $10,000.00 | $10,000.00 | $9,645.85 |

</details>

### Open positions

| Strategy | Coin | Side | Entry → now | Profit | To stop | To liquidation / Alpaca |
|---|---|---|---|--:|--:|--:|
| 🔵 MA | **SUI** | ▼ Short | 0.89681 → 0.62265 | +$305.71 (+61.0%) | ✅ 55.6% | ✅ 105.9% |
| 🔵 MA | **WLD** | ▼ Short | 0.38553 → 0.22044 | +$428.22 (+86.9%) | ✅ 88.9% | ✅ 148.7% |
| 🔵 MA | **NEAR** | ▼ Short | 4.0459 → 2.694 | +$334.14 (+66.5%) | ✅ 62.2% | ✅ 114.9% |
| 🔵 MA | **ZRO** | ▼ Short | 1.6048 → 1.1265 | +$298.05 (+59.3%) | ✅ 53.9% | ✅ 94.6% |
| 🔵 MA | **XMR** | ▼ Short | 479.04 → 438.13 | +$85.39 (+17.1%) | ✅ 18.1% | ✅ 49.1% |
| 🟠 Breakout | **SOL** | ▼ Short | 91.244 → 67.87 | +$256.17 (+51.2%) | ✅ 45.2% | ✅ 96.8% |
| 🟠 Breakout | **NEAR** | ▼ Short | 3.6822 → 2.694 | +$268.37 (+53.4%) | ✅ 47.6% | ✅ 95.6% |
| 🟠 Breakout | **ENA** | ▼ Short | 0.1646 → 0.094629 | +$425.09 (+84.6%) | ✅ 87.9% | ✅ 148.9% |
| 🟠 Breakout | **WLD** | ▼ Short | 0.34441 → 0.22044 | +$359.96 (+72.9%) | ✅ 68.7% | ✅ 122.2% |
| 🟠 Breakout | **XRP** | ▼ Short | 1.1619 → 0.89869 | +$226.53 (+45.3%) | ✅ 39.6% | ✅ 89.2% |
| 🟠 Breakout | **PUMP** | ▼ Short | 0.003674 → 0.002291 | +$376.43 (+75.0%) | ✅ 73.2% | ✅ 129.4% |
| 🟠 Breakout | **SUI** | ▼ Short | 0.81988 → 0.62265 | +$240.56 (+48.2%) | ✅ 42.2% | ✅ 88.0% |
| 🟠 Breakout | **HYPE** | ▼ Short | 71.8649 → 58.586 | +$184.78 (+36.8%) | ✅ 32.5% | ✅ 75.5% |
| 🟠 Breakout | **ZEC** | ▼ Short | 1,003.70 → 733.60 | +$269.10 (+53.6%) | ✅ 47.8% | ✅ 95.8% |
| 🟠 Breakout | **UNI** | ▼ Short | 6.1326 → 4.437 | +$276.50 (+55.3%) | ✅ 49.3% | ✅ 97.4% |
| 🟠 Breakout | **BNB** | ▼ Short | 632.05 → 527.20 | +$165.89 (+33.1%) | ✅ 29.5% | ✅ 71.4% |
| 🟠 Breakout | **AAVE** | ▼ Short | 111.00 → 95.226 | +$142.13 (+28.4%) | ✅ 25.9% | ✅ 66.6% |
| 🟠 Breakout | **XMR** | ▼ Short | 490.83 → 438.13 | +$107.36 (+21.5%) | ✅ 21.0% | ✅ 52.8% |
| 🟠 Breakout | **kPEPE** | ▼ Short | 0.003924 → 0.003331 | +$151.12 (+30.2%) | ✅ 27.2% | ✅ 68.3% |
| 🟠 Breakout | **ZRO** | ▼ Short | 1.4562 → 1.1265 | +$226.41 (+45.2%) | ✅ 39.6% | ✅ 76.4% |
| 🟠 Breakout | **AVAX** | ▼ Short | 6.3055 → 6.311 | −$0.87 (−0.2%) | ✅ 7.9% | ✅ 42.7% |
| 🟠 Breakout | **DOGE** | ▼ Short | 0.053331 → 0.053358 | −$0.51 (−0.1%) | ✅ 7.9% | ✅ 42.8% |
| 🟠 Breakout | **GRAM** | ▼ Short | 0.91872 → 0.919 | −$0.30 (−0.1%) | ✅ 8.0% | ✅ 36.3% |
| 🟢 Momentum | **WLD** | ▼ Short | 0.38553 → 0.22044 | +$428.22 (+86.9%) | ✅ 88.9% | ✅ 148.7% |
| 🟢 Momentum | **ENA** | ▼ Short | 0.14951 → 0.094629 | +$367.08 (+73.2%) | ✅ 70.6% | ✅ 126.0% |
| 🟢 Momentum | **VVV** | ▲ Long | 20.0544 → 21.7119 | +$82.65 (+16.6%) | ✅ 15.0% | ✅ 44.2% |
| 🟢 Momentum | **PUMP** | ▼ Short | 0.00287 → 0.002291 | +$201.74 (+40.3%) | ✅ 35.3% | ✅ 79.1% |
| 🟢 Momentum | **UNI** | ▼ Short | 5.1601 → 4.437 | +$140.14 (+28.0%) | ✅ 25.6% | ✅ 66.2% |
| 🟢 Momentum (spot) | **VVV** | ▲ Long | 20.0503 → 21.617 | +$36.38 (+7.3%) | ✅ 14.7% | not on Alpaca |
| 🟢 Momentum (spot) | **LIT** | ▲ Long | 0.07637 → 0.0878 | +$71.96 (+14.4%) | ✅ 20.0% | not on Alpaca |

_Distance = how far the price can still move against the position. ✅ over 5% · ⚠️ 2–5% · 🔴 under 2%. Spot can't be liquidated; its last column shows whether the trade is copied to Alpaca._

### Recent trades

| Time (PKT) | Strategy | Coin | What | Price | Result |
|---|---|---|---|--:|--:|
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
| Mon 16 Nov, 11:36 | 🟠 Breakout | **XPL** | Closed | 0.042901 | +$318.85 |
| Mon 16 Nov, 11:36 | 🟠 Breakout | **TRUMP** | Closed | 0.93689 | +$1.64 |
| Mon 16 Nov, 11:36 | 🟠 Breakout | **LINK** | Closed | 9.099 | −$2.15 |

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
