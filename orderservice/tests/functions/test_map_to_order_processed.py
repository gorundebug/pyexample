"""User-owned tests for MapToOrderProcessed."""

import asyncio
from datetime import datetime, timezone
from typing import Any

from model.models.order_item_result import OrderItemResult
from order_service.internal.functions.map_to_order_processed import MapToOrderProcessed
from order_service.models.order_state import OrderState


def test_map_to_order_processed_converts_final_state() -> None:
    function = MapToOrderProcessed()
    collected: list[Any] = []

    class Collector:
        async def out(self, value: Any) -> None:
            collected.append(value)

    processed_at = datetime(2026, 8, 16, 12, 30, tzinfo=timezone.utc)
    value = OrderState(
        order_id="order-123",
        status="PARTIALLY_CONFIRMED",
        confirmed_items=[
            OrderItemResult("order-123", "item-1", "SKU-1", 1, 1, True, "CONFIRMED"),
            OrderItemResult("order-123", "item-2", "SKU-2", 1, 0, False, "OUT_OF_STOCK"),
        ],
        processed_at=processed_at,
    )

    asyncio.run(function.map(None, value, Collector()))  # type: ignore[arg-type]

    assert len(collected) == 1
    assert collected[0].order_id == "order-123"
    assert collected[0].status == "PARTIALLY_CONFIRMED"
    assert collected[0].processed_at == processed_at
    assert collected[0].total_items == 2
    assert collected[0].confirmed_items == 1
    assert collected[0].failure_reason == "PARTIALLY_CONFIRMED"
