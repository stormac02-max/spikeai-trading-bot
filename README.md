# SpikeAI paper trading

_Updated **Sun 08 Nov 2026, 11:07 PKT** (Sun 01:07 ET). Refreshed after every daily run. Paper trading only: no real money._

## Strategy test: MA crossover vs breakout vs momentum

**49 days left** in the evaluation (until 2026-12-27), then the best strategy is kept.  
Each simulated account started with $10,000. Futures: 2x, long and short, $500 margin per trade. Spot: 1x, buy-only, $500 per buy, copied to Alpaca for coins it lists. Both use an 8% stop.

### Futures

| Strategy | Value | Return | Below peak | Open | Closed (won) | Fees | Funding |
|---|--:|--:|--:|--:|--:|--:|--:|
| 🔵 MA crossover 20/50 | **$10,277.64** | +2.78% | at peak | 4 | 0 | $1.80 | −$0.20 |
| 🟠 Breakout 20/10 | **$10,109.90** | +1.10% | at peak | 8 | 1 (0) | $4.54 | +$3.03 |
| 🟢 Momentum 14d, 5 long/5 short | **$10,185.55** | +1.86% | −0.09% | 7 | 3 (0) | $5.74 | +$0.49 |

**Futures leader:** 🔵 MA crossover 20/50, $92.09 ahead of Momentum 14d, 5 long/5 short.

### Spot

| Strategy | Value | Return | Below peak | Held | Closed (won) | Fees | On Alpaca |
|---|--:|--:|--:|--:|--:|--:|--:|
| 🔵 MA crossover 20/50 | **$10,000.00** | 0.00% | at peak | 0 | 0 | $0.00 | 0 |
| 🟠 Breakout 20/10 | **$10,000.00** | 0.00% | at peak | 0 | 0 | $0.00 | 0 |
| 🟢 Momentum 14d, 5 long/5 short | **$9,834.86** | −1.65% | −1.65% | 1 | 4 (0) | $10.84 | 1 |

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
| now | $10,277.64 | $10,109.90 | $10,185.55 | $10,000.00 | $10,000.00 | $9,834.86 |

</details>

### Open positions

| Strategy | Coin | Side | Entry → now | Profit | To stop | To liquidation / Alpaca |
|---|---|---|---|--:|--:|--:|
| 🔵 MA | **SUI** | ▼ Short | 0.89681 → 0.85253 | +$49.38 (+9.8%) | ✅ 13.6% | ✅ 50.4% |
| 🔵 MA | **WLD** | ▼ Short | 0.38553 → 0.33019 | +$143.54 (+28.8%) | ✅ 26.1% | ✅ 66.6% |
| 🔵 MA | **NEAR** | ▼ Short | 4.0459 → 3.6955 | +$86.61 (+17.3%) | ✅ 18.2% | ✅ 56.5% |
| 🔵 MA | **ZRO** | ▼ Short | 1.6048 → 1.6046 | +$0.11 (+0.0%) | ✅ 8.0% | ✅ 36.4% |
| 🟠 Breakout | **TRX** | ▼ Short | 0.31088 → 0.32068 | −$31.52 (−6.3%) | ⚠️ 4.7% | ✅ 38.6% |
| 🟠 Breakout | **SOL** | ▼ Short | 91.244 → 89.17 | +$22.73 (+4.5%) | ✅ 10.5% | ✅ 49.8% |
| 🟠 Breakout | **XPL** | ▼ Short | 0.062812 → 0.056174 | +$105.68 (+21.1%) | ✅ 20.8% | ✅ 59.9% |
| 🟠 Breakout | **NEAR** | ▼ Short | 3.6822 → 3.6955 | −$3.61 (−0.7%) | ✅ 7.6% | ✅ 42.4% |
| 🟠 Breakout | **ENA** | ▼ Short | 0.1646 → 0.15482 | +$59.41 (+11.9%) | ✅ 14.8% | ✅ 51.9% |
| 🟠 Breakout | **WLD** | ▼ Short | 0.34441 → 0.33019 | +$41.30 (+8.3%) | ✅ 12.7% | ✅ 48.9% |
| 🟠 Breakout | **XRP** | ▼ Short | 1.1619 → 1.1649 | −$2.58 (−0.5%) | ✅ 7.7% | ✅ 46.0% |
| 🟠 Breakout | **PUMP** | ▼ Short | 0.003674 → 0.003674 | $0.00 (0.0%) | ✅ 8.0% | ✅ 42.9% |
| 🟢 Momentum | **LIT** | ▲ Long | 3.1789 → 3.28 | +$31.80 (+6.4%) | ✅ 10.8% | ✅ 46.1% |
| 🟢 Momentum | **kPEPE** | ▲ Long | 0.004845 → 0.004901 | +$11.56 (+2.3%) | ✅ 9.1% | ✅ 48.0% |
| 🟢 Momentum | **WLD** | ▼ Short | 0.38553 → 0.33019 | +$143.54 (+28.8%) | ✅ 26.1% | ✅ 66.6% |
| 🟢 Momentum | **NEAR** | ▼ Short | 4.202 → 3.6955 | +$120.54 (+24.1%) | ✅ 22.8% | ✅ 62.6% |
| 🟢 Momentum | **AAVE** | ▼ Short | 133.43 → 130.84 | +$19.41 (+3.9%) | ✅ 10.1% | ✅ 45.8% |
| 🟢 Momentum | **SUI** | ▼ Short | 0.89362 → 0.85253 | +$45.98 (+9.2%) | ✅ 13.2% | ✅ 49.8% |
| 🟢 Momentum | **SOL** | ▼ Short | 94.657 → 89.17 | +$57.97 (+11.6%) | ✅ 14.6% | ✅ 55.5% |
| 🟢 Momentum (spot) | **PEPE** | ▲ Long | 0.0000048436 → 0.000004895 | +$2.79 (+0.6%) | ✅ 9.0% | ✅ copied |

_Distance = how far the price can still move against the position. ✅ over 5% · ⚠️ 2–5% · 🔴 under 2%. Spot can't be liquidated; its last column shows whether the trade is copied to Alpaca._

### Recent trades

| Time (PKT) | Strategy | Coin | What | Price | Result |
|---|---|---|---|--:|--:|
| Sun 08 Nov, 11:06 | 🔵 MA | **ZRO** | Opened short | 1.6048 | fee $0.45 |
| Sun 08 Nov, 11:06 | 🟠 Breakout | **PUMP** | Opened short | 0.003674 | fee $0.45 |
| Sat 07 Nov, 11:02 | 🟠 Breakout | **XRP** | Opened short | 1.1619 | fee $0.45 |
| Fri 06 Nov, 11:53 | 🟠 Breakout | **NEAR** | Opened short | 3.6822 | fee $0.45 |
| Fri 06 Nov, 11:53 | 🟠 Breakout | **ENA** | Opened short | 0.1646 | fee $0.45 |
| Fri 06 Nov, 11:53 | 🟠 Breakout | **WLD** | Opened short | 0.34441 | fee $0.45 |
| Thu 05 Nov, 19:00 | 🟢 Momentum | **HYPE** | Stopped out | 80.4779 | −$81.43 |
| Thu 05 Nov, 19:00 | 🟢 Momentum (spot) | **HYPE** | Stopped out | 80.4172 | −$42.30 |
| Thu 05 Nov, 11:52 | 🔵 MA | **NEAR** | Opened short | 4.0459 | fee $0.45 |
| Wed 04 Nov, 13:00 | 🟠 Breakout | **NEAR** | Stopped out | 4.0584 | −$80.15 |
| Tue 03 Nov, 17:00 | 🟢 Momentum (spot) | **LIT** | Stopped out | 0.090796 | −$42.30 |
| Tue 03 Nov, 13:00 | 🟢 Momentum | **VVV** | Stopped out | 20.9547 | −$80.71 |
| Tue 03 Nov, 13:00 | 🟢 Momentum (spot) | **VVV** | Stopped out | 20.9148 | −$42.30 |
| Tue 03 Nov, 11:52 | 🟠 Breakout | **SOL** | Opened short | 91.244 | fee $0.45 |
| Tue 03 Nov, 11:52 | 🟠 Breakout | **NEAR** | Opened short | 3.7578 | fee $0.45 |

### Signal board (daily candle of 2026-11-07)

What each strategy sees per coin. 🔔 = the condition for a trade is met.

| Coin | MA: 20d vs 50d | Breakout: vs 20-day range | Momentum: 14d return |
|---|---|---|---|
| **HYPE** | below (−4.6%) | +24.9% to high / −4.3% to low | +1.5% (#5) 🔔 top 5: long |
| **ZEC** | below (−5.0%) | +11.0% to high / −16.9% to low | +4.4% (#3) 🔔 top 5: long |
| **SOL** | below (−8.8%) | +21.6% to high / −1.7% to low | −12.3% (#14) |
| **NEAR** | below (−6.5%) | +46.2% to high / −3.0% to low | −16.9% (#17) 🔔 bottom 5: short |
| **kPEPE** | above (+6.1%) | +17.5% to high / −22.7% to low | +7.8% (#1) 🔔 top 5: long |
| **ENA** | below (−10.9%) | +42.4% to high / −1.7% to low | −18.8% (#18) 🔔 bottom 5: short |
| **XRP** | below (−7.3%) | 🔔 below 20d low | −10.4% (#13) |
| **BNB** | below (−3.2%) | +9.5% to high / −3.7% to low | −5.9% (#9) |
| **PUMP** | below (−10.4%) | 🔔 below 20d low | −13.8% (#15) |
| **XMR** | above (+5.7%) | +10.0% to high / −6.3% to low | −2.6% (#6) |
| **LIT** | below (−12.9%) | +20.5% to high / −22.4% to low | +2.4% (#4) 🔔 top 5: long |
| **UNI** | below (−10.0%) | +8.2% to high / −13.6% to low | +5.3% (#2) 🔔 top 5: long |
| **WLD** | below (−9.1%) | +78.4% to high / −1.5% to low | −28.5% (#20) 🔔 bottom 5: short |
| **XPL** | below (−14.7%) | +51.4% to high / −1.5% to low | −23.1% (#19) 🔔 bottom 5: short |
| **ZRO** | below (−1.1%) 🔔 crossed down | +30.0% to high / −13.7% to low | −6.4% (#10) |
| **SUI** | below (−9.6%) | +23.3% to high / −3.4% to low | −8.7% (#12) |
| **TRX** | below (−1.7%) | +14.1% to high / −6.0% to low | −2.8% (#7) |
| **AAVE** | below (−9.7%) | +22.0% to high / −12.5% to low | −4.5% (#8) |
| **LINK** | below (−8.8%) | +18.2% to high / −5.2% to low | −6.8% (#11) |
| **VVV** | below (−7.2%) | +37.2% to high / −3.8% to low | −14.6% (#16) 🔔 bottom 5: short |

_Momentum trades its top/bottom 5 at the Monday rebalance; MA and breakout act at each daily run. Spot uses the same signals but only buys: a short signal just sells what it holds._

### This week's coins (chosen 2026-11-02)

HYPE · ZEC · SOL · NEAR · kPEPE · ENA · XRP · BNB · PUMP · XMR · LIT · UNI · WLD · XPL · ZRO · SUI · TRX · AAVE · LINK · VVV

_The 20 most-traded Hyperliquid futures over the past week, excluding BTC and ETH. Refreshed Mondays 00:00 UTC (5:00 AM PKT)._

## Alpaca paper account

Value **$49,504.65** · cash $47,108.92 · account ending YUU8  
Holding: 2 MU (−$498.86), 1.02972e+08 PEPEUSD (+$4.94)

**1** simulated spot trade(s) copied and open. Copies use the same number of coins as the simulation, with a real stop order on Alpaca.

Crypto spot bot: no coins on its watchlist yet (daily 00:15 UTC). Stock bot: stopped.

---
✅ Last run OK · [futures log](logs/futures_bot.log) · [spot log](logs/spot_bot.log) · [project log](PROJECT_LOG.md) · on the PC: `python dashboard.py`

<sub>This page is written by summary.py; edits by hand are overwritten.</sub>
