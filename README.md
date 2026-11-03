# SpikeAI paper trading

_Updated **Tue 03 Nov 2026, 11:52 PKT** (Tue 01:52 ET). Refreshed after every daily run. Paper trading only: no real money._

## Strategy test: MA crossover vs breakout vs momentum

**54 days left** in the evaluation (until 2026-12-27), then the best strategy is kept.  
Each simulated account started with $10,000. Futures: 2x, long and short, $500 margin per trade. Spot: 1x, buy-only, $500 per buy, copied to Alpaca for coins it lists. Both use an 8% stop.

### Futures

| Strategy | Value | Return | Below peak | Open | Closed (won) | Fees | Funding |
|---|--:|--:|--:|--:|--:|--:|--:|
| 🔵 MA crossover 20/50 | **$10,097.18** | +0.97% | at peak | 2 | 0 | $0.90 | +$0.95 |
| 🟠 Breakout 20/10 | **$9,967.71** | −0.32% | −0.32% | 4 | 0 | $1.80 | +$0.28 |
| 🟢 Momentum 14d, 5 long/5 short | **$10,025.90** | +0.26% | −0.01% | 9 | 1 (0) | $4.91 | −$0.21 |

**Futures leader:** 🔵 MA crossover 20/50, $71.28 ahead of Momentum 14d, 5 long/5 short.

### Spot

| Strategy | Value | Return | Below peak | Held | Closed (won) | Fees | On Alpaca |
|---|--:|--:|--:|--:|--:|--:|--:|
| 🔵 MA crossover 20/50 | **$10,000.00** | 0.00% | at peak | 0 | 0 | $0.00 | 0 |
| 🟠 Breakout 20/10 | **$10,000.00** | 0.00% | at peak | 0 | 0 | $0.00 | 0 |
| 🟢 Momentum 14d, 5 long/5 short | **$9,853.76** | −1.46% | −1.46% | 4 | 1 (0) | $7.40 | 1 |

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
| now | $10,097.18 | $9,967.71 | $10,025.90 | $10,000.00 | $10,000.00 | $9,853.76 |

</details>

### Open positions

| Strategy | Coin | Side | Entry → now | Profit | To stop | To liquidation / Alpaca |
|---|---|---|---|--:|--:|--:|
| 🔵 MA | **SUI** | ▼ Short | 0.89681 → 0.85918 | +$41.96 (+8.4%) | ✅ 12.7% | ✅ 49.2% |
| 🔵 MA | **WLD** | ▼ Short | 0.38553 → 0.36426 | +$55.17 (+11.0%) | ✅ 14.3% | ✅ 51.2% |
| 🟠 Breakout | **TRX** | ▼ Short | 0.31088 → 0.32041 | −$30.65 (−6.1%) | ⚠️ 4.8% | ✅ 38.6% |
| 🟠 Breakout | **SOL** | ▼ Short | 91.244 → 91.245 | −$0.01 (−0.0%) | ✅ 8.0% | ✅ 46.3% |
| 🟠 Breakout | **NEAR** | ▼ Short | 3.7578 → 3.758 | −$0.05 (−0.0%) | ✅ 8.0% | ✅ 42.8% |
| 🟠 Breakout | **XPL** | ▼ Short | 0.062812 → 0.062815 | −$0.05 (−0.0%) | ✅ 8.0% | ✅ 42.8% |
| 🟢 Momentum | **VVV** | ▲ Long | 22.7768 → 21.242 | −$67.39 (−13.5%) | 🔴 1.4% | ✅ 35.6% |
| 🟢 Momentum | **LIT** | ▲ Long | 3.1789 → 3.0629 | −$36.49 (−7.3%) | ⚠️ 4.5% | ✅ 42.3% |
| 🟢 Momentum | **HYPE** | ▲ Long | 87.476 → 83.512 | −$45.32 (−9.1%) | ⚠️ 3.6% | ✅ 44.8% |
| 🟢 Momentum | **kPEPE** | ▲ Long | 0.004845 → 0.004671 | −$35.91 (−7.2%) | ⚠️ 4.6% | ✅ 45.4% |
| 🟢 Momentum | **WLD** | ▼ Short | 0.38553 → 0.36426 | +$55.17 (+11.0%) | ✅ 14.3% | ✅ 51.2% |
| 🟢 Momentum | **NEAR** | ▼ Short | 4.202 → 3.758 | +$105.66 (+21.1%) | ✅ 20.8% | ✅ 59.7% |
| 🟢 Momentum | **AAVE** | ▼ Short | 133.43 → 125.33 | +$60.71 (+12.1%) | ✅ 15.0% | ✅ 52.1% |
| 🟢 Momentum | **SUI** | ▼ Short | 0.89362 → 0.85918 | +$38.54 (+7.7%) | ✅ 12.3% | ✅ 48.6% |
| 🟢 Momentum | **SOL** | ▼ Short | 94.657 → 91.245 | +$36.05 (+7.2%) | ✅ 12.0% | ✅ 51.8% |
| 🟢 Momentum (spot) | **VVV** | ▲ Long | 22.7334 → 21.198 | −$36.10 (−7.2%) | 🔴 1.3% | not on Alpaca |
| 🟢 Momentum (spot) | **LIT** | ▲ Long | 0.098691 → 0.0939 | −$26.65 (−5.3%) | ⚠️ 3.3% | not on Alpaca |
| 🟢 Momentum (spot) | **HYPE** | ▲ Long | 87.41 → 83.44 | −$25.09 (−5.0%) | ⚠️ 3.6% | 🔴 copy failed |
| 🟢 Momentum (spot) | **PEPE** | ▲ Long | 0.0000048436 → 0.000004665 | −$20.84 (−4.2%) | ⚠️ 4.5% | ✅ copied |

_Distance = how far the price can still move against the position. ✅ over 5% · ⚠️ 2–5% · 🔴 under 2%. Spot can't be liquidated; its last column shows whether the trade is copied to Alpaca._

### Recent trades

| Time (PKT) | Strategy | Coin | What | Price | Result |
|---|---|---|---|--:|--:|
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
| Mon 02 Nov, 11:12 | 🟢 Momentum | **WLD** | Opened short | 0.38553 | fee $0.45 |
| Mon 02 Nov, 11:12 | 🟢 Momentum | **NEAR** | Opened short | 4.202 | fee $0.45 |
| Mon 02 Nov, 11:12 | 🟢 Momentum | **AAVE** | Opened short | 133.43 | fee $0.45 |

### Signal board (daily candle of 2026-11-02)

What each strategy sees per coin. 🔔 = the condition for a trade is met.

| Coin | MA: 20d vs 50d | Breakout: vs 20-day range | Momentum: 14d return |
|---|---|---|---|
| **HYPE** | below (−5.0%) | +15.6% to high / −11.5% to low | +6.1% (#2) 🔔 top 5: long |
| **ZEC** | below (−7.7%) | +23.3% to high / −7.7% to low | −1.5% (#5) 🔔 top 5: long |
| **SOL** | below (−6.8%) | 🔔 below 20d low | −12.4% (#15) |
| **NEAR** | above (+2.1%) | 🔔 below 20d low | −21.2% (#19) 🔔 bottom 5: short |
| **kPEPE** | above (+4.3%) | +19.6% to high / −21.2% to low | +14.8% (#1) 🔔 top 5: long |
| **ENA** | below (−6.9%) | +32.5% to high / −3.3% to low | −9.8% (#11) |
| **XRP** | below (−6.4%) | +12.0% to high / −4.0% to low | −4.1% (#8) |
| **BNB** | below (−2.8%) | +9.0% to high / −4.1% to low | −4.5% (#9) |
| **PUMP** | below (−7.6%) | +31.6% to high / −5.3% to low | −11.5% (#13) |
| **XMR** | above (+5.1%) | +9.3% to high / −14.1% to low | −0.2% (#3) 🔔 top 5: long |
| **LIT** | below (−17.3%) | +29.2% to high / −16.8% to low | −0.4% (#4) 🔔 top 5: long |
| **UNI** | below (−9.8%) | +9.7% to high / −12.0% to low | −3.0% (#6) |
| **WLD** | below (−2.1%) | +58.2% to high / −4.7% to low | −29.2% (#20) 🔔 bottom 5: short |
| **XPL** | below (−11.1%) | 🔔 below 20d low | −12.9% (#17) 🔔 bottom 5: short |
| **ZRO** | above (+6.3%) | +32.2% to high / −17.8% to low | −9.9% (#12) |
| **SUI** | below (−5.1%) | +23.4% to high / −5.2% to low | −12.6% (#16) 🔔 bottom 5: short |
| **TRX** | below (−1.1%) | +14.3% to high / −5.9% to low | −3.8% (#7) |
| **AAVE** | below (−5.5%) | +31.1% to high / −9.0% to low | −15.3% (#18) 🔔 bottom 5: short |
| **LINK** | below (−6.6%) | +18.6% to high / −7.6% to low | −7.8% (#10) |
| **VVV** | below (−6.5%) | +32.8% to high / −1.7% to low | −11.8% (#14) |

_Momentum trades its top/bottom 5 at the Monday rebalance; MA and breakout act at each daily run. Spot uses the same signals but only buys: a short signal just sells what it holds._

### This week's coins (chosen 2026-11-02)

HYPE · ZEC · SOL · NEAR · kPEPE · ENA · XRP · BNB · PUMP · XMR · LIT · UNI · WLD · XPL · ZRO · SUI · TRX · AAVE · LINK · VVV

_The 20 most-traded Hyperliquid futures over the past week, excluding BTC and ETH. Refreshed Mondays 00:00 UTC (5:00 AM PKT)._

## Alpaca paper account

Value **$49,782.08** · cash $47,108.92 · account ending YUU8  
Holding: 2 MU (−$200.84), 1.02972e+08 PEPEUSD (−$15.65)

**1** simulated spot trade(s) copied and open · 🔴 1 copy error(s): see the spot log. Copies use the same number of coins as the simulation, with a real stop order on Alpaca.

Crypto spot bot: no coins on its watchlist yet (daily 00:15 UTC). Stock bot: stopped.

---
✅ Last run OK · [futures log](logs/futures_bot.log) · [spot log](logs/spot_bot.log) · [project log](PROJECT_LOG.md) · on the PC: `python dashboard.py`

<sub>This page is written by summary.py; edits by hand are overwritten.</sub>
