"""User-owned service extensions. The generator never overwrites this file."""

import os

from pyservicelib_gorundebug.api.models.environment import Environment
from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment.environment import (
    ServiceDependency,
    ServiceEnvironment,
)
from pyservicelib_gorundebug.runtime.environment.log.log import LogsEngine
from pyservicelib_gorundebug.runtime.environment.metrics.metrics import MetricsEngine, NoopMetricsEngine
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
        # self.makers.activity_pause = custom_activity_pause_maker
        # self.makers.local_schedule = custom_local_schedule_maker
        # self.makers.observe_activity_result = custom_observe_activity_result_maker
        # self.makers.observe_workflow_result = custom_observe_workflow_result_maker
        # self.makers.process_activity_job = custom_process_activity_job_maker
        # self.makers.process_scheduled_activity = custom_process_scheduled_activity_maker
        # self.makers.process_scheduled_workflow = custom_process_scheduled_workflow_maker
        # self.makers.process_workflow_job = custom_process_workflow_job_maker
        # self.makers.scheduled_activity_pause = custom_scheduled_activity_pause_maker
        # self.makers.scheduled_workflow_pause = custom_scheduled_workflow_pause_maker
        # self.makers.temporal_activity_schedule = custom_temporal_activity_schedule_maker
        # self.makers.temporal_workflow_schedule = custom_temporal_workflow_schedule_maker
        # self.makers.workflow_pause = custom_workflow_pause_maker

    async def custom_functions_init(self, ctx: Context) -> None:
        """Configure constructed functions here before the graph is wired."""
        del ctx
        # Configure self.functions.activity_pause here when needed.
        # Configure self.functions.local_schedule here when needed.
        # Configure self.functions.observe_activity_result here when needed.
        # Configure self.functions.observe_workflow_result here when needed.
        # Configure self.functions.process_activity_job here when needed.
        # Configure self.functions.process_scheduled_activity here when needed.
        # Configure self.functions.process_scheduled_workflow here when needed.
        # Configure self.functions.process_workflow_job here when needed.
        # Configure self.functions.scheduled_activity_pause here when needed.
        # Configure self.functions.scheduled_workflow_pause here when needed.
        # Configure self.functions.temporal_activity_schedule here when needed.
        # Configure self.functions.temporal_workflow_schedule here when needed.
        # Configure self.functions.workflow_pause here when needed.

    async def on_start(self, ctx: Context) -> None:
        del ctx

    async def on_stop(self, ctx: Context) -> None:
        del ctx


def _uses_otlp(env: ServiceEnvironment) -> bool:
    return env.service_config.environment in {
        Environment.Staging,
        Environment.Production,
    }
