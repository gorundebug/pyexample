"""User-owned tests for FanoutActivityAEndpointSink."""

from automation_service.internal.functions.activity.fanout_activity_a_endpoint_sink import FanoutActivityAEndpointSink


def test_fanout_activity_a_endpoint_sink_contract_surface() -> None:
    function = FanoutActivityAEndpointSink()