"""User-owned function implementation. The generator never overwrites this file."""

from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment
from pyservicelib_gorundebug.runtime.config.stream_types import CaseStreamConfig
from typing import Callable
from analytics_service.models.analytics_result import AnalyticsResult
from pyservicelib_gorundebug.operators.functions import When
from pyservicelib_gorundebug.runtime.common import Stream


class RouteAnalyticsResult:
    """Route high-value analytics results to the first branch and all others to the second branch."""

    def build_switch(
        self,
        stream: Stream,
        when_items: list[When],
    ) -> Callable[[AnalyticsResult], int]:
        del stream
        if len(when_items) != 2:
            raise ValueError(
                f"analytics result case requires exactly 2 branches, got {len(when_items)}"
            )
        return lambda value: 0 if value.total >= 50 else 1


async def make_route_analytics_result(
    ctx: Context,
    environment: ServiceEnvironment,
    config: CaseStreamConfig,
) -> RouteAnalyticsResult:
    """Construct RouteAnalyticsResult asynchronously while the graph is initialized."""
    del ctx, config, environment
    return RouteAnalyticsResult()
