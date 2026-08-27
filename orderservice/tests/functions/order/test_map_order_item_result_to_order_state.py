"""User-owned tests for MapOrderItemResultToOrderState."""

from order_service.internal.functions.order.map_order_item_result_to_order_state import MapOrderItemResultToOrderState


def test_map_order_item_result_to_order_state_contract_surface() -> None:
    function = MapOrderItemResultToOrderState()
    assert callable(function.map)