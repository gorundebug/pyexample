"""User-owned tests for ProcessOrderItemSource."""

from inventory_service.internal.functions.endpoint.process_order_item_source import ProcessOrderItemSource


def test_process_order_item_source_contract_surface() -> None:
    function = ProcessOrderItemSource()
    assert callable(function.begin_request)
    assert callable(function.consume_message)
    assert callable(function.get_message_id)
    assert callable(function.eof)
    assert callable(function.end_request)