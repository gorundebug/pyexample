"""Translate a typed inventory shortage into the same business response."""

import asyncio

from inventory_service.internal.functions.inventory_item.get_inventory_item_error import GetInventoryItemError
from inventory_service.models.inventory_failure import InventoryFailure
from model.models.order_item import OrderItem
from model.models.order_item_result import OrderItemResult


def test_inventory_failure_preserves_fields() -> None:
    results: list[OrderItemResult] = []

    class Collector:
        async def out(self, value: OrderItemResult) -> None:
            results.append(value)

    failure = InventoryFailure(OrderItem(order_id="order-1", item_id="item-1", sku="SKU-001", quantity=3, unit_price=12.5), 2)
    asyncio.run(GetInventoryItemError().map(None, failure, Collector()))
    assert len(results) == 1
    result = results[0]
    assert (result.order_id, result.item_id, result.sku) == ("order-1", "item-1", "SKU-001")
    assert (result.requested_qty, result.available_qty, result.unit_price) == (3, 2, 12.5)
    assert result.reserved is False
    assert result.status == "OUT_OF_STOCK"
    assert result.error == "inventory is out of stock"
