"""The business error branch carries data and must not consume stock."""

import asyncio
from typing import Any

from inventory_service.internal.functions.inventory_item.get_inventory_item_data import GetInventoryItemData
from inventory_service.models.inventory_failure import InventoryFailure
from model.models.order_item import OrderItem


class Collector:
    def __init__(self) -> None:
        self.values: list[Any] = []

    async def out(self, value: Any) -> None:
        self.values.append(value)


def test_reservation_and_shortage_preserve_data() -> None:
    async def run() -> None:
        function = GetInventoryItemData({"SKU-001": 2})
        success, failure = Collector(), Collector()
        item = OrderItem(order_id="order-1", item_id="item-1", sku="SKU-001", quantity=3, unit_price=12.5)
        await function.process(None, item, success, failure)
        assert success.values == []
        assert len(failure.values) == 1
        rejected = failure.values[0]
        assert isinstance(rejected, InventoryFailure)
        assert rejected.item is item
        assert rejected.available_qty == 2
        accepted = OrderItem(order_id="order-1", item_id="item-2", sku="SKU-001", quantity=2, unit_price=12.5)
        await function.process(None, accepted, success, failure)
        assert len(failure.values) == 1
        assert len(success.values) == 1
        assert success.values[0].reserved
        assert success.values[0].available_qty == 2
        assert success.values[0].unit_price == 12.5
    asyncio.run(run())
