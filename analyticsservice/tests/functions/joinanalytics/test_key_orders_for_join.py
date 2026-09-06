"""User-owned tests for KeyOrdersForJoin."""

from analytics_service.internal.functions.joinanalytics.key_orders_for_join import KeyOrdersForJoin


def test_key_orders_for_join_contract_surface() -> None:
    function = KeyOrdersForJoin()
    assert callable(function.key_by)