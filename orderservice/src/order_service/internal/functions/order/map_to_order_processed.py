"""User-owned function implementation. The generator never overwrites this file."""

from datetime import datetime, timezone

from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment
from pyservicelib_gorundebug.runtime.config.stream_types import MapStreamConfig
from model.models.order_processed import OrderProcessed
from order_service.models.order_state import OrderState
from pyservicelib_gorundebug.runtime.common import Collect, Stream


class MapToOrderProcessed:
    """Convert the final order state into the event published to Kafka."""

    async def map(
        self,
        stream: Stream,
        value: OrderState,
        out: Collect[OrderProcessed],
    ) -> None:
        del stream
        confirmed_items = sum(1 for item in value.confirmed_items if item.reserved)
        await out.out(
            OrderProcessed(
                order_id=value.order_id,
                status=value.status,
                # Go forwards the zero time carried by the timeout branch.
                # Python models it explicitly because datetime has no value-type zero.
                processed_at=value.processed_at or datetime.min.replace(tzinfo=timezone.utc),
                total_items=len(value.confirmed_items),
                confirmed_items=confirmed_items,
                failure_reason="" if value.status == "CONFIRMED" else value.status,
            )
        )


def make_map_to_order_processed(
    ctx: Context,
    environment: ServiceEnvironment,
    config: MapStreamConfig,
) -> MapToOrderProcessed:
    """Construct MapToOrderProcessed for the configured service graph."""
    del ctx, config, environment
    return MapToOrderProcessed()
