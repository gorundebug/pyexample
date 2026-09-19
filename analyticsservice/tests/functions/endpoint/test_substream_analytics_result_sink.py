"""User-owned tests for SubstreamAnalyticsResultSink."""

from analytics_service.internal.functions.endpoint.substream_analytics_result_sink import SubstreamAnalyticsResultSink


def test_substream_analytics_result_sink_contract_surface() -> None:
    function = SubstreamAnalyticsResultSink()
    assert callable(function.get_stream_id)
    assert callable(function.begin_request)
    assert callable(function.consume_message)
    assert callable(function.end_request)