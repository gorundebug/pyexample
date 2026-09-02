"""User-owned function implementation. The generator never overwrites this file."""

from pyservicelib_gorundebug.runtime.config.stream_types import MapStreamConfig
from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment
from datetime import datetime, timezone

from model.models.order_item_result import OrderItemResult
from order_service.models.order_state import OrderState
from pyservicelib_gorundebug.runtime.common import Collect, Stream


class MapOrderItemResultToOrderState:
    """Produce an order result containing one inventory result and preserving its order ID.
    Mark it CONFIRMED when the item was reserved; otherwise mark it PARTIALLY_CONFIRMED."""

    async def map(
        self,
        stream: Stream,
        value: OrderItemResult,
        out: Collect[OrderState],
    ) -> None:
        del stream
        await out.out(
            OrderState(
                order_id=value.order_id,
                status="CONFIRMED" if value.reserved else "PARTIALLY_CONFIRMED",
                confirmed_items=[value],
                processed_at=datetime.now(timezone.utc),
            )
        )


async def make_map_order_item_result_to_order_state(
    ctx: Context, environment: ServiceEnvironment, config: MapStreamConfig
) -> MapOrderItemResultToOrderState:
    del ctx, environment, config
    return MapOrderItemResultToOrderState()
