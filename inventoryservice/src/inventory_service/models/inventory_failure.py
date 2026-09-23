"""Inventory shortage data carried by the business error branch."""

from dataclasses import dataclass

from model.models.order_item import OrderItem


@dataclass(slots=True)
class InventoryFailure:
    item: OrderItem
    available_qty: int
