# SpikeAI paper trading

_Updated **Mon 02 Nov 2026, 11:13 PKT** (Mon 01:13 ET). Refreshed after every daily run. Paper trading only: no real money._

## Strategy test: MA crossover vs breakout vs momentum

**55 days left** in the evaluation (until 2026-12-27), then the best strategy is kept.  
Each simulated account started with $10,000. Futures: 2x, long and short, $500 margin per trade. Spot: 1x, buy-only, $500 per buy, copied to Alpaca for coins it lists. Both use an 8% stop.

### Futures

| Strategy | Value | Return | Below peak | Open | Closed (won) | Fees | Funding |
|---|--:|--:|--:|--:|--:|--:|--:|
| 🔵 MA crossover 20/50 | **$10,001.74** | +0.02% | at peak | 2 | 0 | $0.90 | +$0.41 |
| 🟠 Breakout 20/10 | **$9,989.24** | −0.11% | −0.11% | 1 | 0 | $0.45 | +$0.21 |
| 🟢 Momentum 14d, 5 long/5 short | **$9,995.82** | −0.04% | −0.04% | 10 | 0 | $4.50 | $0.00 |

**Futures leader:** 🔵 MA crossover 20/50, $5.92 ahead of Momentum 14d, 5 long/5 short.

### Spot

| Strategy | Value | Return | Below peak | Held | Closed (won) | Fees | On Alpaca |
|---|--:|--:|--:|--:|--:|--:|--:|
| 🔵 MA crossover 20/50 | **$10,000.00** | 0.00% | at peak | 0 | 0 | $0.00 | 0 |
| 🟠 Breakout 20/10 | **$10,000.00** | 0.00% | at peak | 0 | 0 | $0.00 | 0 |
| 🟢 Momentum 14d, 5 long/5 short | **$9,992.51** | −0.07% | −0.07% | 5 | 0 | $6.25 | 1 |

_Spot: no clear leader yet._

![Account value over time: solid = futures, dashed = spot](reports/equity.svg)

_Solid lines = futures, dashed = spot._

<details><summary>Account values as a table</summary>

| Date | MA | Breakout | Momentum | MA (spot) | Breakout (spot) | Momentum (spot) |
|---|--:|--:|--:|--:|--:|--:|
| 2026-10-30 | $9,999.54 | $10,000.00 | $10,000.00 | – | – | – |
| 2026-10-31 | $9,988.39 | $9,999.78 | $10,000.00 | $10,000.00 | $10,000.00 | $10,000.00 |
| 2026-11-01 | $10,001.28 | $9,989.21 | $9,994.61 | $10,000.00 | $10,000.00 | $9,992.51 |
| now | $10,001.74 | $9,989.24 | $9,995.82 | $10,000.00 | $10,000.00 | $9,992.51 |

</details>

### Open positions

| Strategy | Coin | Side | Entry → now | Profit | To stop | To liquidation / Alpaca |
|---|---|---|---|--:|--:|--:|
| 🔵 MA | **SUI** | ▼ Short | 0.89681 → 0.89419 | +$2.92 (+0.6%) | ✅ 8.3% | ✅ 43.3% |
| 🔵 MA | **WLD** | ▼ Short | 0.38553 → 0.3858 | −$0.70 (−0.1%) | ✅ 7.9% | ✅ 42.8% |
| 🟠 Breakout | **TRX** | ▼ Short | 0.31088 → 0.31415 | −$10.52 (−2.1%) | ✅ 6.9% | ✅ 41.4% |
| 🟢 Momentum | **VVV** | ▲ Long | 22.7768 → 22.775 | −$0.08 (−0.0%) | ✅ 8.0% | ✅ 40.0% |
| 🟢 Momentum | **LIT** | ▲ Long | 3.1789 → 3.1814 | +$0.79 (+0.2%) | ✅ 8.1% | ✅ 44.5% |
| 🟢 Momentum | **ZEC** | ▲ Long | 1,272.10 → 1,273.90 | +$1.41 (+0.3%) | ✅ 8.1% | ✅ 47.4% |
| 🟢 Momentum | **HYPE** | ▲ Long | 87.476 → 87.504 | +$0.32 (+0.1%) | ✅ 8.0% | ✅ 47.4% |
| 🟢 Momentum | **kPEPE** | ▲ Long | 0.004845 → 0.00485 | +$1.03 (+0.2%) | ✅ 8.1% | ✅ 47.4% |
| 🟢 Momentum | **WLD** | ▼ Short | 0.38553 → 0.3858 | −$0.70 (−0.1%) | ✅ 7.9% | ✅ 42.8% |
| 🟢 Momentum | **NEAR** | ▼ Short | 4.202 → 4.2055 | −$0.83 (−0.2%) | ✅ 7.9% | ✅ 42.7% |
| 🟢 Momentum | **AAVE** | ▼ Short | 133.43 → 133.52 | −$0.67 (−0.1%) | ✅ 7.9% | ✅ 42.8% |
| 🟢 Momentum | **SUI** | ▼ Short | 0.89362 → 0.89419 | −$0.64 (−0.1%) | ✅ 7.9% | ✅ 42.8% |
| 🟢 Momentum | **SOL** | ▼ Short | 94.657 → 94.686 | −$0.31 (−0.1%) | ✅ 8.0% | ✅ 46.3% |
| 🟢 Momentum (spot) | **VVV** | ▲ Long | 22.7334 → 22.766 | −$1.78 (−0.4%) | ✅ 8.1% | not on Alpaca |
| 🟢 Momentum (spot) | **LIT** | ▲ Long | 0.098691 → 0.0984 | −$3.97 (−0.8%) | ✅ 7.7% | not on Alpaca |
| 🟢 Momentum (spot) | **ZEC** | ▲ Long | 1,270.13 → 1,270.26 | −$2.45 (−0.5%) | ✅ 8.0% | not on Alpaca |
| 🟢 Momentum (spot) | **HYPE** | ▲ Long | 87.41 → 87.38 | −$2.67 (−0.5%) | ✅ 8.0% | 🔴 copy failed |
| 🟢 Momentum (spot) | **PEPE** | ▲ Long | 0.0000048436 → 0.00000484 | −$2.86 (−0.6%) | ✅ 7.9% | ✅ copied |

_Distance = how far the price can still move against the position. ✅ over 5% · ⚠️ 2–5% · 🔴 under 2%. Spot can't be liquidated; its last column shows whether the trade is copied to Alpaca._

### Recent trades

| Time (PKT) | Strategy | Coin | What | Price | Result |
|---|---|---|---|--:|--:|
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
| Mon 02 Nov, 11:12 | 🟢 Momentum | **SUI** | Opened short | 0.89362 | fee $0.45 |
| Mon 02 Nov, 11:12 | 🟢 Momentum | **SOL** | Opened short | 94.657 | fee $0.45 |
| Mon 02 Nov, 11:12 | 🟢 Momentum (spot) | **VVV** | Bought | 22.7334 | fee $1.25 |
| Mon 02 Nov, 11:12 | 🟢 Momentum (spot) | **LIT** | Bought | 0.098691 | fee $1.25 |
| Mon 02 Nov, 11:12 | 🟢 Momentum (spot) | **ZEC** | Bought | 1,270.13 | fee $1.25 |

### Signal board (daily candle of 2026-11-01)

What each strategy sees per coin. 🔔 = the condition for a trade is met.

| Coin | MA: 20d vs 50d | Breakout: vs 20-day range | Momentum: 14d return |
|---|---|---|---|
| **HYPE** | below (−5.0%) | +10.6% to high / −15.4% to low | +11.5% (#2) 🔔 top 5: long |
| **ZEC** | below (−7.3%) | +13.4% to high / −15.1% to low | +9.2% (#3) 🔔 top 5: long |
| **SOL** | below (−6.3%) | +20.0% to high / −2.4% to low | −9.2% (#16) 🔔 bottom 5: short |
| **NEAR** | above (+4.1%) | +40.2% to high / −8.9% to low | −14.5% (#19) 🔔 bottom 5: short |
| **kPEPE** | above (+4.3%) | +16.8% to high / −23.1% to low | +21.9% (#1) 🔔 top 5: long |
| **ENA** | below (−5.7%) | +35.1% to high / −10.0% to low | −2.7% (#11) |
| **XRP** | below (−6.2%) | +13.7% to high / −4.0% to low | −4.3% (#12) |
| **BNB** | below (−2.5%) | +7.0% to high / −6.0% to low | −1.5% (#9) |
| **PUMP** | below (−6.3%) | +44.2% to high / −10.3% to low | +0.7% (#6) |
| **XMR** | above (+4.9%) | +10.3% to high / −13.3% to low | +0.1% (#8) |
| **LIT** | below (−17.4%) | +26.5% to high / −18.8% to low | +2.6% (#4) 🔔 top 5: long |
| **UNI** | below (−9.3%) | +8.6% to high / −13.6% to low | +0.3% (#7) |
| **WLD** | below (−0.7%) 🔔 crossed down | +52.5% to high / −8.1% to low | −19.8% (#20) 🔔 bottom 5: short |
| **XPL** | below (−10.4%) | +25.5% to high / −5.3% to low | −7.2% (#15) |
| **ZRO** | above (+8.1%) | +37.3% to high / −21.7% to low | −2.7% (#10) |
| **SUI** | below (−3.9%) | +26.5% to high / −8.1% to low | −9.6% (#17) 🔔 bottom 5: short |
| **TRX** | below (−1.1%) | +16.6% to high / −3.9% to low | −5.9% (#14) |
| **AAVE** | below (−4.3%) | +28.4% to high / −14.5% to low | −11.4% (#18) 🔔 bottom 5: short |
| **LINK** | below (−5.9%) | +18.5% to high / −9.9% to low | −5.3% (#13) |
| **VVV** | below (−6.2%) | +23.8% to high / −8.4% to low | +1.1% (#5) 🔔 top 5: long |

_Momentum trades its top/bottom 5 at the Monday rebalance; MA and breakout act at each daily run. Spot uses the same signals but only buys: a short signal just sells what it holds._

### This week's coins (chosen 2026-11-02)

HYPE · ZEC · SOL · NEAR · kPEPE · ENA · XRP · BNB · PUMP · XMR · LIT · UNI · WLD · XPL · ZRO · SUI · TRX · AAVE · LINK · VVV

_The 20 most-traded Hyperliquid futures over the past week, excluding BTC and ETH. Refreshed Mondays 00:00 UTC (5:00 AM PKT)._

## Alpaca paper account

Value **$49,947.71** · cash $47,108.92 · account ending YUU8  
Holding: 2 MU (−$57.86), 1.02972e+08 PEPEUSD (+$7.00)

**1** simulated spot trade(s) copied and open · 🔴 1 copy error(s): see the spot log. Copies use the same number of coins as the simulation, with a real stop order on Alpaca.

Crypto spot bot: no coins on its watchlist yet (daily 00:15 UTC). Stock bot: stopped.

---
✅ Last run OK · [futures log](logs/futures_bot.log) · [spot log](logs/spot_bot.log) · [project log](PROJECT_LOG.md) · on the PC: `python dashboard.py`

<sub>This page is written by summary.py; edits by hand are overwritten.</sub>
