"""User-owned function implementation. The generator never overwrites this file."""
from order_service.models.order import Order
from order_service.models.order_state import OrderState
from pyservicelib_gorundebug.runtime.common import Collect, Stream


class MapToOrderState:
    """Convert an Order that reached the soft deadline into an OrderState.
Set OrderID from Order.ID; set Status to TIMED_OUT; leave ConfirmedItems nil."""

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
