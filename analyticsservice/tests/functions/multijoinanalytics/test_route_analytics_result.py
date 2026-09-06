"""User-owned tests for RouteAnalyticsResult."""

from analytics_service.internal.functions.multijoinanalytics.route_analytics_result import RouteAnalyticsResult


def test_route_analytics_result_contract_surface() -> None:
    function = RouteAnalyticsResult()
    assert callable(function.build_switch)