"""Concurrent workflow maker initialization keeps result and error ownership."""

import asyncio
from collections.abc import Awaitable, Callable
from dataclasses import fields
from typing import Any

import pytest

from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment

from automation_service.internal.app.service import Service
from automation_service.internal.app.workflow_graph_generated import (
    default_makers,
    init_functions,
)
from automation_service.internal.config import Config


@pytest.mark.asyncio
async def test_workflow_makers_start_concurrently_and_preserve_results() -> None:
    makers = default_makers()
    names = {field.name for field in fields(makers)}
    started: set[str] = set()
    contexts: list[Context] = []
    results: dict[str, Any] = {}
    ready = asyncio.Event()
    parent = Context()
    environment = Service()
    config = Config.from_dict({})
    assert config is not None

    def wrap(
        name: str,
        original: Callable[[Context, ServiceEnvironment], Awaitable[Any]],
    ) -> Callable[[Context, ServiceEnvironment], Awaitable[Any]]:
        async def make(ctx: Context, env: ServiceEnvironment) -> Any:
            assert env is environment
            contexts.append(ctx)
            started.add(name)
            if started == names:
                ready.set()
            await ready.wait()
            result = await original(ctx, env)
            results[name] = result
            return result

        return make

    for name in names:
        setattr(makers, name, wrap(name, getattr(makers, name)))

    functions = await asyncio.wait_for(
        init_functions(parent, config, environment, makers), timeout=5
    )
    assert started == names
    assert set(results) == names
    for name in names:
        assert getattr(functions, name) is results[name]
    assert all(ctx.cancelled for ctx in contexts)
    assert not parent.cancelled


@pytest.mark.asyncio
async def test_workflow_maker_failure_cancels_child_and_joins_siblings() -> None:
    makers = default_makers()
    names = {field.name for field in fields(makers)}
    failed_name = sorted(names)[0]
    failure = RuntimeError("maker failed")
    ready = asyncio.Event()
    started: set[str] = set()
    finished: set[str] = set()
    parent = Context()
    config = Config.from_dict({})
    assert config is not None

    def wrap(name: str) -> Callable[[Context, ServiceEnvironment], Awaitable[Any]]:
        async def make(ctx: Context, env: ServiceEnvironment) -> Any:
            started.add(name)
            if started == names:
                ready.set()
            await ready.wait()
            if name == failed_name:
                raise failure
            while not ctx.cancelled:
                await asyncio.sleep(0)
            await asyncio.sleep(0)
            finished.add(name)
            return None

        return make

    for name in names:
        setattr(makers, name, wrap(name))

    with pytest.raises(RuntimeError) as raised:
        await asyncio.wait_for(
            init_functions(parent, config, Service(), makers), timeout=5
        )
    assert raised.value is failure
    assert started == names
    assert finished == names - {failed_name}
    assert not parent.cancelled
