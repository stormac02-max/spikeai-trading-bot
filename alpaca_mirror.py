"""Copy the simulated spot trades to the Alpaca paper account, for coins Alpaca lists.

Each simulated buy becomes a "lot" on Alpaca:
- a market buy for the same number of coins (not the same dollars: Alpaca fills dollar-amount crypto
  orders about 2% short, so ordering by quantity keeps both holding exactly the same coins after the
  identical 0.25% fee), and
- a real stop-limit sell order for exactly the coins that buy delivered, at the same stop percentage,
  so the stop works on Alpaca in real time and not only at the next daily run.
Several strategies can hold the same coin; each keeps its own lot and its own stop order.

When the simulation sells (signal, stop-loss or the coin leaving the universe), the lot's stop order is
cancelled and the lot is sold at market. If Alpaca's stop already filled, the lot is simply marked
closed. Prices differ a little between Kraken (the simulation) and Alpaca, so a stop can trigger on one
and not the other; such cases are recorded as "diverged" rather than forced back into line. The
simulation stays the record of each strategy's results.

All orders carry client_order_id "sim-<signal id>[-stop|-sell]", so they're easy to spot in Alpaca and
can't be placed twice for the same signal. Paper account only (TradingClient(..., paper=True)).
"""

import logging
import time
from decimal import ROUND_DOWN, Decimal

from alpaca.common.exceptions import APIError
from alpaca.trading.enums import AssetClass, OrderSide, OrderStatus, TimeInForce
from alpaca.trading.requests import GetAssetsRequest, MarketOrderRequest, StopLimitOrderRequest

log = logging.getLogger("alpaca_mirror")

OPEN_STATUSES = {OrderStatus.NEW, OrderStatus.ACCEPTED, OrderStatus.PENDING_NEW, OrderStatus.PARTIALLY_FILLED,
                 OrderStatus.HELD, OrderStatus.ACCEPTED_FOR_BIDDING, OrderStatus.PENDING_REPLACE}
LIMIT_BUFFER = 0.02  # the stop's limit price sits 2% below the stop, so a fast drop still fills


def round_down(value, increment):
    inc = Decimal(str(increment))
    return float((Decimal(str(value)) / inc).to_integral_value(ROUND_DOWN) * inc)


class AlpacaMirror:
    def __init__(self, client):
        self.client = client
        assets = client.get_all_assets(GetAssetsRequest(asset_class=AssetClass.CRYPTO))
        self.assets = {a.symbol: a for a in assets if a.tradable and a.symbol.endswith("/USD")}

    def supports(self, coin):
        return f"{coin}/USD" in self.assets

    def _held(self, coin):
        for p in self.client.get_all_positions():
            if p.symbol.replace("/", "") == f"{coin}USD":
                return float(p.qty), float(p.qty_available or p.qty)
        return 0.0, 0.0

    def _wait(self, order_id, done, timeout=30):
        """Poll an order until its status is in `done` (or the timeout passes). Returns the order."""
        deadline = time.time() + timeout
        while True:
            order = self.client.get_order_by_id(order_id)
            if order.status in done or time.time() > deadline:
                return order
            time.sleep(1)

    def buy(self, coin, qty, stop_pct, signal_id):
        """Market-buy `qty` coins and place their stop. Returns the lot (a dict saved in the simulation)."""
        symbol, asset = f"{coin}/USD", self.assets[f"{coin}/USD"]
        before, _ = self._held(coin)
        order = self.client.submit_order(MarketOrderRequest(
            symbol=symbol, qty=round_down(qty, asset.min_trade_increment), side=OrderSide.BUY,
            time_in_force=TimeInForce.GTC, client_order_id=f"sim-{signal_id}"))
        order = self._wait(order.id, {OrderStatus.FILLED, OrderStatus.CANCELED, OrderStatus.REJECTED, OrderStatus.EXPIRED})
        if order.status != OrderStatus.FILLED:
            raise RuntimeError(f"Alpaca buy {order.id} ended as {order.status.value}")
        after, _ = self._held(coin)
        qty = round_down(after - before, asset.min_trade_increment)  # what this buy really added, after fees
        price = float(order.filled_avg_price)
        lot = {"symbol": symbol, "qty": qty, "entry": price, "buy_order": str(order.id),
               "stop_order": None, "stop": None, "status": "open"}
        if stop_pct and qty > 0:
            stop = round_down(price * (1 - stop_pct), asset.price_increment)
            limit = round_down(stop * (1 - LIMIT_BUFFER), asset.price_increment)
            stop_order = self.client.submit_order(StopLimitOrderRequest(
                symbol=symbol, qty=qty, side=OrderSide.SELL, time_in_force=TimeInForce.GTC,
                stop_price=stop, limit_price=limit, client_order_id=f"sim-{signal_id}-stop"))
            lot.update(stop_order=str(stop_order.id), stop=stop)
        log.info("Alpaca: bought %.8g %s @ %.6g ($%.2f), stop %s", qty, symbol, price, float(order.filled_qty) * price,
                 f"{lot['stop']:.6g}" if lot["stop"] else "none")
        return lot

    def refresh(self, lot):
        """Mark the lot closed if its Alpaca stop has filled. Returns True if that happened."""
        if lot.get("status") != "open" or not lot.get("stop_order"):
            return False
        order = self.client.get_order_by_id(lot["stop_order"])
        if order.status == OrderStatus.FILLED:
            lot.update(status="stopped on Alpaca", exit=float(order.filled_avg_price))
            return True
        return False

    def sell(self, lot, signal_id):
        """Close the lot: cancel its stop and sell at market, unless Alpaca's stop already closed it."""
        if lot.get("status") != "open":
            return lot
        if self.refresh(lot):
            log.info("Alpaca: %s lot was already closed by its stop @ %.6g", lot["symbol"], lot["exit"])
            return lot
        if lot.get("stop_order"):
            try:
                self.client.cancel_order_by_id(lot["stop_order"])
            except APIError:
                pass  # already gone
            order = self._wait(lot["stop_order"], {OrderStatus.CANCELED, OrderStatus.FILLED, OrderStatus.EXPIRED})
            if order.status == OrderStatus.FILLED:  # filled while we were cancelling it
                lot.update(status="stopped on Alpaca", exit=float(order.filled_avg_price))
                return lot
        coin = lot["symbol"].split("/")[0]
        _, available = self._held(coin)
        qty = round_down(min(lot["qty"], available), self.assets[lot["symbol"]].min_trade_increment)
        if qty <= 0:
            lot.update(status="closed (nothing left on Alpaca)")
            return lot
        order = self.client.submit_order(MarketOrderRequest(
            symbol=lot["symbol"], qty=qty, side=OrderSide.SELL, time_in_force=TimeInForce.GTC,
            client_order_id=f"sim-{signal_id}-sell"))
        order = self._wait(order.id, {OrderStatus.FILLED, OrderStatus.CANCELED, OrderStatus.REJECTED, OrderStatus.EXPIRED})
        if order.status != OrderStatus.FILLED:
            raise RuntimeError(f"Alpaca sell {order.id} ended as {order.status.value}")
        lot.update(status="closed", exit=float(order.filled_avg_price), sell_order=str(order.id))
        log.info("Alpaca: sold %.8g %s @ %.6g", qty, lot["symbol"], lot["exit"])
        return lot
