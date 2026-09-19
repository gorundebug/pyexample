"""User-owned tests for InvokeAnalyticsSubstream."""

from analytics_service.internal.functions.substreamanalytics.invoke_analytics_substream import InvokeAnalyticsSubstream


class _SubStream:
    async def consume(self, value, collector) -> None:
        del value, collector


def test_invoke_analytics_substream_contract_surface() -> None:
    function = InvokeAnalyticsSubstream(_SubStream())
    assert callable(function.map)
