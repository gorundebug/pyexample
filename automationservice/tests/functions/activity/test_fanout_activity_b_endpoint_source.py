"""User-owned tests for FanoutActivityBEndpointSource."""

from automation_service.internal.functions.activity.fanout_activity_b_endpoint_source import FanoutActivityBEndpointSource


def test_fanout_activity_b_endpoint_source_contract_surface() -> None:
    function = FanoutActivityBEndpointSource()
    assert callable(function.begin_request)
    assert callable(function.consume_message)
    assert callable(function.end_request)
