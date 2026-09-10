"""User-owned tests for CycleAnalyticsInputSource."""

from analytics_service.internal.functions.endpoint.cycle_analytics_input_source import CycleAnalyticsInputSource


def test_cycle_analytics_input_source_contract_surface() -> None:
    function = CycleAnalyticsInputSource()
    assert callable(function.concurrency)
    assert callable(function.begin_request)
    assert callable(function.consume_message)
    assert callable(function.get_message_id)
    assert callable(function.end_request)