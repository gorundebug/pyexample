"""User-owned tests for MapToOrderState."""

from order_service.internal.functions.map_to_order_state import MapToOrderState


def test_map_to_order_state_contract_surface() -> None:
    function = MapToOrderState()
    assert callable(function.map)