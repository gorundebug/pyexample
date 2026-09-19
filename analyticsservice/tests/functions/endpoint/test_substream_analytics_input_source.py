"""User-owned tests for SubstreamAnalyticsInputSource."""

from analytics_service.internal.functions.endpoint.substream_analytics_input_source import SubstreamAnalyticsInputSource


def test_substream_analytics_input_source_contract_surface() -> None:
    function = SubstreamAnalyticsInputSource()
    assert callable(function.concurrency)
    assert callable(function.begin_request)
    assert callable(function.consume_message)
    assert callable(function.get_message_id)
    assert callable(function.end_request)