"""User-owned tests for JoinedAnalyticsSink."""

from analytics_service.internal.functions.endpoint.joined_analytics_sink import JoinedAnalyticsSink


def test_joined_analytics_sink_contract_surface() -> None:
    function = JoinedAnalyticsSink()
    assert callable(function.get_stream_id)
    assert callable(function.begin_request)
    assert callable(function.consume_message)
    assert callable(function.end_request)