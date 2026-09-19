"""User-owned tests for GetInventoryItemError."""

from inventory_service.internal.functions.inventory_item.get_inventory_item_error import GetInventoryItemError


def test_get_inventory_item_error_contract_surface() -> None:
    function = GetInventoryItemError()
    assert callable(function.map)