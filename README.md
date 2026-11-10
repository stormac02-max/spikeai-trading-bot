# SpikeAI paper trading

_Updated **Tue 10 Nov 2026, 12:24 PKT** (Tue 02:24 ET). Refreshed after every daily run. Paper trading only: no real money._

## Strategy test: MA crossover vs breakout vs momentum

**47 days left** in the evaluation (until 2026-12-27), then the best strategy is kept.  
Each simulated account started with $10,000. Futures: 2x, long and short, $500 margin per trade. Spot: 1x, buy-only, $500 per buy, copied to Alpaca for coins it lists. Both use an 8% stop.

### Futures

| Strategy | Value | Return | Below peak | Open | Closed (won) | Fees | Funding |
|---|--:|--:|--:|--:|--:|--:|--:|
| 🔵 MA crossover 20/50 | **$10,395.63** | +3.96% | −0.44% | 4 | 0 | $1.80 | +$0.23 |
| 🟠 Breakout 20/10 | **$10,327.75** | +3.28% | −1.08% | 8 | 2 (0) | $5.44 | +$3.60 |
| 🟢 Momentum 14d, 5 long/5 short | **$10,241.62** | +2.42% | −0.52% | 10 | 7 (3) | $10.59 | −$1.04 |

**Futures leader:** 🔵 MA crossover 20/50, $67.89 ahead of Breakout 20/10.

### Spot

| Strategy | Value | Return | Below peak | Held | Closed (won) | Fees | On Alpaca |
|---|--:|--:|--:|--:|--:|--:|--:|
| 🔵 MA crossover 20/50 | **$10,000.00** | 0.00% | at peak | 0 | 0 | $0.00 | 0 |
| 🟠 Breakout 20/10 | **$10,000.00** | 0.00% | at peak | 0 | 0 | $0.00 | 0 |
| 🟢 Momentum 14d, 5 long/5 short | **$9,837.31** | −1.63% | −1.63% | 5 | 4 (0) | $15.84 | 2 |

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
| now | $10,395.63 | $10,327.75 | $10,241.62 | $10,000.00 | $10,000.00 | $9,837.31 |

</details>

### Open positions

| Strategy | Coin | Side | Entry → now | Profit | To stop | To liquidation / Alpaca |
|---|---|---|---|--:|--:|--:|
| 🔵 MA | **SUI** | ▼ Short | 0.89681 → 0.84724 | +$55.27 (+11.0%) | ✅ 14.3% | ✅ 51.4% |
| 🔵 MA | **WLD** | ▼ Short | 0.38553 → 0.31989 | +$170.26 (+34.2%) | ✅ 30.2% | ✅ 71.9% |
| 🔵 MA | **NEAR** | ▼ Short | 4.0459 → 3.6373 | +$100.99 (+20.2%) | ✅ 20.1% | ✅ 59.0% |
| 🔵 MA | **ZRO** | ▼ Short | 1.6048 → 1.4914 | +$70.68 (+14.1%) | ✅ 16.2% | ✅ 46.8% |
| 🟠 Breakout | **SOL** | ▼ Short | 91.244 → 86.155 | +$55.77 (+11.1%) | ✅ 14.4% | ✅ 55.1% |
| 🟠 Breakout | **XPL** | ▼ Short | 0.062812 → 0.051683 | +$177.18 (+35.3%) | ✅ 31.3% | ✅ 73.8% |
| 🟠 Breakout | **NEAR** | ▼ Short | 3.6822 → 3.6373 | +$12.19 (+2.4%) | ✅ 9.3% | ✅ 44.7% |
| 🟠 Breakout | **ENA** | ▼ Short | 0.1646 → 0.15367 | +$66.40 (+13.3%) | ✅ 15.7% | ✅ 53.1% |
| 🟠 Breakout | **WLD** | ▼ Short | 0.34441 → 0.31989 | +$71.21 (+14.3%) | ✅ 16.3% | ✅ 53.6% |
| 🟠 Breakout | **XRP** | ▼ Short | 1.1619 → 1.0997 | +$53.53 (+10.7%) | ✅ 14.1% | ✅ 54.6% |
| 🟠 Breakout | **PUMP** | ▼ Short | 0.003674 → 0.003582 | +$25.04 (+5.0%) | ✅ 10.8% | ✅ 46.6% |
| 🟠 Breakout | **SUI** | ▼ Short | 0.81988 → 0.84724 | −$33.37 (−6.7%) | ⚠️ 4.5% | ✅ 38.3% |
| 🟢 Momentum | **kPEPE** | ▲ Long | 0.004845 → 0.005301 | +$94.12 (+18.8%) | ✅ 15.9% | ✅ 51.9% |
| 🟢 Momentum | **WLD** | ▼ Short | 0.38553 → 0.31989 | +$170.26 (+34.2%) | ✅ 30.2% | ✅ 71.9% |
| 🟢 Momentum | **NEAR** | ▼ Short | 4.202 → 3.6373 | +$134.39 (+26.8%) | ✅ 24.8% | ✅ 65.2% |
| 🟢 Momentum | **HYPE** | ▲ Long | 74.024 → 74.672 | +$8.75 (+1.8%) | ✅ 8.8% | ✅ 47.8% |
| 🟢 Momentum | **UNI** | ▲ Long | 6.7821 → 7.0978 | +$46.54 (+9.3%) | ✅ 12.1% | ✅ 49.7% |
| 🟢 Momentum | **ZEC** | ▲ Long | 1,221.54 → 1,149.20 | −$59.22 (−11.9%) | ⚠️ 2.2% | ✅ 44.0% |
| 🟢 Momentum | **XMR** | ▲ Long | 593.82 → 559.70 | −$57.46 (−11.5%) | ⚠️ 2.4% | ✅ 40.9% |
| 🟢 Momentum | **TRUMP** | ▼ Short | 1.1454 → 1.1255 | +$17.35 (+3.5%) | ✅ 9.9% | ✅ 45.4% |
| 🟢 Momentum | **XPL** | ▼ Short | 0.051503 → 0.051683 | −$3.50 (−0.7%) | ✅ 7.6% | ✅ 42.4% |
| 🟢 Momentum | **ENA** | ▼ Short | 0.14951 → 0.15367 | −$27.81 (−5.6%) | ✅ 5.1% | ✅ 39.0% |
| 🟢 Momentum (spot) | **PEPE** | ▲ Long | 0.0000048436 → 0.000005291 | +$43.46 (+8.7%) | ✅ 15.8% | ✅ copied |
| 🟢 Momentum (spot) | **HYPE** | ▲ Long | 74.1398 → 74.65 | +$0.93 (+0.2%) | ✅ 8.6% | 🔴 copy failed |
| 🟢 Momentum (spot) | **UNI** | ▲ Long | 6.7758 → 7.0932 | +$20.81 (+4.2%) | ✅ 12.1% | ✅ copied |
| 🟢 Momentum (spot) | **ZEC** | ▲ Long | 1,222.38 → 1,147.55 | −$32.95 (−6.6%) | ⚠️ 2.0% | not on Alpaca |
| 🟢 Momentum (spot) | **XMR** | ▲ Long | 593.46 → 558.25 | −$32.01 (−6.4%) | ⚠️ 2.2% | not on Alpaca |

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

### Signal board (daily candle of 2026-11-09)

What each strategy sees per coin. 🔔 = the condition for a trade is met.

| Coin | MA: 20d vs 50d | Breakout: vs 20-day range | Momentum: 14d return |
|---|---|---|---|
| **HYPE** | below (−4.4%) | +29.3% to high / −1.9% to low | −4.0% (#6) |
| **ZEC** | below (−4.3%) | +20.3% to high / −3.9% to low | −5.6% (#7) |
| **SOL** | below (−9.8%) | +26.0% to high / −1.8% to low | −14.1% (#12) |
| **NEAR** | below (−9.1%) | +50.4% to high / −5.1% to low | −19.5% (#16) 🔔 bottom 5: short |
| **XRP** | below (−8.0%) | +27.4% to high / −0.5% to low | −16.1% (#15) |
| **XMR** | above (+5.2%) | +13.2% to high / −3.6% to low | −2.4% (#3) 🔔 top 5: long |
| **PUMP** | below (−12.2%) | +44.4% to high / −3.9% to low | −15.5% (#14) |
| **LIT** | below (−11.6%) | +23.1% to high / −20.7% to low | +7.2% (#2) 🔔 top 5: long |
| **kPEPE** | above (+6.7%) | +11.3% to high / −19.9% to low | +18.9% (#1) 🔔 top 5: long |
| **WLD** | below (−13.4%) | +87.6% to high / −5.1% to low | −28.3% (#18) 🔔 bottom 5: short |
| **ENA** | below (−11.9%) | +47.6% to high / −5.8% to low | −26.1% (#17) 🔔 bottom 5: short |
| **UNI** | below (−9.8%) | +12.0% to high / −10.6% to low | −2.4% (#4) 🔔 top 5: long |
| **TRUMP** | below (−14.9%) | +71.4% to high / −1.3% to low | −34.2% (#20) 🔔 bottom 5: short |
| **XPL** | below (−16.2%) | +67.2% to high / −3.5% to low | −29.0% (#19) 🔔 bottom 5: short |
| **BNB** | below (−3.4%) | +10.2% to high / −3.1% to low | −6.9% (#9) |
| **SUI** | below (−11.2%) | +25.0% to high / −5.1% to low | −8.0% (#10) |
| **AAVE** | below (−10.9%) | +22.1% to high / −12.5% to low | −3.1% (#5) 🔔 top 5: long |
| **ZRO** | below (−4.4%) | +44.5% to high / −4.1% to low | −9.3% (#11) |
| **LINK** | below (−9.5%) | +20.2% to high / −5.0% to low | −6.5% (#8) |
| **VVV** | below (−7.8%) | +30.8% to high / −9.6% to low | −14.1% (#13) |

_Momentum trades its top/bottom 5 at the Monday rebalance; MA and breakout act at each daily run. Spot uses the same signals but only buys: a short signal just sells what it holds._

### This week's coins (chosen 2026-11-09)

HYPE · ZEC · SOL · NEAR · XRP · XMR · PUMP · LIT · kPEPE · WLD · ENA · UNI · TRUMP · XPL · BNB · SUI · AAVE · ZRO · LINK · VVV

_The 20 most-traded Hyperliquid futures over the past week, excluding BTC and ETH. Refreshed Mondays 00:00 UTC (5:00 AM PKT)._

## Alpaca paper account

Value **$49,639.42** · cash $46,097.26 · account ending YUU8  
Holding: 2 MU (−$417.14), 1.02972e+08 PEPEUSD (+$42.01), 73.6075 UNIUSD (+$17.24)

**2** simulated spot trade(s) copied and open · 🔴 1 copy error(s): see the spot log. Copies use the same number of coins as the simulation, with a real stop order on Alpaca.

Crypto spot bot: no coins on its watchlist yet (daily 00:15 UTC). Stock bot: stopped.

---
✅ Last run OK · [futures log](logs/futures_bot.log) · [spot log](logs/spot_bot.log) · [project log](PROJECT_LOG.md) · on the PC: `python dashboard.py`

<sub>This page is written by summary.py; edits by hand are overwritten.</sub>
