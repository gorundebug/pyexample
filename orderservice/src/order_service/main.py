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


async def run() -> None:
    service = await ServiceAppLoader[Service, Config]().load(
        "Order Service",
        Dependency(),
        ConfigSettings(),
    )
    await service.start_service(Context())

    stopped = asyncio.Event()
    loop = asyncio.get_running_loop()
    for sig in (signal.SIGINT, signal.SIGTERM):
        loop.add_signal_handler(sig, stopped.set)
    await stopped.wait()
    await service.stop_service(Context())


async def _run_process() -> None:
    exit_code = 0
    try:
        await run()
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