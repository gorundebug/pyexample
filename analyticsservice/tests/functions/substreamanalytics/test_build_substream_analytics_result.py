"""User-owned tests for BuildSubstreamAnalyticsResult."""

from analytics_service.internal.functions.substreamanalytics.build_substream_analytics_result import BuildSubstreamAnalyticsResult


def test_build_substream_analytics_result_contract_surface() -> None:
    function = BuildSubstreamAnalyticsResult()
    assert callable(function.map)