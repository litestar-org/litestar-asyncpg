from __future__ import annotations

import asyncio
from pathlib import Path
from typing import TYPE_CHECKING

import pytest
from asyncpg import create_pool as asyncpg_create_pool
from asyncpg.pool import Pool
from examples.basic import SampleController
from litestar import Litestar

from litestar_asyncpg.config import AsyncpgConfig
from litestar_asyncpg.plugin import AsyncpgPlugin

here = Path(__file__).parent
if TYPE_CHECKING:
    from collections import abc

pytestmark = pytest.mark.anyio

pytest_plugins = ["tests.docker_service_fixtures"]


@pytest.fixture
def anyio_backend() -> str:
    return "asyncio"


@pytest.fixture(scope="session")
def event_loop() -> abc.Iterator[asyncio.AbstractEventLoop]:
    """Scoped Event loop.

    Need the event loop scoped to the session so that we can use it to check
    containers are ready in session scoped containers fixture.
    """
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    try:
        yield loop
    finally:
        loop.close()


@pytest.fixture(name="connection_pool")
async def connection_pool(docker_ip: str, postgres_service: None) -> Pool:
    """App fixture.

    Returns:
        An application instance, configured via plugin.
    """
    return asyncpg_create_pool(dsn=f"postgresql://app:app@{docker_ip}:5423/app", min_size=1, max_size=1)


@pytest.fixture(name="plugin")
async def plugin(connection_pool: Pool) -> AsyncpgPlugin:
    """App fixture.

    Returns:
        An application instance, configured via plugin.
    """

    return AsyncpgPlugin(
        config=AsyncpgConfig(
            pool_instance=connection_pool,
        ),
    )


@pytest.fixture(name="app")
def fx_app(plugin: AsyncpgPlugin) -> Litestar:
    """App fixture.

    Returns:
        An application instance, configured via plugin.
    """
    return Litestar(plugins=[plugin], route_handlers=[SampleController])
