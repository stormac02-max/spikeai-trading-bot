# SpikeAI paper trading

_Updated **Fri 06 Nov 2026, 11:53 PKT** (Fri 01:53 ET). Refreshed after every daily run. Paper trading only: no real money._

## Strategy test: MA crossover vs breakout vs momentum

**51 days left** in the evaluation (until 2026-12-27), then the best strategy is kept.  
Each simulated account started with $10,000. Futures: 2x, long and short, $500 margin per trade. Spot: 1x, buy-only, $500 per buy, copied to Alpaca for coins it lists. Both use an 8% stop.

### Futures

| Strategy | Value | Return | Below peak | Open | Closed (won) | Fees | Funding |
|---|--:|--:|--:|--:|--:|--:|--:|
| 🔵 MA crossover 20/50 | **$10,237.71** | +2.38% | −0.01% | 3 | 0 | $1.35 | +$0.50 |
| 🟠 Breakout 20/10 | **$9,996.22** | −0.04% | −0.04% | 6 | 1 (0) | $3.64 | +$2.16 |
| 🟢 Momentum 14d, 5 long/5 short | **$10,190.85** | +1.91% | −0.04% | 7 | 3 (0) | $5.74 | −$0.57 |

**Futures leader:** 🔵 MA crossover 20/50, $46.86 ahead of Momentum 14d, 5 long/5 short.

### Spot

| Strategy | Value | Return | Below peak | Held | Closed (won) | Fees | On Alpaca |
|---|--:|--:|--:|--:|--:|--:|--:|
| 🔵 MA crossover 20/50 | **$10,000.00** | 0.00% | at peak | 0 | 0 | $0.00 | 0 |
| 🟠 Breakout 20/10 | **$10,000.00** | 0.00% | at peak | 0 | 0 | $0.00 | 0 |
| 🟢 Momentum 14d, 5 long/5 short | **$9,837.02** | −1.63% | −1.63% | 1 | 4 (0) | $10.84 | 1 |

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
| now | $10,237.71 | $9,996.22 | $10,190.85 | $10,000.00 | $10,000.00 | $9,837.02 |

</details>

### Open positions

| Strategy | Coin | Side | Entry → now | Profit | To stop | To liquidation / Alpaca |
|---|---|---|---|--:|--:|--:|
| 🔵 MA | **SUI** | ▼ Short | 0.89681 → 0.85854 | +$42.67 (+8.5%) | ✅ 12.8% | ✅ 49.4% |
| 🔵 MA | **WLD** | ▼ Short | 0.38553 → 0.34445 | +$106.55 (+21.4%) | ✅ 20.9% | ✅ 59.8% |
| 🔵 MA | **NEAR** | ▼ Short | 4.0459 → 3.6845 | +$89.32 (+17.9%) | ✅ 18.6% | ✅ 56.9% |
| 🟠 Breakout | **TRX** | ▼ Short | 0.31088 → 0.31878 | −$25.41 (−5.1%) | ✅ 5.3% | ✅ 39.3% |
| 🟠 Breakout | **SOL** | ▼ Short | 91.244 → 89.61 | +$17.91 (+3.6%) | ✅ 10.0% | ✅ 49.1% |
| 🟠 Breakout | **XPL** | ▼ Short | 0.062812 → 0.057415 | +$85.92 (+17.2%) | ✅ 18.2% | ✅ 56.4% |
| 🟠 Breakout | **NEAR** | ▼ Short | 3.6822 → 3.6845 | −$0.62 (−0.1%) | ✅ 7.9% | ✅ 42.8% |
| 🟠 Breakout | **ENA** | ▼ Short | 0.1646 → 0.1646 | +$0.01 (+0.0%) | ✅ 8.0% | ✅ 42.9% |
| 🟠 Breakout | **WLD** | ▼ Short | 0.34441 → 0.34445 | −$0.10 (−0.0%) | ✅ 8.0% | ✅ 42.8% |
| 🟢 Momentum | **LIT** | ▲ Long | 3.1789 → 3.4028 | +$70.45 (+14.1%) | ✅ 14.1% | ✅ 48.0% |
| 🟢 Momentum | **kPEPE** | ▲ Long | 0.004845 → 0.004915 | +$14.45 (+2.9%) | ✅ 9.3% | ✅ 48.0% |
| 🟢 Momentum | **WLD** | ▼ Short | 0.38553 → 0.34445 | +$106.55 (+21.4%) | ✅ 20.9% | ✅ 59.8% |
| 🟢 Momentum | **NEAR** | ▼ Short | 4.202 → 3.6845 | +$123.15 (+24.6%) | ✅ 23.2% | ✅ 63.0% |
| 🟢 Momentum | **AAVE** | ▼ Short | 133.43 → 129.43 | +$29.98 (+6.0%) | ✅ 11.3% | ✅ 47.3% |
| 🟢 Momentum | **SUI** | ▼ Short | 0.89362 → 0.85854 | +$39.26 (+7.8%) | ✅ 12.4% | ✅ 48.8% |
| 🟢 Momentum | **SOL** | ▼ Short | 94.657 → 89.61 | +$53.32 (+10.6%) | ✅ 14.1% | ✅ 54.7% |
| 🟢 Momentum (spot) | **PEPE** | ▲ Long | 0.0000048436 → 0.000004916 | +$4.94 (+1.0%) | ✅ 9.4% | ✅ copied |

_Distance = how far the price can still move against the position. ✅ over 5% · ⚠️ 2–5% · 🔴 under 2%. Spot can't be liquidated; its last column shows whether the trade is copied to Alpaca._

### Recent trades

| Time (PKT) | Strategy | Coin | What | Price | Result |
|---|---|---|---|--:|--:|
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
| Mon 02 Nov, 22:00 | 🟢 Momentum (spot) | **ZEC** | Stopped out | 1,168.52 | −$42.30 |

### Signal board (daily candle of 2026-11-05)

What each strategy sees per coin. 🔔 = the condition for a trade is met.

| Coin | MA: 20d vs 50d | Breakout: vs 20-day range | Momentum: 14d return |
|---|---|---|---|
| **HYPE** | below (−5.1%) | +26.8% to high / −2.9% to low | −1.0% (#5) 🔔 top 5: long |
| **ZEC** | below (−6.9%) | +9.2% to high / −18.2% to low | +5.2% (#2) 🔔 top 5: long |
| **SOL** | below (−8.1%) | 🔔 below 20d low | −13.9% (#14) |
| **NEAR** | below (−3.7%) | 🔔 below 20d low | −25.0% (#19) 🔔 bottom 5: short |
| **kPEPE** | above (+5.0%) | +19.1% to high / −21.6% to low | +9.2% (#1) 🔔 top 5: long |
| **ENA** | below (−9.6%) | 🔔 below 20d low | −19.2% (#16) 🔔 bottom 5: short |
| **XRP** | below (−6.8%) | +15.9% to high / −0.6% to low | −7.8% (#9) |
| **BNB** | below (−3.1%) | +10.5% to high / −2.8% to low | −5.7% (#8) |
| **PUMP** | below (−9.7%) | +35.2% to high / −2.8% to low | −14.9% (#15) |
| **XMR** | above (+5.8%) | +6.9% to high / −12.1% to low | +3.0% (#3) 🔔 top 5: long |
| **LIT** | below (−14.9%) | +16.0% to high / −25.3% to low | +1.5% (#4) 🔔 top 5: long |
| **UNI** | below (−10.4%) | +14.8% to high / −8.4% to low | −2.8% (#6) |
| **WLD** | below (−6.5%) | 🔔 below 20d low | −38.8% (#20) 🔔 bottom 5: short |
| **XPL** | below (−13.6%) | 🔔 below 20d low | −24.6% (#18) 🔔 bottom 5: short |
| **ZRO** | above (+1.4%) | +43.5% to high / −10.8% to low | −11.0% (#11) |
| **SUI** | below (−8.1%) | +26.2% to high / −1.6% to low | −13.5% (#13) |
| **TRX** | below (−1.5%) | +14.7% to high / −5.5% to low | −3.2% (#7) |
| **AAVE** | below (−8.4%) | +28.7% to high / −10.7% to low | −12.1% (#12) |
| **LINK** | below (−8.1%) | +19.9% to high / −3.9% to low | −10.6% (#10) |
| **VVV** | below (−7.4%) | +35.3% to high / −2.4% to low | −20.0% (#17) 🔔 bottom 5: short |

_Momentum trades its top/bottom 5 at the Monday rebalance; MA and breakout act at each daily run. Spot uses the same signals but only buys: a short signal just sells what it holds._

### This week's coins (chosen 2026-11-02)

HYPE · ZEC · SOL · NEAR · kPEPE · ENA · XRP · BNB · PUMP · XMR · LIT · UNI · WLD · XPL · ZRO · SUI · TRX · AAVE · LINK · VVV

_The 20 most-traded Hyperliquid futures over the past week, excluding BTC and ETH. Refreshed Mondays 00:00 UTC (5:00 AM PKT)._

## Alpaca paper account

Value **$49,489.62** · cash $47,108.92 · account ending YUU8  
Holding: 2 MU (−$512.86), 1.02972e+08 PEPEUSD (+$3.91)

**1** simulated spot trade(s) copied and open. Copies use the same number of coins as the simulation, with a real stop order on Alpaca.

Crypto spot bot: no coins on its watchlist yet (daily 00:15 UTC). Stock bot: stopped.

---
✅ Last run OK · [futures log](logs/futures_bot.log) · [spot log](logs/spot_bot.log) · [project log](PROJECT_LOG.md) · on the PC: `python dashboard.py`

<sub>This page is written by summary.py; edits by hand are overwritten.</sub>
