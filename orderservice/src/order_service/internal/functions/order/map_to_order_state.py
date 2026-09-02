"""User-owned function implementation. The generator never overwrites this file."""

from pyservicelib_gorundebug.runtime.config.stream_types import MapStreamConfig
from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment
from order_service.models.order import Order
from order_service.models.order_state import OrderState
from pyservicelib_gorundebug.runtime.common import Collect, Stream


class MapToOrderState:
    """Produce a TIMED_OUT order result that preserves the order ID and submitted total.
    Do not add item results at this stage; results received before the timeout are included in the final response."""

    async def map(
        self,
        stream: Stream,
        value: Order,
        out: Collect[OrderState],
    ) -> None:
        del stream
        await out.out(
            OrderState(
                order_id=value.id,
                status="TIMED_OUT",
                total_amount=value.total_amount,
            )
        )


async def make_map_to_order_state(
    ctx: Context, environment: ServiceEnvironment, config: MapStreamConfig
) -> MapToOrderState:
    del ctx, environment, config
    return MapToOrderState()
