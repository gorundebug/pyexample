"""User-owned tests for SequentialActivityBEndpointSource."""

from automation_service.internal.functions.activity.sequential_activity_b_endpoint_source import SequentialActivityBEndpointSource


def test_sequential_activity_b_endpoint_source_contract_surface() -> None:
    function = SequentialActivityBEndpointSource()
    assert callable(function.begin_request)
    assert callable(function.consume_message)
    assert callable(function.end_request)
