"""User-owned tests for FanoutActivityCEndpointSink."""

from automation_service.internal.functions.activity.fanout_activity_c_endpoint_sink import FanoutActivityCEndpointSink


def test_fanout_activity_c_endpoint_sink_contract_surface() -> None:
    function = FanoutActivityCEndpointSink()