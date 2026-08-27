"""User-owned tests for ActivityJobEndpointSink."""

from automation_service.internal.functions.activity.activity_job_endpoint_sink import ActivityJobEndpointSink


def test_activity_job_endpoint_sink_contract_surface() -> None:
    function = ActivityJobEndpointSink()