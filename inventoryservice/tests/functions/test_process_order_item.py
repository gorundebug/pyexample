"""User-owned tests for ProcessOrderItem."""

from inventory_service.internal.functions.process_order_item import ProcessOrderItem


def test_process_order_item_contract_surface() -> None:
    function = ProcessOrderItem()
    assert callable(function.begin_request)
    assert callable(function.consume_message)
    assert callable(function.get_message_id)
    assert callable(function.eof)
    assert callable(function.end_request)