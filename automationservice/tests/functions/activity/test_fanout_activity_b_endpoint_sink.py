"""User-owned tests for FanoutActivityBEndpointSink."""

from automation_service.internal.functions.activity.fanout_activity_b_endpoint_sink import FanoutActivityBEndpointSink


def test_fanout_activity_b_endpoint_sink_contract_surface() -> None:
    function = FanoutActivityBEndpointSink()