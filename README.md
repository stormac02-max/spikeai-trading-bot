# SpikeAI paper trading

_Updated **Wed 25 Nov 2026, 13:41 PKT** (Wed 03:41 ET). Refreshed after every daily run. Paper trading only: no real money._

## Strategy test: MA crossover vs breakout vs momentum

**32 days left** in the evaluation (until 2026-12-27), then the best strategy is kept.  
Each simulated account started with $10,000. Futures: 2x, long and short, $500 margin per trade. Spot: 1x, buy-only, $500 per buy, copied to Alpaca for coins it lists. Both use an 8% stop.

### Futures

| Strategy | Value | Return | Below peak | Open | Closed (won) | Fees | Funding |
|---|--:|--:|--:|--:|--:|--:|--:|
| 🔵 MA crossover 20/50 | **$11,160.30** | +11.60% | −2.53% | 3 | 3 (1) | $4.01 | −$1.15 |
| 🟠 Breakout 20/10 | **$13,212.19** | +32.12% | −3.82% | 16 | 10 (2) | $16.28 | +$5.85 |
| 🟢 Momentum 14d, 5 long/5 short | **$10,981.11** | +9.81% | −0.21% | 5 | 20 (6) | $19.48 | −$10.75 |

**Futures leader:** 🟠 Breakout 20/10, $2,051.90 ahead of MA crossover 20/50.

### Spot

| Strategy | Value | Return | Below peak | Held | Closed (won) | Fees | On Alpaca |
|---|--:|--:|--:|--:|--:|--:|--:|
| 🔵 MA crossover 20/50 | **$10,000.00** | 0.00% | at peak | 0 | 0 | $0.00 | 0 |
| 🟠 Breakout 20/10 | **$9,995.08** | −0.05% | −0.26% | 1 | 0 | $1.25 | 0 |
| 🟢 Momentum 14d, 5 long/5 short | **$9,550.56** | −4.49% | −4.49% | 5 | 12 (0) | $35.02 | 2 |

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
| 2026-11-24 | $11,161.99 | $13,215.80 | $10,981.81 | $10,000.00 | $9,995.08 | $9,550.56 |
| now | $11,160.30 | $13,212.19 | $10,981.11 | $10,000.00 | $9,995.08 | $9,550.56 |

</details>

### Open positions

| Strategy | Coin | Side | Entry → now | Profit | To stop | To liquidation / Alpaca |
|---|---|---|---|--:|--:|--:|
| 🔵 MA | **WLD** | ▼ Short | 0.38553 → 0.23109 | +$400.59 (+81.6%) | ✅ 80.2% | ✅ 136.9% |
| 🔵 MA | **NEAR** | ▼ Short | 4.0459 → 2.8664 | +$291.53 (+58.0%) | ✅ 52.4% | ✅ 102.0% |
| 🔵 MA | **ZRO** | ▼ Short | 1.6048 → 0.99906 | +$377.46 (+75.0%) | ✅ 73.5% | ✅ 119.5% |
| 🟠 Breakout | **SOL** | ▼ Short | 91.244 → 68.001 | +$254.73 (+50.9%) | ✅ 44.9% | ✅ 96.4% |
| 🟠 Breakout | **NEAR** | ▼ Short | 3.6822 → 2.8664 | +$221.55 (+44.1%) | ✅ 38.7% | ✅ 83.9% |
| 🟠 Breakout | **ENA** | ▼ Short | 0.1646 → 0.095732 | +$418.39 (+83.2%) | ✅ 85.7% | ✅ 146.1% |
| 🟠 Breakout | **WLD** | ▼ Short | 0.34441 → 0.23109 | +$329.03 (+67.0%) | ✅ 61.0% | ✅ 111.7% |
| 🟠 Breakout | **XRP** | ▼ Short | 1.1619 → 0.92398 | +$204.77 (+41.0%) | ✅ 35.8% | ✅ 84.0% |
| 🟠 Breakout | **PUMP** | ▼ Short | 0.003674 → 0.002386 | +$350.57 (+69.8%) | ✅ 66.3% | ✅ 120.3% |
| 🟠 Breakout | **SUI** | ▼ Short | 0.81988 → 0.64369 | +$214.90 (+43.1%) | ✅ 37.6% | ✅ 81.7% |
| 🟠 Breakout | **HYPE** | ▼ Short | 71.8649 → 58.681 | +$183.45 (+36.5%) | ✅ 32.3% | ✅ 75.3% |
| 🟠 Breakout | **ZEC** | ▼ Short | 1,003.70 → 731.96 | +$270.74 (+53.8%) | ✅ 48.1% | ✅ 96.3% |
| 🟠 Breakout | **UNI** | ▼ Short | 6.1326 → 4.5553 | +$257.20 (+51.5%) | ✅ 45.4% | ✅ 92.3% |
| 🟠 Breakout | **BNB** | ▼ Short | 632.05 → 542.46 | +$141.75 (+28.3%) | ✅ 25.8% | ✅ 66.6% |
| 🟠 Breakout | **AAVE** | ▼ Short | 111.00 → 92.369 | +$167.87 (+33.6%) | ✅ 29.8% | ✅ 71.6% |
| 🟠 Breakout | **XMR** | ▼ Short | 490.83 → 506.95 | −$32.84 (−6.5%) | ⚠️ 4.6% | ✅ 32.2% |
| 🟠 Breakout | **kPEPE** | ▼ Short | 0.003924 → 0.003475 | +$114.42 (+23.0%) | ✅ 22.0% | ✅ 61.1% |
| 🟠 Breakout | **ZRO** | ▼ Short | 1.4562 → 0.99906 | +$313.92 (+62.5%) | ✅ 57.4% | ✅ 99.0% |
| 🟠 Breakout | **VVV** | ▲ Long | 24.993 → 24.796 | −$7.88 (−1.6%) | ✅ 7.3% | ✅ 39.4% |
| 🟢 Momentum | **WLD** | ▼ Short | 0.38553 → 0.23109 | +$400.59 (+81.6%) | ✅ 80.2% | ✅ 136.9% |
| 🟢 Momentum | **ENA** | ▼ Short | 0.14951 → 0.095732 | +$359.70 (+71.6%) | ✅ 68.7% | ✅ 123.4% |
| 🟢 Momentum | **VVV** | ▲ Long | 20.0544 → 24.796 | +$236.44 (+47.8%) | ✅ 25.6% | ✅ 51.0% |
| 🟢 Momentum | **PUMP** | ▼ Short | 0.00287 → 0.002386 | +$168.64 (+33.6%) | ✅ 29.9% | ✅ 72.0% |
| 🟢 Momentum | **UNI** | ▼ Short | 5.1601 → 4.5553 | +$117.21 (+23.4%) | ✅ 22.3% | ✅ 61.8% |
| 🟠 Breakout (spot) | **VVV** | ▲ Long | 24.9223 → 24.739 | −$6.16 (−1.2%) | ✅ 7.3% | not on Alpaca |
| 🟢 Momentum (spot) | **VVV** | ▲ Long | 20.0503 → 24.739 | +$113.84 (+22.8%) | ✅ 25.4% | not on Alpaca |
| 🟢 Momentum (spot) | **XRP** | ▲ Long | 0.9366 → 0.92344 | −$9.49 (−1.9%) | ✅ 6.7% | ✅ copied |
| 🟢 Momentum (spot) | **HYPE** | ▲ Long | 62.8598 → 58.66 | −$35.74 (−7.1%) | 🔴 1.4% | 🔴 copy failed |
| 🟢 Momentum (spot) | **LINK** | ▲ Long | 8.9148 → 8.741 | −$12.20 (−2.4%) | ✅ 6.2% | ✅ copied |
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

### Signal board (daily candle of 2026-11-24)

What each strategy sees per coin. 🔔 = the condition for a trade is met.

| Coin | MA: 20d vs 50d | Breakout: vs 20-day range | Momentum: 14d return |
|---|---|---|---|
| **HYPE** | below (−10.3%) | +48.3% to high / −6.9% to low | −17.1% (#8) |
| **ZEC** | below (−13.5%) | +88.1% to high / −8.0% to low | −29.2% (#14) |
| **SOL** | below (−16.5%) | +40.9% to high / −6.9% to low | −16.4% (#6) |
| **XRP** | below (−15.5%) | +45.1% to high / −7.0% to low | −12.4% (#3) 🔔 top 5: long |
| **NEAR** | below (−20.7%) | +48.0% to high / −11.7% to low | −19.5% (#11) |
| **LIT** | below (−6.6%) | +49.9% to high / −9.5% to low | −31.3% (#17) 🔔 bottom 5: short |
| **XMR** | below (−5.2%) | +26.9% to high / −17.3% to low | −9.4% (#2) 🔔 top 5: long |
| **PUMP** | below (−23.9%) | +86.9% to high / −10.6% to low | −30.4% (#16) 🔔 bottom 5: short |
| **VVV** | below (−6.8%) | +9.8% to high / −32.3% to low | +27.8% (#1) 🔔 top 5: long |
| **kPEPE** | below (−2.8%) | +63.0% to high / −8.2% to low | −35.9% (#20) 🔔 bottom 5: short |
| **AAVE** | below (−16.0%) | +45.7% to high / −3.2% to low | −23.9% (#12) |
| **UNI** | below (−14.5%) | +65.7% to high / −11.3% to low | −29.2% (#15) |
| **ENA** | below (−25.9%) | +93.7% to high / −8.7% to low | −34.5% (#19) 🔔 bottom 5: short |
| **DOGE** | below (−14.7%) | +41.7% to high / −8.2% to low | −18.7% (#9) |
| **WLD** | below (−29.9%) | +70.5% to high / −11.3% to low | −24.3% (#13) |
| **BNB** | below (−9.9%) | +31.8% to high / −8.3% to low | −19.4% (#10) |
| **ZRO** | below (−16.7%) | 🔔 below 20d low | −31.7% (#18) 🔔 bottom 5: short |
| **LINK** | below (−13.4%) | +33.3% to high / −10.1% to low | −14.0% (#4) 🔔 top 5: long |
| **ADA** | below (−17.5%) | +39.6% to high / −7.8% to low | −16.9% (#7) |
| **XPL** | below (−26.5%) | +52.5% to high / −9.2% to low | −15.7% (#5) 🔔 top 5: long |

_Momentum trades its top/bottom 5 at the Monday rebalance; MA and breakout act at each daily run. Spot uses the same signals but only buys: a short signal just sells what it holds._

### This week's coins (chosen 2026-11-23)

HYPE · ZEC · SOL · XRP · NEAR · LIT · XMR · PUMP · VVV · kPEPE · AAVE · UNI · ENA · DOGE · WLD · BNB · ZRO · LINK · ADA · XPL

_The 20 most-traded Hyperliquid futures over the past week, excluding BTC and ETH. Refreshed Mondays 00:00 UTC (5:00 AM PKT)._

## Alpaca paper account

Value **$49,180.52** · cash $45,449.84 · account ending YUU8  
Holding: 55.9462 LINKUSD (−$9.43), 2 MU (−$662.26), 7e-09 PEPEUSD ($0.00), 532.511 XRPUSD (−$8.03)

**2** simulated spot trade(s) copied and open · 🔴 1 copy error(s): see the spot log. Copies use the same number of coins as the simulation, with a real stop order on Alpaca.

Crypto spot bot: no coins on its watchlist yet (daily 00:15 UTC). Stock bot: stopped.

---
✅ Last run OK · [futures log](logs/futures_bot.log) · [spot log](logs/spot_bot.log) · [project log](PROJECT_LOG.md) · on the PC: `python dashboard.py`

<sub>This page is written by summary.py; edits by hand are overwritten.</sub>
