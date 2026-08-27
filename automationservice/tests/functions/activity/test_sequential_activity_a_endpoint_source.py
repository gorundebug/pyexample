"""User-owned tests for SequentialActivityAEndpointSource."""

from automation_service.internal.functions.activity.sequential_activity_a_endpoint_source import SequentialActivityAEndpointSource


def test_sequential_activity_a_endpoint_source_contract_surface() -> None:
    function = SequentialActivityAEndpointSource()
    assert callable(function.begin_request)
    assert callable(function.consume_message)
    assert callable(function.end_request)
