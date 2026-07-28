"""User-owned tests for ProcessOrderItem."""

from order_service.internal.functions.process_order_item import ProcessOrderItem


def test_process_order_item_contract_surface() -> None:
    function = ProcessOrderItem()
    assert callable(function.begin_request)
    assert callable(function.consume_message)
    assert callable(function.handle_response)
    assert callable(function.end_request)