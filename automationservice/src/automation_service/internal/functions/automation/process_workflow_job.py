"""User-owned function implementation. The generator never overwrites this file."""

from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment
from pyservicelib_gorundebug.runtime.config.stream_types import MapStreamConfig
from pyservicelib_gorundebug.runtime.common import Collect, Stream
from pyservicelib_gorundebug.runtime import temporal_continue_as_new


class ProcessWorkflowJob:
    """Continue the Workflow as new once, then return its final result."""

    async def map(
        self,
        stream: Stream,
        value: str,
        out: Collect[str],
    ) -> None:
        del stream
        continued_prefix = "continued:"
        if continued_prefix not in value:
            temporal_continue_as_new(f"{continued_prefix}{value}")
        await out.out(f"workflow:processed:{value.replace(continued_prefix, '', 1)}")


async def make_process_workflow_job(
    ctx: Context,
    environment: ServiceEnvironment,
    config: MapStreamConfig,
) -> ProcessWorkflowJob:
    """Construct ProcessWorkflowJob for the configured service graph."""
    del ctx, config, environment
    return ProcessWorkflowJob()
