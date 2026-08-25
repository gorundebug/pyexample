"""User-owned tests for ObserveFanoutActivityB."""

from automation_service.internal.functions.observe_fanout_activity_b import ObserveFanoutActivityB


def test_observe_fanout_activity_b_contract_surface() -> None:
    function = ObserveFanoutActivityB()
    assert callable(function.map)
