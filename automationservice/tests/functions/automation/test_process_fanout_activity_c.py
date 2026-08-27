"""User-owned tests for ProcessFanoutActivityC."""

from automation_service.internal.functions.automation.process_fanout_activity_c import ProcessFanoutActivityC


def test_process_fanout_activity_c_contract_surface() -> None:
    function = ProcessFanoutActivityC()
    assert callable(function.map)
