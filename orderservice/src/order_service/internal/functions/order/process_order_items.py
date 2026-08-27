"""User-owned function implementation. The generator never overwrites this file."""

from pyservicelib_gorundebug.runtime.config.stream_types import FlatMapStreamConfig
from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment
from dataclasses import replace

from model.models.order_item import OrderItem
from order_service.models.order import Order
from pyservicelib_gorundebug.runtime.common import Collect, Stream


class ProcessOrderItems:
    """Emit every order item independently for inventory processing.
    Preserve each item's data and assign the parent order ID."""

    async def flatmap(
        self,
        stream: Stream,
        value: Order,
        out: Collect[OrderItem],
    ) -> None:
        del stream
        for item in value.items:
            await out.out(replace(item, order_id=value.id))


def make_process_order_items(
    ctx: Context, environment: ServiceEnvironment, config: FlatMapStreamConfig
) -> ProcessOrderItems:
    del ctx, environment, config
    return ProcessOrderItems()
