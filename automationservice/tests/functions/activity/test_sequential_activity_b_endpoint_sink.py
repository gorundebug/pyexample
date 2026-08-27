"""User-owned tests for SequentialActivityBEndpointSink."""

from automation_service.internal.functions.activity.sequential_activity_b_endpoint_sink import SequentialActivityBEndpointSink


def test_sequential_activity_b_endpoint_sink_contract_surface() -> None:
    function = SequentialActivityBEndpointSink()