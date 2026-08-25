"""User-owned tests for ObserveFanoutActivityC."""

from automation_service.internal.functions.observe_fanout_activity_c import ObserveFanoutActivityC


def test_observe_fanout_activity_c_contract_surface() -> None:
    function = ObserveFanoutActivityC()
    assert callable(function.map)
