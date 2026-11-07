# SpikeAI paper trading

_Updated **Sat 07 Nov 2026, 11:03 PKT** (Sat 01:03 ET). Refreshed after every daily run. Paper trading only: no real money._

## Strategy test: MA crossover vs breakout vs momentum

**50 days left** in the evaluation (until 2026-12-27), then the best strategy is kept.  
Each simulated account started with $10,000. Futures: 2x, long and short, $500 margin per trade. Spot: 1x, buy-only, $500 per buy, copied to Alpaca for coins it lists. Both use an 8% stop.

### Futures

| Strategy | Value | Return | Below peak | Open | Closed (won) | Fees | Funding |
|---|--:|--:|--:|--:|--:|--:|--:|
| 🔵 MA crossover 20/50 | **$10,221.92** | +2.22% | −0.16% | 3 | 0 | $1.35 | +$0.33 |
| 🟠 Breakout 20/10 | **$9,972.03** | −0.28% | −0.28% | 7 | 1 (0) | $4.09 | +$2.76 |
| 🟢 Momentum 14d, 5 long/5 short | **$10,182.90** | +1.83% | −0.11% | 7 | 3 (0) | $5.74 | −$0.40 |

**Futures leader:** 🔵 MA crossover 20/50, $39.02 ahead of Momentum 14d, 5 long/5 short.

### Spot

| Strategy | Value | Return | Below peak | Held | Closed (won) | Fees | On Alpaca |
|---|--:|--:|--:|--:|--:|--:|--:|
| 🔵 MA crossover 20/50 | **$10,000.00** | 0.00% | at peak | 0 | 0 | $0.00 | 0 |
| 🟠 Breakout 20/10 | **$10,000.00** | 0.00% | at peak | 0 | 0 | $0.00 | 0 |
| 🟢 Momentum 14d, 5 long/5 short | **$9,837.64** | −1.62% | −1.62% | 1 | 4 (0) | $10.84 | 1 |

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
| now | $10,221.92 | $9,972.03 | $10,182.90 | $10,000.00 | $10,000.00 | $9,837.64 |

</details>

### Open positions

| Strategy | Coin | Side | Entry → now | Profit | To stop | To liquidation / Alpaca |
|---|---|---|---|--:|--:|--:|
| 🔵 MA | **SUI** | ▼ Short | 0.89681 → 0.86915 | +$30.84 (+6.2%) | ✅ 11.4% | ✅ 47.5% |
| 🔵 MA | **WLD** | ▼ Short | 0.38553 → 0.34065 | +$116.41 (+23.4%) | ✅ 22.2% | ✅ 61.5% |
| 🔵 MA | **NEAR** | ▼ Short | 4.0459 → 3.7397 | +$75.68 (+15.1%) | ✅ 16.8% | ✅ 54.6% |
| 🟠 Breakout | **TRX** | ▼ Short | 0.31088 → 0.31787 | −$22.47 (−4.5%) | ✅ 5.6% | ✅ 39.8% |
| 🟠 Breakout | **SOL** | ▼ Short | 91.244 → 90.239 | +$11.01 (+2.2%) | ✅ 9.2% | ✅ 48.0% |
| 🟠 Breakout | **XPL** | ▼ Short | 0.062812 → 0.058541 | +$67.99 (+13.6%) | ✅ 15.9% | ✅ 53.4% |
| 🟠 Breakout | **NEAR** | ▼ Short | 3.6822 → 3.7397 | −$15.62 (−3.1%) | ✅ 6.3% | ✅ 40.7% |
| 🟠 Breakout | **ENA** | ▼ Short | 0.1646 → 0.16435 | +$1.51 (+0.3%) | ✅ 8.2% | ✅ 43.1% |
| 🟠 Breakout | **WLD** | ▼ Short | 0.34441 → 0.34065 | +$10.93 (+2.2%) | ✅ 9.2% | ✅ 44.4% |
| 🟠 Breakout | **XRP** | ▼ Short | 1.1619 → 1.1619 | −$0.01 (−0.0%) | ✅ 8.0% | ✅ 46.3% |
| 🟢 Momentum | **LIT** | ▲ Long | 3.1789 → 3.4926 | +$98.68 (+19.8%) | ✅ 16.3% | ✅ 49.4% |
| 🟢 Momentum | **kPEPE** | ▲ Long | 0.004845 → 0.004924 | +$16.31 (+3.3%) | ✅ 9.5% | ✅ 48.1% |
| 🟢 Momentum | **WLD** | ▼ Short | 0.38553 → 0.34065 | +$116.41 (+23.4%) | ✅ 22.2% | ✅ 61.5% |
| 🟢 Momentum | **NEAR** | ▼ Short | 4.202 → 3.7397 | +$110.02 (+22.0%) | ✅ 21.4% | ✅ 60.6% |
| 🟢 Momentum | **AAVE** | ▼ Short | 133.43 → 131.62 | +$13.57 (+2.7%) | ✅ 9.5% | ✅ 44.9% |
| 🟢 Momentum | **SUI** | ▼ Short | 0.89362 → 0.86915 | +$27.38 (+5.5%) | ✅ 11.0% | ✅ 47.0% |
| 🟢 Momentum | **SOL** | ▼ Short | 94.657 → 90.239 | +$46.67 (+9.3%) | ✅ 13.3% | ✅ 53.6% |
| 🟢 Momentum (spot) | **PEPE** | ▲ Long | 0.0000048436 → 0.000004922 | +$5.56 (+1.1%) | ✅ 9.5% | ✅ copied |

_Distance = how far the price can still move against the position. ✅ over 5% · ⚠️ 2–5% · 🔴 under 2%. Spot can't be liquidated; its last column shows whether the trade is copied to Alpaca._

### Recent trades

| Time (PKT) | Strategy | Coin | What | Price | Result |
|---|---|---|---|--:|--:|
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
| Tue 03 Nov, 11:52 | 🟠 Breakout | **XPL** | Opened short | 0.062812 | fee $0.45 |
| Mon 02 Nov, 22:00 | 🟢 Momentum | **ZEC** | Stopped out | 1,170.33 | −$80.54 |

### Signal board (daily candle of 2026-11-06)

What each strategy sees per coin. 🔔 = the condition for a trade is met.

| Coin | MA: 20d vs 50d | Breakout: vs 20-day range | Momentum: 14d return |
|---|---|---|---|
| **HYPE** | below (−4.9%) | +23.7% to high / −5.3% to low | +1.9% (#5) 🔔 top 5: long |
| **ZEC** | below (−6.0%) | +5.8% to high / −20.7% to low | +11.9% (#1) 🔔 top 5: long |
| **SOL** | below (−8.6%) | +21.2% to high / −2.1% to low | −12.3% (#15) |
| **NEAR** | below (−5.1%) | +47.1% to high / −2.4% to low | −20.8% (#18) 🔔 bottom 5: short |
| **kPEPE** | above (+5.6%) | +14.6% to high / −24.6% to low | +9.0% (#2) 🔔 top 5: long |
| **ENA** | below (−10.3%) | +38.1% to high / −4.6% to low | −17.8% (#17) 🔔 bottom 5: short |
| **XRP** | below (−7.1%) | 🔔 below 20d low | −9.0% (#12) |
| **BNB** | below (−3.2%) | +9.9% to high / −3.4% to low | −6.2% (#9) |
| **PUMP** | below (−10.1%) | +33.6% to high / −3.9% to low | −8.8% (#11) |
| **XMR** | above (+5.8%) | +8.1% to high / −10.9% to low | +4.6% (#4) 🔔 top 5: long |
| **LIT** | below (−13.9%) | +19.8% to high / −22.9% to low | +5.6% (#3) 🔔 top 5: long |
| **UNI** | below (−10.4%) | +13.5% to high / −9.4% to low | −1.1% (#6) |
| **WLD** | below (−7.9%) | +74.0% to high / −3.9% to low | −28.7% (#20) 🔔 bottom 5: short |
| **XPL** | below (−14.3%) | +50.1% to high / −2.1% to low | −24.1% (#19) 🔔 bottom 5: short |
| **ZRO** | above (+0.1%) | +30.7% to high / −13.3% to low | −4.0% (#8) |
| **SUI** | below (−8.9%) | +21.6% to high / −4.7% to low | −9.5% (#14) |
| **TRX** | below (−1.6%) | +14.7% to high / −5.5% to low | −3.6% (#7) |
| **AAVE** | below (−9.1%) | +22.8% to high / −11.9% to low | −9.4% (#13) |
| **LINK** | below (−8.5%) | +18.0% to high / −5.4% to low | −8.2% (#10) |
| **VVV** | below (−7.3%) | +36.5% to high / −4.3% to low | −17.2% (#16) 🔔 bottom 5: short |

_Momentum trades its top/bottom 5 at the Monday rebalance; MA and breakout act at each daily run. Spot uses the same signals but only buys: a short signal just sells what it holds._

### This week's coins (chosen 2026-11-02)

HYPE · ZEC · SOL · NEAR · kPEPE · ENA · XRP · BNB · PUMP · XMR · LIT · UNI · WLD · XPL · ZRO · SUI · TRX · AAVE · LINK · VVV

_The 20 most-traded Hyperliquid futures over the past week, excluding BTC and ETH. Refreshed Mondays 00:00 UTC (5:00 AM PKT)._

## Alpaca paper account

Value **$49,512.89** · cash $47,108.92 · account ending YUU8  
Holding: 2 MU (−$498.86), 1.02972e+08 PEPEUSD (+$13.18)

**1** simulated spot trade(s) copied and open. Copies use the same number of coins as the simulation, with a real stop order on Alpaca.

Crypto spot bot: no coins on its watchlist yet (daily 00:15 UTC). Stock bot: stopped.

---
✅ Last run OK · [futures log](logs/futures_bot.log) · [spot log](logs/spot_bot.log) · [project log](PROJECT_LOG.md) · on the PC: `python dashboard.py`

<sub>This page is written by summary.py; edits by hand are overwritten.</sub>
