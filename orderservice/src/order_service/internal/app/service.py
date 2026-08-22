"""User-owned service extensions. The generator never overwrites this file."""

import os

from pyservicelib_gorundebug.api.models.environment import Environment
from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment.environment import (
    ServiceDependency,
    ServiceEnvironment,
)
from pyservicelib_gorundebug.runtime.environment.log.log import LogsEngine
from pyservicelib_gorundebug.runtime.environment.metrics.metrics import (
    MetricsEngine,
    NoopMetricsEngine,
)
from pyservicelib_gorundebug.runtime.environment.tracing.tracing import TracingEngine
from pyservicelib_gorundebug.runtime.telemetry.telemetry import (
    create_otlp_logs_engine,
    create_otlp_metrics_engine,
    create_otlp_tracing_engine,
    create_pretty_tracing_engine,
    create_prometheus_metrics_engine,
)

from .service_generated import GeneratedService


class Dependency(ServiceDependency):
    async def get_logs_engine(
        self,
        env: ServiceEnvironment,
    ) -> LogsEngine | None:
        if _uses_otlp(env):
            return create_otlp_logs_engine(env.service_config.name)
        return None

    async def get_metrics_engine(
        self,
        env: ServiceEnvironment,
    ) -> MetricsEngine | None:
        if os.getenv("SERVICELIB_NOOP_METRICS"):
            return NoopMetricsEngine()
        if _uses_otlp(env):
            return create_otlp_metrics_engine(env.service_config.name)
        return create_prometheus_metrics_engine(env.service_config.name)

    async def get_tracing_engine(
        self,
        env: ServiceEnvironment,
    ) -> TracingEngine | None:
        if _uses_otlp(env):
            return create_otlp_tracing_engine(env.service_config.name)
        return create_pretty_tracing_engine(
            env.service_config.name,
            context_sampler=True,
        )


class Service(GeneratedService):
    async def custom_makers_init(self, ctx: Context) -> None:
        """Replace generated makers here before any function is constructed."""
        del ctx
        # self.makers.map_order_item_result_to_order_state = custom_map_order_item_result_to_order_state_maker
        # self.makers.map_to_order_processed = custom_map_to_order_processed_maker
        # self.makers.map_to_order_state = custom_map_to_order_state_maker
        # self.makers.order_processed_endpoint = custom_order_processed_endpoint_maker
        # self.makers.process_order = custom_process_order_maker
        # self.makers.process_order_item = custom_process_order_item_maker
        # self.makers.process_order_items = custom_process_order_items_maker
        # self.makers.soft_deadline = custom_soft_deadline_maker

    async def custom_functions_init(self, ctx: Context) -> None:
        """Configure constructed functions here before the graph is wired."""
        del ctx
        # Configure self.functions.map_order_item_result_to_order_state here when needed.
        # Configure self.functions.map_to_order_processed here when needed.
        # Configure self.functions.map_to_order_state here when needed.
        # Configure self.functions.order_processed_endpoint here when needed.
        # Configure self.functions.process_order here when needed.
        # Configure self.functions.process_order_item here when needed.
        # Configure self.functions.process_order_items here when needed.
        # Configure self.functions.soft_deadline here when needed.

    async def on_start(self, ctx: Context) -> None:
        del ctx

    async def on_stop(self, ctx: Context) -> None:
        del ctx


def _uses_otlp(env: ServiceEnvironment) -> bool:
    return env.service_config.environment in {
        Environment.Staging,
        Environment.Production,
    }
