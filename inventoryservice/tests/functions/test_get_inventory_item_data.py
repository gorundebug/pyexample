"""User-owned tests for GetInventoryItemData."""

from inventory_service.internal.functions.get_inventory_item_data import GetInventoryItemData


def test_get_inventory_item_data_contract_surface() -> None:
    function = GetInventoryItemData()
    assert callable(function.process)