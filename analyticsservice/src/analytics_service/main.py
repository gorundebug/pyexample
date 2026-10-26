"""Generated process lifecycle entrypoint. DO NOT EDIT."""

import asyncio
import os
import signal
import traceback

from pyservicelib_gorundebug.runtime.config.config import ConfigSettings
from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.serviceapp import ServiceAppLoader

from .internal.app.service import Dependency, Service
from .internal.config import Config


async def run(ctx: Context) -> None:
    service = await ServiceAppLoader[Service, Config]().load(
        "Analytics Service",
        Dependency(),
        ConfigSettings(),
    )
    loop = asyncio.get_running_loop()
    installed_signals: list[signal.Signals] = []
    try:
        await service.start_service(ctx)
        stopped = asyncio.Event()
        for sig in (signal.SIGINT, signal.SIGTERM):
            loop.add_signal_handler(sig, stopped.set)
            installed_signals.append(sig)
        await stopped.wait()
    finally:
        for sig in installed_signals:
            loop.remove_signal_handler(sig)
        try:
            await service.stop_service(ctx)
        finally:
            await service.release(ctx)


async def _run_process() -> None:
    exit_code = 0
    try:
        await run(Context())
    except BaseException:
        exit_code = 1
        traceback.print_exc()
    finally:
        # stop_service owns the shutdown budget and resource drain. Like Go,
        # exit without waiting again for leftover tasks or non-daemon threads.
        os._exit(exit_code)


def main() -> None:
    asyncio.run(_run_process())


if __name__ == "__main__":
    main()