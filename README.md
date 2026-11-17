# SpikeAI paper trading

_Updated **Tue 17 Nov 2026, 12:59 PKT** (Tue 02:59 ET). Refreshed after every daily run. Paper trading only: no real money._

## Strategy test: MA crossover vs breakout vs momentum

**40 days left** in the evaluation (until 2026-12-27), then the best strategy is kept.  
Each simulated account started with $10,000. Futures: 2x, long and short, $500 margin per trade. Spot: 1x, buy-only, $500 per buy, copied to Alpaca for coins it lists. Both use an 8% stop.

### Futures

| Strategy | Value | Return | Below peak | Open | Closed (won) | Fees | Funding |
|---|--:|--:|--:|--:|--:|--:|--:|
| 🔵 MA crossover 20/50 | **$10,755.09** | +7.55% | −1.15% | 4 | 0 | $1.80 | −$0.25 |
| 🟠 Breakout 20/10 | **$11,661.38** | +16.61% | −3.36% | 15 | 7 (2) | $13.02 | +$7.25 |
| 🟢 Momentum 14d, 5 long/5 short | **$10,588.72** | +5.89% | −0.42% | 9 | 16 (6) | $17.75 | −$4.43 |

**Futures leader:** 🟠 Breakout 20/10, $906.28 ahead of MA crossover 20/50.

### Spot

| Strategy | Value | Return | Below peak | Held | Closed (won) | Fees | On Alpaca |
|---|--:|--:|--:|--:|--:|--:|--:|
| 🔵 MA crossover 20/50 | **$10,000.00** | 0.00% | at peak | 0 | 0 | $0.00 | 0 |
| 🟠 Breakout 20/10 | **$10,000.00** | 0.00% | at peak | 0 | 0 | $0.00 | 0 |
| 🟢 Momentum 14d, 5 long/5 short | **$9,678.18** | −3.22% | −3.22% | 4 | 9 (0) | $26.57 | 1 |

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
| now | $10,755.09 | $11,661.38 | $10,588.72 | $10,000.00 | $10,000.00 | $9,678.18 |

</details>

### Open positions

| Strategy | Coin | Side | Entry → now | Profit | To stop | To liquidation / Alpaca |
|---|---|---|---|--:|--:|--:|
| 🔵 MA | **SUI** | ▼ Short | 0.89681 → 0.72445 | +$192.19 (+38.3%) | ✅ 33.7% | ✅ 77.0% |
| 🔵 MA | **WLD** | ▼ Short | 0.38553 → 0.26691 | +$307.68 (+62.2%) | ✅ 56.0% | ✅ 105.6% |
| 🔵 MA | **NEAR** | ▼ Short | 4.0459 → 3.2592 | +$194.44 (+38.7%) | ✅ 34.1% | ✅ 77.6% |
| 🔵 MA | **ZRO** | ▼ Short | 1.6048 → 1.504 | +$62.83 (+12.5%) | ✅ 15.2% | ✅ 45.7% |
| 🟠 Breakout | **SOL** | ▼ Short | 91.244 → 72.865 | +$201.43 (+40.2%) | ✅ 35.2% | ✅ 83.4% |
| 🟠 Breakout | **NEAR** | ▼ Short | 3.6822 → 3.2592 | +$114.88 (+22.9%) | ✅ 22.0% | ✅ 61.6% |
| 🟠 Breakout | **ENA** | ▼ Short | 0.1646 → 0.11651 | +$292.16 (+58.2%) | ✅ 52.6% | ✅ 102.0% |
| 🟠 Breakout | **WLD** | ▼ Short | 0.34441 → 0.26691 | +$225.03 (+45.5%) | ✅ 39.4% | ✅ 83.7% |
| 🟠 Breakout | **XRP** | ▼ Short | 1.1619 → 0.96105 | +$172.86 (+34.6%) | ✅ 30.6% | ✅ 76.9% |
| 🟠 Breakout | **PUMP** | ▼ Short | 0.003674 → 0.002779 | +$243.60 (+48.6%) | ✅ 42.8% | ✅ 89.0% |
| 🟠 Breakout | **SUI** | ▼ Short | 0.81988 → 0.72445 | +$116.40 (+23.3%) | ✅ 22.2% | ✅ 61.6% |
| 🟠 Breakout | **HYPE** | ▼ Short | 71.8649 → 69.346 | +$35.05 (+7.0%) | ✅ 11.9% | ✅ 48.2% |
| 🟠 Breakout | **ZEC** | ▼ Short | 1,003.70 → 925.28 | +$78.13 (+15.6%) | ✅ 17.2% | ✅ 55.1% |
| 🟠 Breakout | **UNI** | ▼ Short | 6.1326 → 5.3056 | +$134.85 (+27.0%) | ✅ 24.8% | ✅ 65.1% |
| 🟠 Breakout | **BNB** | ▼ Short | 632.05 → 593.09 | +$61.65 (+12.3%) | ✅ 15.1% | ✅ 52.3% |
| 🟠 Breakout | **AAVE** | ▼ Short | 111.00 → 113.13 | −$19.16 (−3.8%) | ✅ 6.0% | ✅ 40.2% |
| 🟠 Breakout | **XMR** | ▼ Short | 490.83 → 502.27 | −$23.30 (−4.7%) | ✅ 5.5% | ✅ 33.2% |
| 🟠 Breakout | **kPEPE** | ▼ Short | 0.003924 → 0.003899 | +$6.37 (+1.3%) | ✅ 8.7% | ✅ 43.8% |
| 🟠 Breakout | **ZRO** | ▼ Short | 1.4562 → 1.504 | −$32.82 (−6.6%) | ⚠️ 4.6% | ✅ 32.1% |
| 🟢 Momentum | **WLD** | ▼ Short | 0.38553 → 0.26691 | +$307.68 (+62.2%) | ✅ 56.0% | ✅ 105.6% |
| 🟢 Momentum | **ENA** | ▼ Short | 0.14951 → 0.11651 | +$220.73 (+44.1%) | ✅ 38.6% | ✅ 83.4% |
| 🟢 Momentum | **BNB** | ▲ Long | 589.91 → 593.09 | +$5.40 (+1.1%) | ✅ 8.5% | ✅ 47.6% |
| 🟢 Momentum | **AVAX** | ▲ Long | 7.102 → 7.1937 | +$12.91 (+2.6%) | ✅ 9.2% | ✅ 48.0% |
| 🟢 Momentum | **GRAM** | ▲ Long | 1.0515 → 1.0332 | −$17.37 (−3.5%) | ✅ 6.4% | ✅ 43.6% |
| 🟢 Momentum | **VVV** | ▲ Long | 20.0544 → 21.517 | +$72.93 (+14.6%) | ✅ 14.3% | ✅ 44.0% |
| 🟢 Momentum | **PUMP** | ▼ Short | 0.00287 → 0.002779 | +$31.71 (+6.3%) | ✅ 11.5% | ✅ 47.5% |
| 🟢 Momentum | **UNI** | ▼ Short | 5.1601 → 5.3056 | −$28.20 (−5.6%) | ✅ 5.0% | ✅ 38.9% |
| 🟢 Momentum | **ZEC** | ▼ Short | 886.59 → 925.28 | −$43.64 (−8.7%) | ⚠️ 3.5% | ✅ 36.9% |
| 🟢 Momentum (spot) | **BNB** | ▲ Long | 589.82 → 592.73 | −$0.04 (−0.0%) | ✅ 8.5% | not on Alpaca |
| 🟢 Momentum (spot) | **AVAX** | ▲ Long | 7.106 → 7.192 | +$3.52 (+0.7%) | ✅ 9.1% | ✅ copied |
| 🟢 Momentum (spot) | **VVV** | ▲ Long | 20.0503 → 21.454 | +$32.33 (+6.5%) | ✅ 14.0% | not on Alpaca |
| 🟢 Momentum (spot) | **LIT** | ▲ Long | 0.07637 → 0.0795 | +$17.89 (+3.6%) | ✅ 11.6% | not on Alpaca |

_Distance = how far the price can still move against the position. ✅ over 5% · ⚠️ 2–5% · 🔴 under 2%. Spot can't be liquidated; its last column shows whether the trade is copied to Alpaca._

### Recent trades

| Time (PKT) | Strategy | Coin | What | Price | Result |
|---|---|---|---|--:|--:|
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
| Mon 16 Nov, 11:36 | 🟢 Momentum | **UNI** | Opened short | 5.1601 | fee $0.45 |

### Signal board (daily candle of 2026-11-16)

What each strategy sees per coin. 🔔 = the condition for a trade is met.

| Coin | MA: 20d vs 50d | Breakout: vs 20-day range | Momentum: 14d return |
|---|---|---|---|
| **HYPE** | below (−4.0%) | +39.3% to high / −14.4% to low | −17.0% (#8) |
| **ZEC** | below (−6.0%) | +54.7% to high / −11.4% to low | −20.3% (#13) |
| **SOL** | below (−13.4%) | +45.2% to high / −5.8% to low | −22.2% (#15) |
| **XRP** | below (−11.2%) | +40.8% to high / −6.6% to low | −23.6% (#16) 🔔 bottom 5: short |
| **NEAR** | below (−16.0%) | +52.6% to high / −9.3% to low | −18.3% (#11) |
| **kPEPE** | above (+6.4%) | +46.3% to high / −5.7% to low | −18.2% (#10) |
| **XMR** | above (+1.5%) | +33.4% to high / −8.2% to low | −18.3% (#12) |
| **PUMP** | below (−18.5%) | +64.2% to high / −3.9% to low | −28.6% (#18) 🔔 bottom 5: short |
| **LIT** | below (−6.3%) | +20.6% to high / −13.4% to low | −3.9% (#1) 🔔 top 5: long |
| **AVAX** | below (−12.3%) | +29.0% to high / −5.3% to low | −15.2% (#5) 🔔 top 5: long |
| **UNI** | below (−9.7%) | +51.4% to high / −10.8% to low | −27.2% (#17) 🔔 bottom 5: short |
| **ENA** | below (−18.1%) | +89.8% to high / −4.2% to low | −32.7% (#20) 🔔 bottom 5: short |
| **DOGE** | below (−11.4%) | +38.3% to high / −6.0% to low | −20.6% (#14) |
| **SUI** | below (−13.6%) | +33.9% to high / −6.3% to low | −17.5% (#9) |
| **BNB** | below (−5.9%) | +29.0% to high / −4.3% to low | −15.5% (#7) |
| **GRAM** | below (−12.6%) | +22.5% to high / −5.9% to low | −11.3% (#3) 🔔 top 5: long |
| **VVV** | below (−10.9%) | +30.0% to high / −17.7% to low | −5.0% (#2) 🔔 top 5: long |
| **WLD** | below (−24.0%) | +72.6% to high / −7.4% to low | −30.7% (#19) 🔔 bottom 5: short |
| **AAVE** | below (−14.7%) | +29.9% to high / −10.9% to low | −14.3% (#4) 🔔 top 5: long |
| **ZRO** | below (−9.5%) | +33.4% to high / −8.7% to low | −15.4% (#6) |

_Momentum trades its top/bottom 5 at the Monday rebalance; MA and breakout act at each daily run. Spot uses the same signals but only buys: a short signal just sells what it holds._

### This week's coins (chosen 2026-11-16)

HYPE · ZEC · SOL · XRP · NEAR · kPEPE · XMR · PUMP · LIT · AVAX · UNI · ENA · DOGE · SUI · BNB · GRAM · VVV · WLD · AAVE · ZRO

_The 20 most-traded Hyperliquid futures over the past week, excluding BTC and ETH. Refreshed Mondays 00:00 UTC (5:00 AM PKT)._

## Alpaca paper account

Value **$49,485.82** · cash $46,504.43 · account ending YUU8  
Holding: 70.1872 AVAXUSD (+$7.43), 2 MU (−$425.98), 7e-09 PEPEUSD ($0.00)

**1** simulated spot trade(s) copied and open. Copies use the same number of coins as the simulation, with a real stop order on Alpaca.

Crypto spot bot: no coins on its watchlist yet (daily 00:15 UTC). Stock bot: stopped.

---
✅ Last run OK · [futures log](logs/futures_bot.log) · [spot log](logs/spot_bot.log) · [project log](PROJECT_LOG.md) · on the PC: `python dashboard.py`

<sub>This page is written by summary.py; edits by hand are overwritten.</sub>
