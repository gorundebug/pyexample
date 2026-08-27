"""User-owned tests for ProcessFanoutActivityA."""

from automation_service.internal.functions.automation.process_fanout_activity_a import ProcessFanoutActivityA


def test_process_fanout_activity_a_contract_surface() -> None:
    function = ProcessFanoutActivityA()
    assert callable(function.map)
