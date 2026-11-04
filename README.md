# SpikeAI paper trading

_Updated **Wed 04 Nov 2026, 11:29 PKT** (Wed 01:29 ET). Refreshed after every daily run. Paper trading only: no real money._

## Strategy test: MA crossover vs breakout vs momentum

**53 days left** in the evaluation (until 2026-12-27), then the best strategy is kept.  
Each simulated account started with $10,000. Futures: 2x, long and short, $500 margin per trade. Spot: 1x, buy-only, $500 per buy, copied to Alpaca for coins it lists. Both use an 8% stop.

### Futures

| Strategy | Value | Return | Below peak | Open | Closed (won) | Fees | Funding |
|---|--:|--:|--:|--:|--:|--:|--:|
| 🔵 MA crossover 20/50 | **$9,999.84** | −0.00% | −0.96% | 2 | 0 | $0.90 | +$1.43 |
| 🟠 Breakout 20/10 | **$9,880.53** | −1.19% | −1.19% | 4 | 0 | $1.80 | +$1.38 |
| 🟢 Momentum 14d, 5 long/5 short | **$9,971.15** | −0.29% | −0.55% | 8 | 2 (0) | $5.33 | +$0.21 |

**Futures leader:** 🔵 MA crossover 20/50, $28.69 ahead of Momentum 14d, 5 long/5 short.

### Spot

| Strategy | Value | Return | Below peak | Held | Closed (won) | Fees | On Alpaca |
|---|--:|--:|--:|--:|--:|--:|--:|
| 🔵 MA crossover 20/50 | **$10,000.00** | 0.00% | at peak | 0 | 0 | $0.00 | 0 |
| 🟠 Breakout 20/10 | **$10,000.00** | 0.00% | at peak | 0 | 0 | $0.00 | 0 |
| 🟢 Momentum 14d, 5 long/5 short | **$9,867.56** | −1.32% | −1.32% | 2 | 3 (0) | $9.69 | 1 |

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
| now | $9,999.84 | $9,880.53 | $9,971.15 | $10,000.00 | $10,000.00 | $9,867.56 |

</details>

### Open positions

| Strategy | Coin | Side | Entry → now | Profit | To stop | To liquidation / Alpaca |
|---|---|---|---|--:|--:|--:|
| 🔵 MA | **SUI** | ▼ Short | 0.89681 → 0.89582 | +$1.10 (+0.2%) | ✅ 8.1% | ✅ 43.1% |
| 🔵 MA | **WLD** | ▼ Short | 0.38553 → 0.38622 | −$1.79 (−0.4%) | ✅ 7.8% | ✅ 42.6% |
| 🟠 Breakout | **TRX** | ▼ Short | 0.31088 → 0.32291 | −$38.69 (−7.7%) | ⚠️ 4.0% | ✅ 37.6% |
| 🟠 Breakout | **SOL** | ▼ Short | 91.244 → 93.072 | −$20.03 (−4.0%) | ✅ 5.9% | ✅ 43.5% |
| 🟠 Breakout | **NEAR** | ▼ Short | 3.7578 → 3.949 | −$50.88 (−10.2%) | ⚠️ 2.8% | ✅ 36.0% |
| 🟠 Breakout | **XPL** | ▼ Short | 0.062812 → 0.063405 | −$9.44 (−1.9%) | ✅ 7.0% | ✅ 41.5% |
| 🟢 Momentum | **LIT** | ▲ Long | 3.1789 → 3.2986 | +$37.65 (+7.5%) | ✅ 11.3% | ✅ 46.4% |
| 🟢 Momentum | **HYPE** | ▲ Long | 87.476 → 84.585 | −$33.05 (−6.6%) | ⚠️ 4.9% | ✅ 45.5% |
| 🟢 Momentum | **kPEPE** | ▲ Long | 0.004845 → 0.004983 | +$28.48 (+5.7%) | ✅ 10.5% | ✅ 48.8% |
| 🟢 Momentum | **WLD** | ▼ Short | 0.38553 → 0.38622 | −$1.79 (−0.4%) | ✅ 7.8% | ✅ 42.6% |
| 🟢 Momentum | **NEAR** | ▼ Short | 4.202 → 3.949 | +$60.21 (+12.0%) | ✅ 14.9% | ✅ 52.0% |
| 🟢 Momentum | **AAVE** | ▼ Short | 133.43 → 129.37 | +$30.47 (+6.1%) | ✅ 11.4% | ✅ 47.4% |
| 🟢 Momentum | **SUI** | ▼ Short | 0.89362 → 0.89582 | −$2.46 (−0.5%) | ✅ 7.7% | ✅ 42.6% |
| 🟢 Momentum | **SOL** | ▼ Short | 94.657 → 93.072 | +$16.74 (+3.3%) | ✅ 9.8% | ✅ 48.9% |
| 🟢 Momentum (spot) | **HYPE** | ▲ Long | 87.41 → 84.54 | −$18.83 (−3.8%) | ⚠️ 4.9% | 🔴 copy failed |
| 🟢 Momentum (spot) | **PEPE** | ▲ Long | 0.0000048436 → 0.000004973 | +$10.80 (+2.2%) | ✅ 10.4% | ✅ copied |

_Distance = how far the price can still move against the position. ✅ over 5% · ⚠️ 2–5% · 🔴 under 2%. Spot can't be liquidated; its last column shows whether the trade is copied to Alpaca._

### Recent trades

| Time (PKT) | Strategy | Coin | What | Price | Result |
|---|---|---|---|--:|--:|
| Tue 03 Nov, 17:00 | 🟢 Momentum (spot) | **LIT** | Stopped out | 0.090796 | −$42.30 |
| Tue 03 Nov, 13:00 | 🟢 Momentum | **VVV** | Stopped out | 20.9547 | −$80.71 |
| Tue 03 Nov, 13:00 | 🟢 Momentum (spot) | **VVV** | Stopped out | 20.9148 | −$42.30 |
| Tue 03 Nov, 11:52 | 🟠 Breakout | **SOL** | Opened short | 91.244 | fee $0.45 |
| Tue 03 Nov, 11:52 | 🟠 Breakout | **NEAR** | Opened short | 3.7578 | fee $0.45 |
| Tue 03 Nov, 11:52 | 🟠 Breakout | **XPL** | Opened short | 0.062812 | fee $0.45 |
| Mon 02 Nov, 22:00 | 🟢 Momentum | **ZEC** | Stopped out | 1,170.33 | −$80.54 |
| Mon 02 Nov, 22:00 | 🟢 Momentum (spot) | **ZEC** | Stopped out | 1,168.52 | −$42.30 |
| Mon 02 Nov, 11:13 | 🟢 Momentum (spot) | **PEPE** | Bought | 0.0000048436 | fee $1.25 |
| Mon 02 Nov, 11:12 | 🔵 MA | **WLD** | Opened short | 0.38553 | fee $0.45 |
| Mon 02 Nov, 11:12 | 🟢 Momentum | **VVV** | Opened long | 22.7768 | fee $0.45 |
| Mon 02 Nov, 11:12 | 🟢 Momentum | **LIT** | Opened long | 3.1789 | fee $0.45 |
| Mon 02 Nov, 11:12 | 🟢 Momentum | **ZEC** | Opened long | 1,272.10 | fee $0.45 |
| Mon 02 Nov, 11:12 | 🟢 Momentum | **HYPE** | Opened long | 87.476 | fee $0.45 |
| Mon 02 Nov, 11:12 | 🟢 Momentum | **kPEPE** | Opened long | 0.004845 | fee $0.45 |

### Signal board (daily candle of 2026-11-03)

What each strategy sees per coin. 🔔 = the condition for a trade is met.

| Coin | MA: 20d vs 50d | Breakout: vs 20-day range | Momentum: 14d return |
|---|---|---|---|
| **HYPE** | below (−4.9%) | +14.1% to high / −12.6% to low | +5.9% (#2) 🔔 top 5: long |
| **ZEC** | below (−7.5%) | +14.8% to high / −14.0% to low | −3.0% (#6) |
| **SOL** | below (−7.2%) | +17.6% to high / −2.2% to low | −12.8% (#15) |
| **NEAR** | above (+0.3%) | 🔔 below 20d low | −22.3% (#19) 🔔 bottom 5: short |
| **kPEPE** | above (+4.6%) | +17.4% to high / −22.7% to low | +6.6% (#1) 🔔 top 5: long |
| **ENA** | below (−7.7%) | +29.3% to high / −5.6% to low | −10.8% (#12) |
| **XRP** | below (−6.4%) | +9.6% to high / −6.0% to low | −4.4% (#8) |
| **BNB** | below (−2.9%) | +9.2% to high / −4.0% to low | −5.9% (#9) |
| **PUMP** | below (−8.3%) | +20.8% to high / −13.1% to low | −11.0% (#13) |
| **XMR** | above (+5.4%) | +4.8% to high / −16.4% to low | +5.4% (#3) 🔔 top 5: long |
| **LIT** | below (−16.5%) | +18.7% to high / −23.5% to low | −0.9% (#4) 🔔 top 5: long |
| **UNI** | below (−9.9%) | +7.8% to high / −13.6% to low | −3.1% (#7) |
| **WLD** | below (−3.3%) | +58.4% to high / −4.6% to low | −35.8% (#20) 🔔 bottom 5: short |
| **XPL** | below (−11.7%) | 🔔 below 20d low | −19.5% (#18) 🔔 bottom 5: short |
| **ZRO** | above (+5.2%) | +21.8% to high / −24.3% to low | −6.8% (#10) |
| **SUI** | below (−6.0%) | +19.8% to high / −7.4% to low | −13.2% (#16) 🔔 bottom 5: short |
| **TRX** | below (−1.2%) | +13.5% to high / −6.5% to low | −3.0% (#5) 🔔 top 5: long |
| **AAVE** | below (−6.4%) | +30.5% to high / −9.4% to low | −17.8% (#17) 🔔 bottom 5: short |
| **LINK** | below (−7.0%) | +18.7% to high / −6.9% to low | −10.6% (#11) |
| **VVV** | below (−6.6%) | +25.3% to high / −7.2% to low | −11.4% (#14) |

_Momentum trades its top/bottom 5 at the Monday rebalance; MA and breakout act at each daily run. Spot uses the same signals but only buys: a short signal just sells what it holds._

### This week's coins (chosen 2026-11-02)

HYPE · ZEC · SOL · NEAR · kPEPE · ENA · XRP · BNB · PUMP · XMR · LIT · UNI · WLD · XPL · ZRO · SUI · TRX · AAVE · LINK · VVV

_The 20 most-traded Hyperliquid futures over the past week, excluding BTC and ETH. Refreshed Mondays 00:00 UTC (5:00 AM PKT)._

## Alpaca paper account

Value **$49,851.12** · cash $47,108.92 · account ending YUU8  
Holding: 2 MU (−$161.66), 1.02972e+08 PEPEUSD (+$14.21)

**1** simulated spot trade(s) copied and open · 🔴 1 copy error(s): see the spot log. Copies use the same number of coins as the simulation, with a real stop order on Alpaca.

Crypto spot bot: no coins on its watchlist yet (daily 00:15 UTC). Stock bot: stopped.

---
✅ Last run OK · [futures log](logs/futures_bot.log) · [spot log](logs/spot_bot.log) · [project log](PROJECT_LOG.md) · on the PC: `python dashboard.py`

<sub>This page is written by summary.py; edits by hand are overwritten.</sub>
