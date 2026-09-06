"""User-owned tests for JoinOrderPaymentAnalytics."""

from analytics_service.internal.functions.joinanalytics.join_order_payment_analytics import JoinOrderPaymentAnalytics


def test_join_order_payment_analytics_contract_surface() -> None:
    function = JoinOrderPaymentAnalytics()
    assert callable(function.join)