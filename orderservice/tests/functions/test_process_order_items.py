"""User-owned tests for ProcessOrderItems."""

from order_service.internal.functions.process_order_items import ProcessOrderItems


def test_process_order_items_contract_surface() -> None:
    function = ProcessOrderItems()
    assert callable(function.flatmap)