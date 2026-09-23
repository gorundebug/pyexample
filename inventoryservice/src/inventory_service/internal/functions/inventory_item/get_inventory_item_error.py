"""User-owned function implementation. The generator never overwrites this file."""

from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment

from model.models.order_item_result import OrderItemResult
from pyservicelib_gorundebug.runtime.common import Collect, Stream
from inventory_service.models.inventory_failure import InventoryFailure
class GetInventoryItemError:
    """When inventory processing fails, return an OUT_OF_STOCK result with no available quantity.
Preserve the order and item identity and requested quantity, and record the failure."""

    async def map(
        self,
        stream: Stream,
        value: InventoryFailure,
        out: Collect[OrderItemResult],
    ) -> None:
        del stream
        failure = value
        await out.out(OrderItemResult(
            order_id=failure.item.order_id,
            item_id=failure.item.item_id,
            sku=failure.item.sku,
            requested_qty=failure.item.quantity,
            available_qty=failure.available_qty,
            reserved=False,
            status="OUT_OF_STOCK",
            unit_price=failure.item.unit_price,
            error="inventory is out of stock",
        ))


async def make_get_inventory_item_error(
    ctx: Context,
    environment: ServiceEnvironment,
) -> GetInventoryItemError:
    """Construct GetInventoryItemError asynchronously while the graph is initialized."""
    del ctx, environment
    return GetInventoryItemError()
