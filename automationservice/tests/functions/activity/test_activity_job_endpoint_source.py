"""User-owned tests for ActivityJobEndpointSource."""

from automation_service.internal.functions.activity.activity_job_endpoint_source import ActivityJobEndpointSource


def test_activity_job_endpoint_source_contract_surface() -> None:
    function = ActivityJobEndpointSource()
    assert callable(function.begin_request)
    assert callable(function.consume_message)
    assert callable(function.end_request)
