"""User-owned tests for DurablePause."""

from automation_service.internal.functions.durable_pause import DurablePause


def test_durable_pause_contract_surface() -> None:
    function = DurablePause()
    assert callable(function.duration)
    assert callable(function.delay_error)