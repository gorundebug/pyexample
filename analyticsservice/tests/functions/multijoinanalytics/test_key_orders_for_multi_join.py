"""User-owned tests for KeyOrdersForMultiJoin."""

from analytics_service.internal.functions.multijoinanalytics.key_orders_for_multi_join import KeyOrdersForMultiJoin


def test_key_orders_for_multi_join_contract_surface() -> None:
    function = KeyOrdersForMultiJoin()
    assert callable(function.key_by)