"""User-owned function implementation. The generator never overwrites this file."""
from dataclasses import replace

from model.models.order_item import OrderItem
from order_service.models.order import Order
from pyservicelib_gorundebug.runtime.common import Collect, Stream


class ProcessOrderItems:
    """Expand an Order into individual OrderItem messages — one sc.Collect call per element of Order.Items.
Copy Order.ID into each emitted OrderItem.OrderID."""

    async def flatmap(
        self,
        stream: Stream,
        value: Order,
        out: Collect[OrderItem],
    ) -> None:
        del stream
        for item in value.items:
            await out.out(replace(item, order_id=value.id))
