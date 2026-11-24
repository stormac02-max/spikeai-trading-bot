# SpikeAI paper trading

_Updated **Tue 24 Nov 2026, 14:59 PKT** (Tue 04:59 ET). Refreshed after every daily run. Paper trading only: no real money._

## Strategy test: MA crossover vs breakout vs momentum

**33 days left** in the evaluation (until 2026-12-27), then the best strategy is kept.  
Each simulated account started with $10,000. Futures: 2x, long and short, $500 margin per trade. Spot: 1x, buy-only, $500 per buy, copied to Alpaca for coins it lists. Both use an 8% stop.

### Futures

| Strategy | Value | Return | Below peak | Open | Closed (won) | Fees | Funding |
|---|--:|--:|--:|--:|--:|--:|--:|
| 🔵 MA crossover 20/50 | **$11,088.41** | +10.88% | −3.15% | 3 | 3 (1) | $4.01 | −$0.66 |
| 🟠 Breakout 20/10 | **$12,941.19** | +29.41% | −5.80% | 16 | 10 (2) | $16.28 | +$6.61 |
| 🟢 Momentum 14d, 5 long/5 short | **$10,903.62** | +9.04% | −0.91% | 5 | 20 (6) | $19.48 | −$9.89 |

**Futures leader:** 🟠 Breakout 20/10, $1,852.78 ahead of MA crossover 20/50.

### Spot

| Strategy | Value | Return | Below peak | Held | Closed (won) | Fees | On Alpaca |
|---|--:|--:|--:|--:|--:|--:|--:|
| 🔵 MA crossover 20/50 | **$10,000.00** | 0.00% | at peak | 0 | 0 | $0.00 | 0 |
| 🟠 Breakout 20/10 | **$10,004.27** | +0.04% | −0.17% | 1 | 0 | $1.25 | 0 |
| 🟢 Momentum 14d, 5 long/5 short | **$9,613.54** | −3.86% | −3.86% | 5 | 12 (0) | $35.02 | 2 |

**Spot leader:** 🟠 Breakout 20/10, $4.27 ahead of MA crossover 20/50.

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
| 2026-11-11 | $10,465.16 | $10,591.82 | $10,003.86 | $10,000.00 | $10,000.00 | $9,639.79 |
| 2026-11-12 | $10,502.65 | $10,863.61 | $10,142.84 | $10,000.00 | $10,000.00 | $9,643.96 |
| 2026-11-13 | $10,569.20 | $11,143.10 | $10,203.16 | $10,000.00 | $10,000.00 | $9,619.33 |
| 2026-11-14 | $10,842.64 | $12,031.38 | $10,629.43 | $10,000.00 | $10,000.00 | $9,619.33 |
| 2026-11-15 | $10,879.67 | $12,066.42 | $10,633.32 | $10,000.00 | $10,000.00 | $9,614.19 |
| 2026-11-16 | $10,754.52 | $11,659.55 | $10,585.62 | $10,000.00 | $10,000.00 | $9,678.18 |
| 2026-11-17 | $10,822.96 | $11,790.38 | $10,654.51 | $10,000.00 | $10,000.00 | $9,820.39 |
| 2026-11-18 | $10,770.65 | $11,796.49 | $10,712.06 | $10,000.00 | $10,000.00 | $9,874.21 |
| 2026-11-19 | $11,045.66 | $12,571.77 | $10,718.62 | $10,000.00 | $10,000.00 | $9,759.36 |
| 2026-11-20 | $11,449.50 | $13,737.30 | $10,920.02 | $10,000.00 | $10,000.00 | $9,645.85 |
| 2026-11-21 | $11,254.31 | $13,278.13 | $11,004.09 | $10,000.00 | $9,998.52 | $9,612.09 |
| 2026-11-22 | $11,083.23 | – | – | $10,000.00 | $10,021.08 | $9,635.59 |
| 2026-11-23 | $11,088.22 | $12,939.80 | $10,903.60 | $10,000.00 | $10,004.27 | $9,613.54 |
| now | $11,088.41 | $12,941.19 | $10,903.62 | $10,000.00 | $10,004.27 | $9,613.54 |

</details>

### Open positions

| Strategy | Coin | Side | Entry → now | Profit | To stop | To liquidation / Alpaca |
|---|---|---|---|--:|--:|--:|
| 🔵 MA | **WLD** | ▼ Short | 0.38553 → 0.23585 | +$388.24 (+78.9%) | ✅ 76.5% | ✅ 132.2% |
| 🔵 MA | **NEAR** | ▼ Short | 4.0459 → 2.9511 | +$270.59 (+53.8%) | ✅ 48.1% | ✅ 96.2% |
| 🔵 MA | **ZRO** | ▼ Short | 1.6048 → 1.0618 | +$338.37 (+67.2%) | ✅ 63.2% | ✅ 106.5% |
| 🟠 Breakout | **SOL** | ▼ Short | 91.244 → 70.68 | +$225.37 (+45.0%) | ✅ 39.4% | ✅ 89.0% |
| 🟠 Breakout | **NEAR** | ▼ Short | 3.6822 → 2.9511 | +$198.55 (+39.5%) | ✅ 34.8% | ✅ 78.6% |
| 🟠 Breakout | **ENA** | ▼ Short | 0.1646 → 0.098994 | +$398.57 (+79.3%) | ✅ 79.6% | ✅ 138.0% |
| 🟠 Breakout | **WLD** | ▼ Short | 0.34441 → 0.23585 | +$315.21 (+64.0%) | ✅ 57.7% | ✅ 107.5% |
| 🟠 Breakout | **XRP** | ▼ Short | 1.1619 → 0.93378 | +$196.33 (+39.3%) | ✅ 34.4% | ✅ 82.1% |
| 🟠 Breakout | **PUMP** | ▼ Short | 0.003674 → 0.002451 | +$332.88 (+66.3%) | ✅ 61.9% | ✅ 114.4% |
| 🟠 Breakout | **SUI** | ▼ Short | 0.81988 → 0.65843 | +$196.92 (+39.5%) | ✅ 34.5% | ✅ 77.7% |
| 🟠 Breakout | **HYPE** | ▼ Short | 71.8649 → 62.749 | +$126.85 (+25.2%) | ✅ 23.7% | ✅ 63.9% |
| 🟠 Breakout | **ZEC** | ▼ Short | 1,003.70 → 741.21 | +$261.52 (+52.0%) | ✅ 46.2% | ✅ 93.8% |
| 🟠 Breakout | **UNI** | ▼ Short | 6.1326 → 4.7699 | +$222.21 (+44.5%) | ✅ 38.9% | ✅ 83.6% |
| 🟠 Breakout | **BNB** | ▼ Short | 632.05 → 547.31 | +$134.08 (+26.8%) | ✅ 24.7% | ✅ 65.1% |
| 🟠 Breakout | **AAVE** | ▼ Short | 111.00 → 95.044 | +$143.77 (+28.8%) | ✅ 26.1% | ✅ 66.8% |
| 🟠 Breakout | **XMR** | ▼ Short | 490.83 → 497.02 | −$12.61 (−2.5%) | ✅ 6.7% | ✅ 34.9% |
| 🟠 Breakout | **kPEPE** | ▼ Short | 0.003924 → 0.003484 | +$112.13 (+22.5%) | ✅ 21.6% | ✅ 60.8% |
| 🟠 Breakout | **ZRO** | ▼ Short | 1.4562 → 1.0618 | +$270.84 (+54.0%) | ✅ 48.1% | ✅ 87.2% |
| 🟠 Breakout | **VVV** | ▲ Long | 24.993 → 25.198 | +$8.20 (+1.6%) | ✅ 8.7% | ✅ 40.4% |
| 🟢 Momentum | **WLD** | ▼ Short | 0.38553 → 0.23585 | +$388.24 (+78.9%) | ✅ 76.5% | ✅ 132.2% |
| 🟢 Momentum | **ENA** | ▼ Short | 0.14951 → 0.098994 | +$337.89 (+67.3%) | ✅ 63.1% | ✅ 116.1% |
| 🟢 Momentum | **VVV** | ▲ Long | 20.0544 → 25.198 | +$256.48 (+51.8%) | ✅ 26.8% | ✅ 51.8% |
| 🟢 Momentum | **PUMP** | ▼ Short | 0.00287 → 0.002451 | +$145.99 (+29.1%) | ✅ 26.5% | ✅ 67.4% |
| 🟢 Momentum | **UNI** | ▼ Short | 5.1601 → 4.7699 | +$75.62 (+15.1%) | ✅ 16.8% | ✅ 54.5% |
| 🟠 Breakout (spot) | **VVV** | ▲ Long | 24.9223 → 25.198 | +$3.01 (+0.6%) | ✅ 9.0% | not on Alpaca |
| 🟢 Momentum (spot) | **VVV** | ▲ Long | 20.0503 → 25.198 | +$125.23 (+25.0%) | ✅ 26.8% | not on Alpaca |
| 🟢 Momentum (spot) | **XRP** | ▲ Long | 0.9366 → 0.9337 | −$4.04 (−0.8%) | ✅ 7.7% | ✅ copied |
| 🟢 Momentum (spot) | **HYPE** | ▲ Long | 62.8598 → 62.77 | −$3.21 (−0.6%) | ✅ 7.9% | 🔴 copy failed |
| 🟢 Momentum (spot) | **LINK** | ▲ Long | 8.9148 → 8.982 | +$1.26 (+0.3%) | ✅ 8.7% | ✅ copied |
| 🟢 Momentum (spot) | **XPL** | ▲ Long | 0.0454 → 0.0452 | −$4.69 (−0.9%) | ✅ 7.6% | not on Alpaca |

_Distance = how far the price can still move against the position. ✅ over 5% · ⚠️ 2–5% · 🔴 under 2%. Spot can't be liquidated; its last column shows whether the trade is copied to Alpaca._

### Recent trades

| Time (PKT) | Strategy | Coin | What | Price | Result |
|---|---|---|---|--:|--:|
| Mon 23 Nov, 19:00 | 🔵 MA | **kPEPE** | Stopped out | 0.0036957 | −$80.59 |
| Mon 23 Nov, 18:00 | 🔵 MA | **XMR** | Stopped out | 517.36 | −$78.99 |
| Mon 23 Nov, 18:00 | 🟠 Breakout | **AVAX** | Stopped out | 6.8099 | −$81.62 |
| Mon 23 Nov, 18:00 | 🟠 Breakout | **DOGE** | Stopped out | 0.057597 | −$80.14 |
| Mon 23 Nov, 12:45 | 🟢 Momentum (spot) | **XRP** | Bought | 0.9366 | fee $1.25 |
| Mon 23 Nov, 12:45 | 🟢 Momentum (spot) | **HYPE** | Bought | 62.8598 | fee $1.25 |
| Mon 23 Nov, 12:45 | 🟢 Momentum (spot) | **LINK** | Bought | 8.9148 | fee $1.25 |
| Mon 23 Nov, 12:45 | 🟢 Momentum (spot) | **XPL** | Bought | 0.0454 | fee $1.25 |
| Mon 23 Nov, 12:44 | 🔵 MA | **SUI** | Closed | 0.66734 | +$255.80 |
| Mon 23 Nov, 12:44 | 🔵 MA | **kPEPE** | Opened short | 0.0034219 | fee $0.45 |
| Mon 23 Nov, 09:00 | 🟠 Breakout | **GRAM** | Stopped out | 0.99222 | −$82.07 |
| Sun 22 Nov, 11:54 | 🟠 Breakout | **VVV** | Opened long | 24.993 | fee $0.45 |
| Sun 22 Nov, 11:54 | 🟠 Breakout (spot) | **VVV** | Bought | 24.9223 | fee $1.25 |
| Sat 21 Nov, 20:00 | 🟢 Momentum (spot) | **LIT** | Stopped out | 0.070261 | −$42.30 |
| Sat 21 Nov, 12:14 | 🟠 Breakout | **AVAX** | Opened short | 6.3055 | fee $0.45 |

### Signal board (daily candle of 2026-11-23)

What each strategy sees per coin. 🔔 = the condition for a trade is met.

| Coin | MA: 20d vs 50d | Breakout: vs 20-day range | Momentum: 14d return |
|---|---|---|---|
| **HYPE** | below (−9.6%) | +39.4% to high / −12.5% to low | −15.2% (#4) 🔔 top 5: long |
| **ZEC** | below (−12.0%) | +79.1% to high / −12.4% to low | −33.3% (#19) 🔔 bottom 5: short |
| **SOL** | below (−16.1%) | +36.3% to high / −9.9% to low | −16.9% (#8) |
| **XRP** | below (−14.8%) | +42.8% to high / −8.5% to low | −14.4% (#3) 🔔 top 5: long |
| **NEAR** | below (−20.3%) | +43.2% to high / −14.6% to low | −17.8% (#9) |
| **LIT** | below (−6.1%) | +47.2% to high / −11.1% to low | −24.9% (#13) |
| **XMR** | below (−4.2%) | +33.1% to high / −13.4% to low | −16.7% (#7) |
| **PUMP** | below (−23.2%) | +80.3% to high / −13.7% to low | −30.0% (#16) 🔔 bottom 5: short |
| **VVV** | below (−7.8%) | +8.7% to high / −32.0% to low | +13.1% (#1) 🔔 top 5: long |
| **kPEPE** | below (−1.5%) | +64.2% to high / −7.5% to low | −33.2% (#18) 🔔 bottom 5: short |
| **AAVE** | below (−15.7%) | +40.9% to high / −6.4% to low | −26.1% (#15) |
| **UNI** | below (−13.5%) | +61.5% to high / −13.6% to low | −30.7% (#17) 🔔 bottom 5: short |
| **ENA** | below (−24.8%) | +88.2% to high / −11.3% to low | −34.0% (#20) 🔔 bottom 5: short |
| **DOGE** | below (−14.2%) | +39.0% to high / −9.9% to low | −19.5% (#10) |
| **WLD** | below (−29.4%) | +68.3% to high / −12.5% to low | −25.1% (#14) |
| **BNB** | below (−9.3%) | +29.9% to high / −9.6% to low | −19.5% (#11) |
| **ZRO** | below (−15.5%) | +69.9% to high / −7.7% to low | −22.5% (#12) |
| **LINK** | below (−13.0%) | +30.9% to high / −11.7% to low | −15.5% (#5) 🔔 top 5: long |
| **ADA** | below (−17.2%) | +35.8% to high / −10.3% to low | −16.3% (#6) |
| **XPL** | below (−26.2%) | +46.7% to high / −12.7% to low | −11.4% (#2) 🔔 top 5: long |

_Momentum trades its top/bottom 5 at the Monday rebalance; MA and breakout act at each daily run. Spot uses the same signals but only buys: a short signal just sells what it holds._

### This week's coins (chosen 2026-11-23)

HYPE · ZEC · SOL · XRP · NEAR · LIT · XMR · PUMP · VVV · kPEPE · AAVE · UNI · ENA · DOGE · WLD · BNB · ZRO · LINK · ADA · XPL

_The 20 most-traded Hyperliquid futures over the past week, excluding BTC and ETH. Refreshed Mondays 00:00 UTC (5:00 AM PKT)._

## Alpaca paper account

Value **$49,323.05** · cash $45,449.84 · account ending YUU8  
Holding: 55.9462 LINKUSD (+$5.71), 2 MU (−$540.14), 7e-09 PEPEUSD ($0.00), 532.511 XRPUSD (−$2.76)

**2** simulated spot trade(s) copied and open · 🔴 1 copy error(s): see the spot log. Copies use the same number of coins as the simulation, with a real stop order on Alpaca.

Crypto spot bot: no coins on its watchlist yet (daily 00:15 UTC). Stock bot: stopped.

---
✅ Last run OK · [futures log](logs/futures_bot.log) · [spot log](logs/spot_bot.log) · [project log](PROJECT_LOG.md) · on the PC: `python dashboard.py`

<sub>This page is written by summary.py; edits by hand are overwritten.</sub>
