"""User-owned tests for KeyShipmentsForMultiJoin."""

from analytics_service.internal.functions.multijoinanalytics.key_shipments_for_multi_join import KeyShipmentsForMultiJoin


def test_key_shipments_for_multi_join_contract_surface() -> None:
    function = KeyShipmentsForMultiJoin()
    assert callable(function.key_by)