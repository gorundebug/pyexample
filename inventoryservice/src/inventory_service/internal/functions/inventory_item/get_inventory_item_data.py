"""User-owned function implementation. The generator never overwrites this file."""

from pyservicelib_gorundebug.runtime.config.stream_types import ProcessStreamConfig
from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment

from model.models.order_item import OrderItem
from model.models.order_item_result import OrderItemResult
from pyservicelib_gorundebug.runtime.common import Collect, Stream


class GetInventoryItemData:
    """Reserve the requested quantity without allowing concurrent orders to overdraw stock.
    On success, return CONFIRMED with the requested quantity available. Otherwise return OUT_OF_STOCK with the current available quantity.
    Preserve the order and item identity, requested quantity, and unit price.
    The example starts with SKU-001: 100, SKU-002: 50, and SKU-003: 25."""

    def __init__(self, stock: dict[str, int] | None = None) -> None:
        self._stock = dict(
            stock if stock is not None else {"SKU-001": 100, "SKU-002": 50, "SKU-003": 25}
        )

    async def process(
        self,
        stream: Stream,
        value: OrderItem,
        out: Collect[OrderItemResult],
        err_out: Collect[OrderItemResult],
    ) -> None:
        del stream
        # This block contains no await, so it is uninterrupted on the
        # service's single asyncio event loop without an asyncio.Lock.
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


async def make_get_inventory_item_data(
    ctx: Context, environment: ServiceEnvironment, config: ProcessStreamConfig
) -> GetInventoryItemData:
    del ctx, environment, config
    return GetInventoryItemData()
