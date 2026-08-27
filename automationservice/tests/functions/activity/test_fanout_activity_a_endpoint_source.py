"""User-owned tests for FanoutActivityAEndpointSource."""

from automation_service.internal.functions.activity.fanout_activity_a_endpoint_source import FanoutActivityAEndpointSource


def test_fanout_activity_a_endpoint_source_contract_surface() -> None:
    function = FanoutActivityAEndpointSource()
    assert callable(function.begin_request)
    assert callable(function.consume_message)
    assert callable(function.end_request)
