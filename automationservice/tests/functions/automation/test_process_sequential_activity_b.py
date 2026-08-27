"""User-owned tests for ProcessSequentialActivityB."""

from automation_service.internal.functions.automation.process_sequential_activity_b import (
    ProcessSequentialActivityB,
)


def test_process_sequential_activity_b_contract_surface() -> None:
    function = ProcessSequentialActivityB()
    assert callable(function.map)
