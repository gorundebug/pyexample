"""User-owned function implementation. The generator never overwrites this file."""
import asyncio

from model.models.order_item import OrderItem
from model.models.order_item_result import OrderItemResult
from pyservicelib_gorundebug.runtime.common import Collect, Stream


class GetInventoryItemData:
    """Look up the inventory record by OrderItem.SKU; retrieve current stock and UnitPrice from the record.
Always copy OrderID, ItemID, SKU, RequestedQty (=OrderItem.Quantity), UnitPrice into the result.
If stock >= OrderItem.Quantity: reserve the stock atomically and emit
OrderItemResult{OrderID, ItemID, SKU, RequestedQty, UnitPrice, Reserved: true, Status: CONFIRMED, AvailableQty: OrderItem.Quantity} via out.
If stock is insufficient: emit
OrderItemResult{OrderID, ItemID, SKU, RequestedQty, UnitPrice, Reserved: false, Status: OUT_OF_STOCK, AvailableQty: actual available} via rout."""

    def __init__(self, stock: dict[str, int] | None = None) -> None:
        self._stock = dict(
            stock
            if stock is not None
            else {"SKU-001": 100, "SKU-002": 50, "SKU-003": 25}
        )
        self._lock = asyncio.Lock()

    async def process(
        self,
        stream: Stream,
        value: OrderItem,
        out: Collect[OrderItemResult],
        err_out: Collect[OrderItemResult],
    ) -> None:
        del stream
        async with self._lock:
            available = self._stock.get(value.sku, 0)
            reserved = available >= value.quantity
            if reserved:
                self._stock[value.sku] = available - value.quantity

        result = OrderItemResult(
            order_id=value.order_id,
            item_id=value.item_id,
            sku=value.sku,
            requested_qty=value.quantity,
            available_qty=value.quantity if reserved else available,
            reserved=reserved,
            status="CONFIRMED" if reserved else "OUT_OF_STOCK",
            unit_price=value.unit_price,
        )
        await (out if reserved else err_out).out(result)
