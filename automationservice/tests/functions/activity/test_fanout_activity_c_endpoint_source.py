"""User-owned tests for FanoutActivityCEndpointSource."""

from automation_service.internal.functions.activity.fanout_activity_c_endpoint_source import FanoutActivityCEndpointSource


def test_fanout_activity_c_endpoint_source_contract_surface() -> None:
    function = FanoutActivityCEndpointSource()
    assert callable(function.begin_request)
    assert callable(function.consume_message)
    assert callable(function.end_request)
