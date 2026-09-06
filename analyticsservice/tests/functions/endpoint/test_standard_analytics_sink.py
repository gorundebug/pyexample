"""User-owned tests for StandardAnalyticsSink."""

from analytics_service.internal.functions.endpoint.standard_analytics_sink import StandardAnalyticsSink


def test_standard_analytics_sink_contract_surface() -> None:
    function = StandardAnalyticsSink()
    assert callable(function.get_stream_id)
    assert callable(function.begin_request)
    assert callable(function.consume_message)
    assert callable(function.end_request)