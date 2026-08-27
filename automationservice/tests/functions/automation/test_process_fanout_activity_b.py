"""User-owned tests for ProcessFanoutActivityB."""

from automation_service.internal.functions.automation.process_fanout_activity_b import ProcessFanoutActivityB


def test_process_fanout_activity_b_contract_surface() -> None:
    function = ProcessFanoutActivityB()
    assert callable(function.map)
