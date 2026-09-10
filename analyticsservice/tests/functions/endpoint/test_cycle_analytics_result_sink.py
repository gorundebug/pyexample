"""User-owned tests for CycleAnalyticsResultSink."""

from analytics_service.internal.functions.endpoint.cycle_analytics_result_sink import CycleAnalyticsResultSink


def test_cycle_analytics_result_sink_contract_surface() -> None:
    function = CycleAnalyticsResultSink()
    assert callable(function.get_stream_id)
    assert callable(function.begin_request)
    assert callable(function.consume_message)
    assert callable(function.end_request)