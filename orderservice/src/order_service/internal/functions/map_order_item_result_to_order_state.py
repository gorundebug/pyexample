"""User-owned function implementation. The generator never overwrites this file."""
from model.models.order_item_result import OrderItemResult
from order_service.models.order_state import OrderState
from pyservicelib_gorundebug.runtime.common import Collect, Stream


class MapOrderItemResultToOrderState:
    """Convert a single OrderItemResult into an OrderState.
Set OrderID from result.OrderID; set Status=CONFIRMED if result.Reserved==true, otherwise PARTIALLY_CONFIRMED.
Set ConfirmedItems to a single-element slice containing result."""

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
            )
        )
