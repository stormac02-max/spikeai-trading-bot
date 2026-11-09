# SpikeAI paper trading

_Updated **Mon 09 Nov 2026, 11:40 PKT** (Mon 01:40 ET). Refreshed after every daily run. Paper trading only: no real money._

## Strategy test: MA crossover vs breakout vs momentum

**48 days left** in the evaluation (until 2026-12-27), then the best strategy is kept.  
Each simulated account started with $10,000. Futures: 2x, long and short, $500 margin per trade. Spot: 1x, buy-only, $500 per buy, copied to Alpaca for coins it lists. Both use an 8% stop.

### Futures

| Strategy | Value | Return | Below peak | Open | Closed (won) | Fees | Funding |
|---|--:|--:|--:|--:|--:|--:|--:|
| 🔵 MA crossover 20/50 | **$10,438.90** | +4.39% | −0.03% | 4 | 0 | $1.80 | −$0.28 |
| 🟠 Breakout 20/10 | **$10,432.73** | +4.33% | −0.07% | 8 | 2 (0) | $5.44 | +$2.91 |
| 🟢 Momentum 14d, 5 long/5 short | **$10,291.34** | +2.91% | −0.03% | 10 | 7 (3) | $10.59 | +$0.68 |

**Futures leader:** 🔵 MA crossover 20/50, $6.17 ahead of Breakout 20/10.

### Spot

| Strategy | Value | Return | Below peak | Held | Closed (won) | Fees | On Alpaca |
|---|--:|--:|--:|--:|--:|--:|--:|
| 🔵 MA crossover 20/50 | **$10,000.00** | 0.00% | at peak | 0 | 0 | $0.00 | 0 |
| 🟠 Breakout 20/10 | **$10,000.00** | 0.00% | at peak | 0 | 0 | $0.00 | 0 |
| 🟢 Momentum 14d, 5 long/5 short | **$9,844.28** | −1.56% | −1.56% | 5 | 4 (0) | $15.84 | 2 |

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
| now | $10,438.90 | $10,432.73 | $10,291.34 | $10,000.00 | $10,000.00 | $9,844.28 |

</details>

### Open positions

| Strategy | Coin | Side | Entry → now | Profit | To stop | To liquidation / Alpaca |
|---|---|---|---|--:|--:|--:|
| 🔵 MA | **SUI** | ▼ Short | 0.89681 → 0.82044 | +$85.16 (+17.0%) | ✅ 18.1% | ✅ 56.3% |
| 🔵 MA | **WLD** | ▼ Short | 0.38553 → 0.31786 | +$175.52 (+35.3%) | ✅ 31.0% | ✅ 73.0% |
| 🔵 MA | **NEAR** | ▼ Short | 4.0459 → 3.5535 | +$121.70 (+24.3%) | ✅ 23.0% | ✅ 62.7% |
| 🔵 MA | **ZRO** | ▼ Short | 1.6048 → 1.5108 | +$58.59 (+11.7%) | ✅ 14.7% | ✅ 44.9% |
| 🟠 Breakout | **SOL** | ▼ Short | 91.244 → 86.183 | +$55.47 (+11.1%) | ✅ 14.3% | ✅ 55.0% |
| 🟠 Breakout | **XPL** | ▼ Short | 0.062812 → 0.05155 | +$179.29 (+35.8%) | ✅ 31.6% | ✅ 74.2% |
| 🟠 Breakout | **NEAR** | ▼ Short | 3.6822 → 3.5535 | +$34.95 (+7.0%) | ✅ 11.9% | ✅ 48.1% |
| 🟠 Breakout | **ENA** | ▼ Short | 0.1646 → 0.14967 | +$90.70 (+18.1%) | ✅ 18.8% | ✅ 57.2% |
| 🟠 Breakout | **WLD** | ▼ Short | 0.34441 → 0.31786 | +$77.10 (+15.5%) | ✅ 17.0% | ✅ 54.6% |
| 🟠 Breakout | **XRP** | ▼ Short | 1.1619 → 1.0896 | +$62.23 (+12.4%) | ✅ 15.2% | ✅ 56.1% |
| 🟠 Breakout | **PUMP** | ▼ Short | 0.003674 → 0.003547 | +$34.57 (+6.9%) | ✅ 11.9% | ✅ 48.0% |
| 🟠 Breakout | **SUI** | ▼ Short | 0.81988 → 0.82044 | −$0.68 (−0.1%) | ✅ 7.9% | ✅ 42.8% |
| 🟢 Momentum | **kPEPE** | ▲ Long | 0.004845 → 0.005051 | +$42.52 (+8.5%) | ✅ 11.8% | ✅ 49.5% |
| 🟢 Momentum | **WLD** | ▼ Short | 0.38553 → 0.31786 | +$175.52 (+35.3%) | ✅ 31.0% | ✅ 73.0% |
| 🟢 Momentum | **NEAR** | ▼ Short | 4.202 → 3.5535 | +$154.33 (+30.8%) | ✅ 27.7% | ✅ 69.1% |
| 🟢 Momentum | **HYPE** | ▲ Long | 74.024 → 74.087 | +$0.85 (+0.2%) | ✅ 8.1% | ✅ 47.4% |
| 🟢 Momentum | **UNI** | ▲ Long | 6.7821 → 6.7792 | −$0.43 (−0.1%) | ✅ 8.0% | ✅ 47.3% |
| 🟢 Momentum | **ZEC** | ▲ Long | 1,221.54 → 1,223.30 | +$1.44 (+0.3%) | ✅ 8.1% | ✅ 47.4% |
| 🟢 Momentum | **XMR** | ▲ Long | 593.82 → 593.70 | −$0.20 (−0.0%) | ✅ 8.0% | ✅ 44.4% |
| 🟢 Momentum | **TRUMP** | ▼ Short | 1.1454 → 1.1461 | −$0.64 (−0.1%) | ✅ 7.9% | ✅ 42.8% |
| 🟢 Momentum | **XPL** | ▼ Short | 0.051503 → 0.05155 | −$0.92 (−0.2%) | ✅ 7.9% | ✅ 42.7% |
| 🟢 Momentum | **ENA** | ▼ Short | 0.14951 → 0.14967 | −$1.06 (−0.2%) | ✅ 7.9% | ✅ 42.7% |
| 🟢 Momentum (spot) | **PEPE** | ▲ Long | 0.0000048436 → 0.000005042 | +$17.89 (+3.6%) | ✅ 11.6% | ✅ copied |
| 🟢 Momentum (spot) | **HYPE** | ▲ Long | 74.1398 → 74.12 | −$2.63 (−0.5%) | ✅ 8.0% | 🔴 copy failed |
| 🟢 Momentum (spot) | **UNI** | ▲ Long | 6.7758 → 6.779 | −$2.26 (−0.5%) | ✅ 8.0% | ✅ copied |
| 🟢 Momentum (spot) | **ZEC** | ▲ Long | 1,222.38 → 1,221.57 | −$2.83 (−0.6%) | ✅ 7.9% | not on Alpaca |
| 🟢 Momentum (spot) | **XMR** | ▲ Long | 593.46 → 592.88 | −$2.98 (−0.6%) | ✅ 7.9% | not on Alpaca |

_Distance = how far the price can still move against the position. ✅ over 5% · ⚠️ 2–5% · 🔴 under 2%. Spot can't be liquidated; its last column shows whether the trade is copied to Alpaca._

### Recent trades

| Time (PKT) | Strategy | Coin | What | Price | Result |
|---|---|---|---|--:|--:|
| Mon 09 Nov, 11:40 | 🟢 Momentum (spot) | **UNI** | Bought | 6.7758 | fee $1.25 |
| Mon 09 Nov, 11:40 | 🟢 Momentum (spot) | **ZEC** | Bought | 1,222.38 | fee $1.25 |
| Mon 09 Nov, 11:40 | 🟢 Momentum (spot) | **XMR** | Bought | 593.46 | fee $1.25 |
| Mon 09 Nov, 11:39 | 🟠 Breakout | **TRX** | Closed | 0.31659 | −$18.25 |
| Mon 09 Nov, 11:39 | 🟠 Breakout | **SUI** | Opened short | 0.81988 | fee $0.45 |
| Mon 09 Nov, 11:39 | 🟢 Momentum | **LIT** | Closed | 3.0731 | −$33.67 |
| Mon 09 Nov, 11:39 | 🟢 Momentum | **AAVE** | Closed | 129.34 | +$31.46 |
| Mon 09 Nov, 11:39 | 🟢 Momentum | **SUI** | Closed | 0.81992 | +$83.26 |
| Mon 09 Nov, 11:39 | 🟢 Momentum | **SOL** | Closed | 86.137 | +$90.76 |
| Mon 09 Nov, 11:39 | 🟢 Momentum | **HYPE** | Opened long | 74.024 | fee $0.45 |
| Mon 09 Nov, 11:39 | 🟢 Momentum | **UNI** | Opened long | 6.7821 | fee $0.45 |
| Mon 09 Nov, 11:39 | 🟢 Momentum | **ZEC** | Opened long | 1,221.54 | fee $0.45 |
| Mon 09 Nov, 11:39 | 🟢 Momentum | **XMR** | Opened long | 593.82 | fee $0.45 |
| Mon 09 Nov, 11:39 | 🟢 Momentum | **TRUMP** | Opened short | 1.1454 | fee $0.45 |
| Mon 09 Nov, 11:39 | 🟢 Momentum | **XPL** | Opened short | 0.051503 | fee $0.45 |

### Signal board (daily candle of 2026-11-08)

What each strategy sees per coin. 🔔 = the condition for a trade is met.

| Coin | MA: 20d vs 50d | Breakout: vs 20-day range | Momentum: 14d return |
|---|---|---|---|
| **HYPE** | below (−4.5%) | +30.4% to high / −0.1% to low | −2.3% (#5) 🔔 top 5: long |
| **ZEC** | below (−4.4%) | +15.5% to high / −8.4% to low | −0.2% (#3) 🔔 top 5: long |
| **SOL** | below (−9.3%) | 🔔 below 20d low | −14.6% (#13) |
| **NEAR** | below (−7.9%) | 🔔 below 20d low | −21.9% (#16) 🔔 bottom 5: short |
| **XRP** | below (−7.6%) | 🔔 below 20d low | −14.2% (#12) |
| **XMR** | above (+5.4%) | +10.4% to high / −6.0% to low | +0.8% (#2) 🔔 top 5: long |
| **PUMP** | below (−11.1%) | 🔔 below 20d low | −16.7% (#14) |
| **LIT** | below (−12.2%) | +30.3% to high / −16.1% to low | −3.6% (#6) |
| **kPEPE** | above (+6.6%) | +15.4% to high / −19.5% to low | +15.6% (#1) 🔔 top 5: long |
| **WLD** | below (−11.0%) | 🔔 below 20d low | −30.7% (#19) 🔔 bottom 5: short |
| **ENA** | below (−11.4%) | 🔔 below 20d low | −28.2% (#17) 🔔 bottom 5: short |
| **UNI** | below (−9.9%) | +15.3% to high / −8.0% to low | −2.1% (#4) 🔔 top 5: long |
| **TRUMP** | below (−13.9%) | +69.2% to high / −2.1% to low | −31.2% (#20) 🔔 bottom 5: short |
| **XPL** | below (−15.3%) | 🔔 below 20d low | −30.2% (#18) 🔔 bottom 5: short |
| **BNB** | below (−3.3%) | +11.4% to high / −2.1% to low | −7.3% (#7) |
| **SUI** | below (−10.4%) | 🔔 below 20d low | −10.8% (#10) |
| **AAVE** | below (−10.3%) | +27.3% to high / −8.7% to low | −7.5% (#8) |
| **ZRO** | below (−2.6%) | +38.1% to high / −8.4% to low | −12.1% (#11) |
| **LINK** | below (−9.1%) | +23.1% to high / −1.3% to low | −9.1% (#9) |
| **VVV** | below (−7.6%) | +41.6% to high / −0.7% to low | −20.4% (#15) |

_Momentum trades its top/bottom 5 at the Monday rebalance; MA and breakout act at each daily run. Spot uses the same signals but only buys: a short signal just sells what it holds._

### This week's coins (chosen 2026-11-09)

HYPE · ZEC · SOL · NEAR · XRP · XMR · PUMP · LIT · kPEPE · WLD · ENA · UNI · TRUMP · XPL · BNB · SUI · AAVE · ZRO · LINK · VVV

_The 20 most-traded Hyperliquid futures over the past week, excluding BTC and ETH. Refreshed Mondays 00:00 UTC (5:00 AM PKT)._

## Alpaca paper account

Value **$49,512.85** · cash $46,097.26 · account ending YUU8  
Holding: 2 MU (−$514.12), 1.02972e+08 PEPEUSD (+$30.69), 73.6075 UNIUSD (−$1.03)

**2** simulated spot trade(s) copied and open · 🔴 1 copy error(s): see the spot log. Copies use the same number of coins as the simulation, with a real stop order on Alpaca.

Crypto spot bot: no coins on its watchlist yet (daily 00:15 UTC). Stock bot: stopped.

---
✅ Last run OK · [futures log](logs/futures_bot.log) · [spot log](logs/spot_bot.log) · [project log](PROJECT_LOG.md) · on the PC: `python dashboard.py`

<sub>This page is written by summary.py; edits by hand are overwritten.</sub>
