# SpikeAI paper trading

_Updated **Wed 11 Nov 2026, 11:30 PKT** (Wed 01:30 ET). Refreshed after every daily run. Paper trading only: no real money._

## Strategy test: MA crossover vs breakout vs momentum

**46 days left** in the evaluation (until 2026-12-27), then the best strategy is kept.  
Each simulated account started with $10,000. Futures: 2x, long and short, $500 margin per trade. Spot: 1x, buy-only, $500 per buy, copied to Alpaca for coins it lists. Both use an 8% stop.

### Futures

| Strategy | Value | Return | Below peak | Open | Closed (won) | Fees | Funding |
|---|--:|--:|--:|--:|--:|--:|--:|
| 🔵 MA crossover 20/50 | **$10,417.00** | +4.17% | −0.24% | 4 | 0 | $1.80 | +$0.88 |
| 🟠 Breakout 20/10 | **$10,474.38** | +4.74% | at peak | 11 | 2 (0) | $6.79 | +$4.89 |
| 🟢 Momentum 14d, 5 long/5 short | **$10,097.64** | +0.98% | −1.92% | 8 | 9 (3) | $11.41 | −$1.01 |

**Futures leader:** 🟠 Breakout 20/10, $57.37 ahead of MA crossover 20/50.

### Spot

| Strategy | Value | Return | Below peak | Held | Closed (won) | Fees | On Alpaca |
|---|--:|--:|--:|--:|--:|--:|--:|
| 🔵 MA crossover 20/50 | **$10,000.00** | 0.00% | at peak | 0 | 0 | $0.00 | 0 |
| 🟠 Breakout 20/10 | **$10,000.00** | 0.00% | at peak | 0 | 0 | $0.00 | 0 |
| 🟢 Momentum 14d, 5 long/5 short | **$9,752.48** | −2.48% | −2.48% | 3 | 6 (0) | $18.13 | 2 |

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
| now | $10,417.00 | $10,474.38 | $10,097.64 | $10,000.00 | $10,000.00 | $9,752.48 |

</details>

### Open positions

| Strategy | Coin | Side | Entry → now | Profit | To stop | To liquidation / Alpaca |
|---|---|---|---|--:|--:|--:|
| 🔵 MA | **SUI** | ▼ Short | 0.89681 → 0.82369 | +$81.53 (+16.2%) | ✅ 17.6% | ✅ 55.7% |
| 🔵 MA | **WLD** | ▼ Short | 0.38553 → 0.30974 | +$196.59 (+39.5%) | ✅ 34.4% | ✅ 77.5% |
| 🔵 MA | **NEAR** | ▼ Short | 4.0459 → 3.6224 | +$104.67 (+20.9%) | ✅ 20.6% | ✅ 59.7% |
| 🔵 MA | **ZRO** | ▼ Short | 1.6048 → 1.5484 | +$35.13 (+7.0%) | ✅ 11.9% | ✅ 41.4% |
| 🟠 Breakout | **SOL** | ▼ Short | 91.244 → 83.025 | +$90.08 (+18.0%) | ✅ 18.7% | ✅ 60.9% |
| 🟠 Breakout | **XPL** | ▼ Short | 0.062812 → 0.052617 | +$162.31 (+32.4%) | ✅ 28.9% | ✅ 70.7% |
| 🟠 Breakout | **NEAR** | ▼ Short | 3.6822 → 3.6224 | +$16.24 (+3.2%) | ✅ 9.8% | ✅ 45.3% |
| 🟠 Breakout | **ENA** | ▼ Short | 0.1646 → 0.15124 | +$81.13 (+16.2%) | ✅ 17.5% | ✅ 55.6% |
| 🟠 Breakout | **WLD** | ▼ Short | 0.34441 → 0.30974 | +$100.68 (+20.2%) | ✅ 20.1% | ✅ 58.7% |
| 🟠 Breakout | **XRP** | ▼ Short | 1.1619 → 1.0586 | +$88.91 (+17.8%) | ✅ 18.5% | ✅ 60.7% |
| 🟠 Breakout | **PUMP** | ▼ Short | 0.003674 → 0.00352 | +$41.92 (+8.4%) | ✅ 12.7% | ✅ 49.2% |
| 🟠 Breakout | **SUI** | ▼ Short | 0.81988 → 0.82369 | −$4.64 (−0.9%) | ✅ 7.5% | ✅ 42.2% |
| 🟠 Breakout | **HYPE** | ▼ Short | 71.8649 → 71.888 | −$0.32 (−0.1%) | ✅ 8.0% | ✅ 42.8% |
| 🟠 Breakout | **ZEC** | ▼ Short | 1,003.70 → 1,004.42 | −$0.72 (−0.1%) | ✅ 7.9% | ✅ 42.8% |
| 🟠 Breakout | **VVV** | ▼ Short | 19.0003 → 19.018 | −$0.93 (−0.2%) | ✅ 7.9% | ✅ 28.5% |
| 🟢 Momentum | **kPEPE** | ▲ Long | 0.004845 → 0.0053 | +$93.91 (+18.8%) | ✅ 15.9% | ✅ 51.8% |
| 🟢 Momentum | **WLD** | ▼ Short | 0.38553 → 0.30974 | +$196.59 (+39.5%) | ✅ 34.4% | ✅ 77.5% |
| 🟢 Momentum | **NEAR** | ▼ Short | 4.202 → 3.6224 | +$137.93 (+27.5%) | ✅ 25.3% | ✅ 65.9% |
| 🟢 Momentum | **HYPE** | ▲ Long | 74.024 → 71.888 | −$28.86 (−5.8%) | ✅ 5.3% | ✅ 45.8% |
| 🟢 Momentum | **UNI** | ▲ Long | 6.7821 → 6.5052 | −$40.83 (−8.2%) | ⚠️ 4.1% | ✅ 45.1% |
| 🟢 Momentum | **TRUMP** | ▼ Short | 1.1454 → 1.1285 | +$14.73 (+2.9%) | ✅ 9.6% | ✅ 45.0% |
| 🟢 Momentum | **XPL** | ▼ Short | 0.051503 → 0.052617 | −$21.64 (−4.3%) | ✅ 5.7% | ✅ 39.9% |
| 🟢 Momentum | **ENA** | ▼ Short | 0.14951 → 0.15124 | −$11.59 (−2.3%) | ✅ 6.8% | ✅ 41.3% |
| 🟢 Momentum (spot) | **PEPE** | ▲ Long | 0.0000048436 → 0.000005288 | +$43.15 (+8.6%) | ✅ 15.7% | ✅ copied |
| 🟢 Momentum (spot) | **HYPE** | ▲ Long | 74.1398 → 71.88 | −$17.66 (−3.5%) | ✅ 5.1% | 🔴 copy failed |
| 🟢 Momentum (spot) | **UNI** | ▲ Long | 6.7758 → 6.4966 | −$23.00 (−4.6%) | ⚠️ 4.0% | ✅ copied |

_Distance = how far the price can still move against the position. ✅ over 5% · ⚠️ 2–5% · 🔴 under 2%. Spot can't be liquidated; its last column shows whether the trade is copied to Alpaca._

### Recent trades

| Time (PKT) | Strategy | Coin | What | Price | Result |
|---|---|---|---|--:|--:|
| Wed 11 Nov, 11:29 | 🟠 Breakout | **HYPE** | Opened short | 71.8649 | fee $0.45 |
| Wed 11 Nov, 11:29 | 🟠 Breakout | **ZEC** | Opened short | 1,003.70 | fee $0.45 |
| Wed 11 Nov, 11:29 | 🟠 Breakout | **VVV** | Opened short | 19.0003 | fee $0.45 |
| Tue 10 Nov, 20:00 | 🟢 Momentum | **ZEC** | Stopped out | 1,123.82 | −$80.79 |
| Tue 10 Nov, 20:00 | 🟢 Momentum (spot) | **ZEC** | Stopped out | 1,124.59 | −$42.30 |
| Tue 10 Nov, 15:00 | 🟢 Momentum | **XMR** | Stopped out | 546.31 | −$82.08 |
| Tue 10 Nov, 15:00 | 🟢 Momentum (spot) | **XMR** | Stopped out | 545.98 | −$42.30 |
| Mon 09 Nov, 11:40 | 🟢 Momentum (spot) | **UNI** | Bought | 6.7758 | fee $1.25 |
| Mon 09 Nov, 11:40 | 🟢 Momentum (spot) | **ZEC** | Bought | 1,222.38 | fee $1.25 |
| Mon 09 Nov, 11:40 | 🟢 Momentum (spot) | **XMR** | Bought | 593.46 | fee $1.25 |
| Mon 09 Nov, 11:39 | 🟠 Breakout | **TRX** | Closed | 0.31659 | −$18.25 |
| Mon 09 Nov, 11:39 | 🟠 Breakout | **SUI** | Opened short | 0.81988 | fee $0.45 |
| Mon 09 Nov, 11:39 | 🟢 Momentum | **LIT** | Closed | 3.0731 | −$33.67 |
| Mon 09 Nov, 11:39 | 🟢 Momentum | **AAVE** | Closed | 129.34 | +$31.46 |
| Mon 09 Nov, 11:39 | 🟢 Momentum | **SUI** | Closed | 0.81992 | +$83.26 |

### Signal board (daily candle of 2026-11-10)

What each strategy sees per coin. 🔔 = the condition for a trade is met.

| Coin | MA: 20d vs 50d | Breakout: vs 20-day range | Momentum: 14d return |
|---|---|---|---|
| **HYPE** | below (−4.4%) | 🔔 below 20d low | −11.1% (#8) |
| **ZEC** | below (−4.7%) | 🔔 below 20d low | −20.2% (#13) |
| **SOL** | below (−10.3%) | 🔔 below 20d low | −17.8% (#11) |
| **NEAR** | below (−10.6%) | +52.2% to high / −4.0% to low | −23.4% (#15) |
| **XRP** | below (−8.5%) | 🔔 below 20d low | −20.7% (#14) |
| **XMR** | above (+4.8%) | +17.4% to high / −0.0% to low | −7.4% (#4) 🔔 top 5: long |
| **PUMP** | below (−13.6%) | +49.1% to high / −0.8% to low | −19.6% (#12) |
| **LIT** | below (−11.4%) | +14.8% to high / −26.1% to low | +13.7% (#2) 🔔 top 5: long |
| **kPEPE** | above (+7.2%) | +6.1% to high / −21.9% to low | +17.1% (#1) 🔔 top 5: long |
| **WLD** | below (−15.8%) | +92.1% to high / −2.9% to low | −29.1% (#19) 🔔 bottom 5: short |
| **ENA** | below (−12.9%) | +50.7% to high / −3.8% to low | −28.1% (#17) 🔔 bottom 5: short |
| **UNI** | below (−9.8%) | +17.3% to high / −6.4% to low | −5.9% (#3) 🔔 top 5: long |
| **TRUMP** | below (−15.9%) | +68.0% to high / −3.3% to low | −33.0% (#20) 🔔 bottom 5: short |
| **XPL** | below (−17.1%) | +65.3% to high / −4.6% to low | −29.0% (#18) 🔔 bottom 5: short |
| **BNB** | below (−3.5%) | +12.0% to high / −1.5% to low | −8.6% (#7) |
| **SUI** | below (−11.9%) | +28.2% to high / −2.6% to low | −11.7% (#10) |
| **AAVE** | below (−11.7%) | +29.9% to high / −6.8% to low | −7.6% (#5) 🔔 top 5: long |
| **ZRO** | below (−6.0%) | +39.5% to high / −7.5% to low | −8.5% (#6) |
| **LINK** | below (−10.0%) | +24.5% to high / −1.5% to low | −11.1% (#9) |
| **VVV** | below (−8.4%) | 🔔 below 20d low | −26.1% (#16) 🔔 bottom 5: short |

_Momentum trades its top/bottom 5 at the Monday rebalance; MA and breakout act at each daily run. Spot uses the same signals but only buys: a short signal just sells what it holds._

### This week's coins (chosen 2026-11-09)

HYPE · ZEC · SOL · NEAR · XRP · XMR · PUMP · LIT · kPEPE · WLD · ENA · UNI · TRUMP · XPL · BNB · SUI · AAVE · ZRO · LINK · VVV

_The 20 most-traded Hyperliquid futures over the past week, excluding BTC and ETH. Refreshed Mondays 00:00 UTC (5:00 AM PKT)._

## Alpaca paper account

Value **$49,666.37** · cash $46,097.26 · account ending YUU8  
Holding: 2 MU (−$352.86), 1.02972e+08 PEPEUSD (+$43.04), 73.6075 UNIUSD (−$21.13)

**2** simulated spot trade(s) copied and open · 🔴 1 copy error(s): see the spot log. Copies use the same number of coins as the simulation, with a real stop order on Alpaca.

Crypto spot bot: no coins on its watchlist yet (daily 00:15 UTC). Stock bot: stopped.

---
✅ Last run OK · [futures log](logs/futures_bot.log) · [spot log](logs/spot_bot.log) · [project log](PROJECT_LOG.md) · on the PC: `python dashboard.py`

<sub>This page is written by summary.py; edits by hand are overwritten.</sub>
