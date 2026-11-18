# SpikeAI paper trading

_Updated **Wed 18 Nov 2026, 12:34 PKT** (Wed 02:34 ET). Refreshed after every daily run. Paper trading only: no real money._

## Strategy test: MA crossover vs breakout vs momentum

**39 days left** in the evaluation (until 2026-12-27), then the best strategy is kept.  
Each simulated account started with $10,000. Futures: 2x, long and short, $500 margin per trade. Spot: 1x, buy-only, $500 per buy, copied to Alpaca for coins it lists. Both use an 8% stop.

### Futures

| Strategy | Value | Return | Below peak | Open | Closed (won) | Fees | Funding |
|---|--:|--:|--:|--:|--:|--:|--:|
| 🔵 MA crossover 20/50 | **$10,822.63** | +8.23% | −0.52% | 4 | 0 | $1.80 | +$0.23 |
| 🟠 Breakout 20/10 | **$11,787.97** | +17.88% | −2.31% | 15 | 7 (2) | $13.02 | +$8.97 |
| 🟢 Momentum 14d, 5 long/5 short | **$10,655.27** | +6.55% | at peak | 8 | 17 (6) | $18.24 | −$4.52 |

**Futures leader:** 🟠 Breakout 20/10, $965.34 ahead of MA crossover 20/50.

### Spot

| Strategy | Value | Return | Below peak | Held | Closed (won) | Fees | On Alpaca |
|---|--:|--:|--:|--:|--:|--:|--:|
| 🔵 MA crossover 20/50 | **$10,000.00** | 0.00% | at peak | 0 | 0 | $0.00 | 0 |
| 🟠 Breakout 20/10 | **$10,000.00** | 0.00% | at peak | 0 | 0 | $0.00 | 0 |
| 🟢 Momentum 14d, 5 long/5 short | **$9,820.39** | −1.80% | −1.80% | 4 | 9 (0) | $26.57 | 1 |

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
| now | $10,822.63 | $11,787.97 | $10,655.27 | $10,000.00 | $10,000.00 | $9,820.39 |

</details>

### Open positions

| Strategy | Coin | Side | Entry → now | Profit | To stop | To liquidation / Alpaca |
|---|---|---|---|--:|--:|--:|
| 🔵 MA | **SUI** | ▼ Short | 0.89681 → 0.73125 | +$184.61 (+36.8%) | ✅ 32.5% | ✅ 75.4% |
| 🔵 MA | **WLD** | ▼ Short | 0.38553 → 0.2639 | +$315.49 (+63.8%) | ✅ 57.8% | ✅ 107.9% |
| 🔵 MA | **NEAR** | ▼ Short | 4.0459 → 3.3714 | +$166.71 (+33.2%) | ✅ 29.6% | ✅ 71.7% |
| 🔵 MA | **ZRO** | ▼ Short | 1.6048 → 1.3522 | +$157.39 (+31.3%) | ✅ 28.2% | ✅ 62.1% |
| 🟠 Breakout | **SOL** | ▼ Short | 91.244 → 74.875 | +$179.40 (+35.8%) | ✅ 31.6% | ✅ 78.4% |
| 🟠 Breakout | **NEAR** | ▼ Short | 3.6822 → 3.3714 | +$84.41 (+16.8%) | ✅ 18.0% | ✅ 56.3% |
| 🟠 Breakout | **ENA** | ▼ Short | 0.1646 → 0.11303 | +$313.28 (+62.4%) | ✅ 57.3% | ✅ 108.3% |
| 🟠 Breakout | **WLD** | ▼ Short | 0.34441 → 0.2639 | +$233.77 (+47.2%) | ✅ 41.0% | ✅ 85.8% |
| 🟠 Breakout | **XRP** | ▼ Short | 1.1619 → 0.99244 | +$145.85 (+29.2%) | ✅ 26.4% | ✅ 71.3% |
| 🟠 Breakout | **PUMP** | ▼ Short | 0.003674 → 0.002656 | +$277.08 (+55.3%) | ✅ 49.4% | ✅ 97.8% |
| 🟠 Breakout | **SUI** | ▼ Short | 0.81988 → 0.73125 | +$108.10 (+21.6%) | ✅ 21.1% | ✅ 60.1% |
| 🟠 Breakout | **HYPE** | ▼ Short | 71.8649 → 68.794 | +$42.73 (+8.5%) | ✅ 12.8% | ✅ 49.4% |
| 🟠 Breakout | **ZEC** | ▼ Short | 1,003.70 → 952.65 | +$50.86 (+10.1%) | ✅ 13.8% | ✅ 50.7% |
| 🟠 Breakout | **UNI** | ▼ Short | 6.1326 → 5.2221 | +$148.47 (+29.7%) | ✅ 26.8% | ✅ 67.7% |
| 🟠 Breakout | **BNB** | ▼ Short | 632.05 → 592.16 | +$63.12 (+12.6%) | ✅ 15.3% | ✅ 52.6% |
| 🟠 Breakout | **AAVE** | ▼ Short | 111.00 → 111.09 | −$0.78 (−0.2%) | ✅ 7.9% | ✅ 42.8% |
| 🟠 Breakout | **XMR** | ▼ Short | 490.83 → 505.19 | −$29.25 (−5.9%) | ⚠️ 4.9% | ✅ 32.4% |
| 🟠 Breakout | **kPEPE** | ▼ Short | 0.003924 → 0.003753 | +$43.58 (+8.7%) | ✅ 12.9% | ✅ 49.4% |
| 🟠 Breakout | **ZRO** | ▼ Short | 1.4562 → 1.3522 | +$71.39 (+14.3%) | ✅ 16.3% | ✅ 46.9% |
| 🟢 Momentum | **WLD** | ▼ Short | 0.38553 → 0.2639 | +$315.49 (+63.8%) | ✅ 57.8% | ✅ 107.9% |
| 🟢 Momentum | **ENA** | ▼ Short | 0.14951 → 0.11303 | +$243.98 (+48.7%) | ✅ 42.9% | ✅ 89.1% |
| 🟢 Momentum | **BNB** | ▲ Long | 589.91 → 592.16 | +$3.82 (+0.8%) | ✅ 8.4% | ✅ 47.5% |
| 🟢 Momentum | **AVAX** | ▲ Long | 7.102 → 7.1673 | +$9.19 (+1.8%) | ✅ 8.8% | ✅ 47.9% |
| 🟢 Momentum | **GRAM** | ▲ Long | 1.0515 → 1.0734 | +$20.86 (+4.2%) | ✅ 9.9% | ✅ 45.7% |
| 🟢 Momentum | **VVV** | ▲ Long | 20.0544 → 21.1249 | +$53.38 (+10.7%) | ✅ 12.7% | ✅ 42.9% |
| 🟢 Momentum | **PUMP** | ▼ Short | 0.00287 → 0.002656 | +$74.56 (+14.9%) | ✅ 16.7% | ✅ 54.4% |
| 🟢 Momentum | **UNI** | ▼ Short | 5.1601 → 5.2221 | −$12.02 (−2.4%) | ✅ 6.7% | ✅ 41.2% |
| 🟢 Momentum (spot) | **BNB** | ▲ Long | 589.82 → 591.59 | −$1.00 (−0.2%) | ✅ 8.3% | not on Alpaca |
| 🟢 Momentum (spot) | **AVAX** | ▲ Long | 7.106 → 7.168 | +$1.84 (+0.4%) | ✅ 8.8% | ✅ copied |
| 🟢 Momentum (spot) | **VVV** | ▲ Long | 20.0503 → 21.055 | +$22.43 (+4.5%) | ✅ 12.4% | not on Alpaca |
| 🟢 Momentum (spot) | **LIT** | ▲ Long | 0.07637 → 0.1032 | +$172.28 (+34.5%) | ✅ 31.9% | not on Alpaca |

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

### Signal board (daily candle of 2026-11-17)

What each strategy sees per coin. 🔔 = the condition for a trade is met.

| Coin | MA: 20d vs 50d | Breakout: vs 20-day range | Momentum: 14d return |
|---|---|---|---|
| **HYPE** | below (−4.2%) | +38.7% to high / −14.7% to low | −17.7% (#9) |
| **ZEC** | below (−6.7%) | +44.5% to high / −17.3% to low | −20.6% (#13) |
| **SOL** | below (−14.0%) | +38.2% to high / −10.4% to low | −19.0% (#10) |
| **XRP** | below (−11.8%) | +36.7% to high / −9.3% to low | −23.0% (#15) |
| **NEAR** | below (−17.0%) | +41.9% to high / −15.6% to low | −11.4% (#4) 🔔 top 5: long |
| **kPEPE** | above (+5.2%) | +49.3% to high / −3.8% to low | −21.4% (#14) |
| **XMR** | above (+0.8%) | +29.6% to high / −10.7% to low | −19.4% (#11) |
| **PUMP** | below (−19.6%) | +65.2% to high / −3.4% to low | −34.9% (#20) 🔔 bottom 5: short |
| **LIT** | below (−5.4%) | +23.7% to high / −19.7% to low | −13.8% (#5) 🔔 top 5: long |
| **AVAX** | below (−12.6%) | +25.8% to high / −7.7% to low | −14.3% (#6) |
| **UNI** | below (−10.2%) | +47.1% to high / −13.3% to low | −26.4% (#17) 🔔 bottom 5: short |
| **ENA** | below (−19.3%) | +84.5% to high / −6.9% to low | −32.4% (#19) 🔔 bottom 5: short |
| **DOGE** | below (−11.9%) | +35.5% to high / −7.8% to low | −20.1% (#12) |
| **SUI** | below (−13.9%) | +30.5% to high / −8.7% to low | −17.4% (#8) |
| **BNB** | below (−6.6%) | +27.6% to high / −5.3% to low | −14.5% (#7) |
| **GRAM** | below (−12.6%) | +19.6% to high / −8.1% to low | −8.2% (#2) 🔔 top 5: long |
| **VVV** | below (−11.0%) | +24.2% to high / −20.9% to low | −6.8% (#1) 🔔 top 5: long |
| **WLD** | below (−25.1%) | +67.6% to high / −10.1% to low | −28.5% (#18) 🔔 bottom 5: short |
| **AAVE** | below (−15.0%) | +25.0% to high / −14.2% to low | −11.4% (#3) 🔔 top 5: long |
| **ZRO** | below (−10.2%) | +36.9% to high / −6.3% to low | −24.0% (#16) 🔔 bottom 5: short |

_Momentum trades its top/bottom 5 at the Monday rebalance; MA and breakout act at each daily run. Spot uses the same signals but only buys: a short signal just sells what it holds._

### This week's coins (chosen 2026-11-16)

HYPE · ZEC · SOL · XRP · NEAR · kPEPE · XMR · PUMP · LIT · AVAX · UNI · ENA · DOGE · SUI · BNB · GRAM · VVV · WLD · AAVE · ZRO

_The 20 most-traded Hyperliquid futures over the past week, excluding BTC and ETH. Refreshed Mondays 00:00 UTC (5:00 AM PKT)._

## Alpaca paper account

Value **$49,500.48** · cash $46,504.43 · account ending YUU8  
Holding: 70.1872 AVAXUSD (+$6.97), 2 MU (−$410.86), 7e-09 PEPEUSD ($0.00)

**1** simulated spot trade(s) copied and open. Copies use the same number of coins as the simulation, with a real stop order on Alpaca.

Crypto spot bot: no coins on its watchlist yet (daily 00:15 UTC). Stock bot: stopped.

---
✅ Last run OK · [futures log](logs/futures_bot.log) · [spot log](logs/spot_bot.log) · [project log](PROJECT_LOG.md) · on the PC: `python dashboard.py`

<sub>This page is written by summary.py; edits by hand are overwritten.</sub>
