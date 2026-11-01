# SpikeAI paper trading

_Updated **Sun 01 Nov 2026, 11:12 PKT** (Sun 01:12 ET). Refreshed after every daily run. Paper trading only: no real money._

## Strategy test: MA crossover vs breakout vs momentum

**56 days left** in the evaluation (until 2026-12-27), then the best strategy is kept.  
Each simulated account started with $10,000. Futures: 2x, long and short, $500 margin per trade. Spot: 1x, buy-only, $500 per buy, copied to Alpaca for coins it lists. Both use an 8% stop.

### Futures

| Strategy | Value | Return | Below peak | Open | Closed (won) | Fees | Funding |
|---|--:|--:|--:|--:|--:|--:|--:|
| 🔵 MA crossover 20/50 | **$9,988.39** | −0.12% | −0.12% | 1 | 0 | $0.45 | +$0.11 |
| 🟠 Breakout 20/10 | **$9,999.20** | −0.01% | −0.01% | 1 | 0 | $0.45 | $0.00 |
| 🟢 Momentum 14d, 5 long/5 short | **$10,000.00** | 0.00% | at peak | 0 | 0 | $0.00 | $0.00 |

_Futures: no clear leader yet._

### Spot

| Strategy | Value | Return | Below peak | Held | Closed (won) | Fees | On Alpaca |
|---|--:|--:|--:|--:|--:|--:|--:|
| 🔵 MA crossover 20/50 | **$10,000.00** | 0.00% | at peak | 0 | 0 | $0.00 | 0 |
| 🟠 Breakout 20/10 | **$10,000.00** | 0.00% | at peak | 0 | 0 | $0.00 | 0 |
| 🟢 Momentum 14d, 5 long/5 short | **$10,000.00** | 0.00% | at peak | 0 | 0 | $0.00 | 0 |

_Spot: no clear leader yet._

![Account value over time: solid = futures, dashed = spot](reports/equity.svg)

_Solid lines = futures, dashed = spot._

<details><summary>Account values as a table</summary>

| Date | MA | Breakout | Momentum | MA (spot) | Breakout (spot) | Momentum (spot) |
|---|--:|--:|--:|--:|--:|--:|
| 2026-10-30 | $9,999.54 | $10,000.00 | $10,000.00 | – | – | – |
| 2026-10-31 | $9,988.39 | $9,999.78 | $10,000.00 | $10,000.00 | $10,000.00 | $10,000.00 |
| now | $9,988.39 | $9,999.20 | $10,000.00 | $10,000.00 | $10,000.00 | $10,000.00 |

</details>

### Open positions

| Strategy | Coin | Side | Entry → now | Profit | To stop | To liquidation / Alpaca |
|---|---|---|---|--:|--:|--:|
| 🔵 MA | **SUI** | ▼ Short | 0.89681 → 0.90692 | −$11.27 (−2.3%) | ✅ 6.8% | ✅ 41.3% |
| 🟠 Breakout | **TRX** | ▼ Short | 0.31088 → 0.31099 | −$0.35 (−0.1%) | ✅ 8.0% | ✅ 42.8% |

_Distance = how far the price can still move against the position. ✅ over 5% · ⚠️ 2–5% · 🔴 under 2%. Spot can't be liquidated; its last column shows whether the trade is copied to Alpaca._

### Recent trades

| Time (PKT) | Strategy | Coin | What | Price | Result |
|---|---|---|---|--:|--:|
| Sun 01 Nov, 11:11 | 🟠 Breakout | **TRX** | Opened short | 0.31088 | fee $0.45 |
| Sun 01 Nov, 01:46 | 🔵 MA | **SUI** | Opened short | 0.89681 | fee $0.45 |

### Signal board (daily candle of 2026-10-31)

What each strategy sees per coin. 🔔 = the condition for a trade is met.

| Coin | MA: 20d vs 50d | Breakout: vs 20-day range | Momentum: 14d return |
|---|---|---|---|
| **HYPE** | below (−5.2%) | +10.4% to high / −15.4% to low | +12.8% (#2) 🔔 top 5: long |
| **ZEC** | below (−7.4%) | +11.9% to high / −16.2% to low | +11.0% (#3) 🔔 top 5: long |
| **SOL** | below (−5.9%) | +18.9% to high / −3.3% to low | −7.7% (#15) |
| **NEAR** | above (+5.8%) | +35.7% to high / −11.9% to low | −8.8% (#17) 🔔 bottom 5: short |
| **kPEPE** | above (+3.9%) | +15.1% to high / −24.2% to low | +28.2% (#1) 🔔 top 5: long |
| **XRP** | below (−6.0%) | +14.0% to high / −4.1% to low | −3.3% (#14) |
| **ENA** | below (−4.8%) | +31.2% to high / −12.6% to low | +0.3% (#8) |
| **PUMP** | below (−5.3%) | +43.8% to high / −10.5% to low | −3.2% (#13) |
| **XMR** | above (+4.5%) | +10.4% to high / −13.8% to low | +5.0% (#4) 🔔 top 5: long |
| **BNB** | below (−2.4%) | +8.4% to high / −4.7% to low | −2.0% (#11) |
| **WLD** | above (+0.3%) | +50.2% to high / −9.5% to low | −19.1% (#20) 🔔 bottom 5: short |
| **UNI** | below (−9.3%) | +11.5% to high / −11.9% to low | −1.0% (#10) |
| **LIT** | below (−17.6%) | +26.6% to high / −18.7% to low | +1.2% (#7) |
| **SUI** | below (−2.9%) | +27.0% to high / −7.9% to low | −7.9% (#16) 🔔 bottom 5: short |
| **ZRO** | above (+9.9%) | +34.2% to high / −23.4% to low | −0.8% (#9) |
| **XPL** | below (−10.1%) | +10.1% to high / −17.2% to low | +3.5% (#6) |
| **AAVE** | below (−3.5%) | +29.4% to high / −13.8% to low | −11.9% (#19) 🔔 bottom 5: short |
| **VVV** | below (−6.4%) | +21.3% to high / −10.2% to low | +4.7% (#5) 🔔 top 5: long |
| **TRX** | below (−1.1%) | 🔔 below 20d low | −9.2% (#18) 🔔 bottom 5: short |
| **LINK** | below (−5.4%) | +15.9% to high / −11.9% to low | −2.7% (#12) |

_Momentum trades its top/bottom 5 at the Monday rebalance; MA and breakout act at each daily run. Spot uses the same signals but only buys: a short signal just sells what it holds._

### This week's coins (chosen 2026-10-31)

HYPE · ZEC · SOL · NEAR · kPEPE · XRP · ENA · PUMP · XMR · BNB · WLD · UNI · LIT · SUI · ZRO · XPL · AAVE · VVV · TRX · LINK

_The 20 most-traded Hyperliquid futures over the past week, excluding BTC and ETH. Refreshed Mondays 00:00 UTC (5:00 AM PKT)._

## Alpaca paper account

Value **$49,890.43** · cash $48,120.95 · account ending YUU8  
Holding: 2 MU (−$109.38)

**0** simulated spot trade(s) copied and open. Copies use the same number of coins as the simulation, with a real stop order on Alpaca.

Crypto spot bot: no coins on its watchlist yet (daily 00:15 UTC). Stock bot: stopped.

---
✅ Last run OK · [futures log](logs/futures_bot.log) · [spot log](logs/spot_bot.log) · [project log](PROJECT_LOG.md) · on the PC: `python dashboard.py`

<sub>This page is written by summary.py; edits by hand are overwritten.</sub>
