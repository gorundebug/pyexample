"""User-owned function implementation. The generator never overwrites this file."""

from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment
from pyservicelib_gorundebug.runtime.config.stream_types import MapStreamConfig
from model.models.order_item_result import OrderItemResult
from pyservicelib_gorundebug.runtime.common import Collect, Stream
from .get_inventory_item_data import InventoryFailureError
class GetInventoryItemError:
    """When inventory processing fails, return an OUT_OF_STOCK result with no available quantity.
Preserve the order and item identity and requested quantity, and record the failure."""

    async def map(
        self,
        stream: Stream,
        value: Exception,
        out: Collect[OrderItemResult],
    ) -> None:
        del stream
        failure = value if isinstance(value, InventoryFailureError) else None
        await out.out(OrderItemResult(
            order_id=failure.item.order_id if failure else "",
            item_id=failure.item.item_id if failure else "",
            sku=failure.item.sku if failure else "",
            requested_qty=failure.item.quantity if failure else 0,
            available_qty=failure.available_qty if failure else 0,
            reserved=False,
            status="OUT_OF_STOCK" if failure else "PROCESSING_ERROR",
            unit_price=failure.item.unit_price if failure else 0.0,
            error=str(value),
        ))


async def make_get_inventory_item_error(
    ctx: Context,
    environment: ServiceEnvironment,
    config: MapStreamConfig,
) -> GetInventoryItemError:
    """Construct GetInventoryItemError asynchronously while the graph is initialized."""
    del ctx, config, environment
    return GetInventoryItemError()
