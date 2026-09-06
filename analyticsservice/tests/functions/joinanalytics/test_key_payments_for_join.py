"""User-owned tests for KeyPaymentsForJoin."""

from analytics_service.internal.functions.joinanalytics.key_payments_for_join import KeyPaymentsForJoin


def test_key_payments_for_join_contract_surface() -> None:
    function = KeyPaymentsForJoin()
    assert callable(function.key_by)