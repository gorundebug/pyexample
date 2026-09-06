"""User-owned tests for HighValueAnalyticsSink."""

from analytics_service.internal.functions.endpoint.high_value_analytics_sink import HighValueAnalyticsSink


def test_high_value_analytics_sink_contract_surface() -> None:
    function = HighValueAnalyticsSink()
    assert callable(function.get_stream_id)
    assert callable(function.begin_request)
    assert callable(function.consume_message)
    assert callable(function.end_request)