"""User-owned tests for ObserveActivityResult."""

from automation_service.internal.functions.observe_activity_result import ObserveActivityResult


def test_observe_activity_result_contract_surface() -> None:
    function = ObserveActivityResult()
    assert callable(function.map)
