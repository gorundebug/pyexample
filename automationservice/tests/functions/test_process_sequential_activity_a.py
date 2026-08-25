"""User-owned tests for ProcessSequentialActivityA."""

from automation_service.internal.functions.process_sequential_activity_a import (
    ProcessSequentialActivityA,
)


def test_process_sequential_activity_a_contract_surface() -> None:
    function = ProcessSequentialActivityA()
    assert callable(function.map)
