"""User-owned function implementation. The generator never overwrites this file."""

from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment

from pyservicelib_gorundebug.runtime.common import Collect, Stream


class ProcessScheduledWorkflow:
    """Return the visible result of one scheduled Workflow execution."""

    async def map(
        self,
        stream: Stream,
        value: str,
        out: Collect[str],
    ) -> None:
        del stream
        await out.out(f"workflow:processed:{value}")


async def make_process_scheduled_workflow(
    ctx: Context,
    environment: ServiceEnvironment,
) -> ProcessScheduledWorkflow:
    """Construct ProcessScheduledWorkflow for the configured service graph."""
    del ctx, environment
    return ProcessScheduledWorkflow()
