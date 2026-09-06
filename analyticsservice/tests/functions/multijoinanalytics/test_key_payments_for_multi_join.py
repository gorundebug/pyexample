"""User-owned tests for KeyPaymentsForMultiJoin."""

from analytics_service.internal.functions.multijoinanalytics.key_payments_for_multi_join import KeyPaymentsForMultiJoin


def test_key_payments_for_multi_join_contract_surface() -> None:
    function = KeyPaymentsForMultiJoin()
    assert callable(function.key_by)