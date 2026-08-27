"""User-owned tests for SoftDeadline."""

from order_service.internal.functions.order.soft_deadline import SoftDeadline


def test_soft_deadline_contract_surface() -> None:
    function = SoftDeadline()
    assert callable(function.duration)
    assert callable(function.delay_error)