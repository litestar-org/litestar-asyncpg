from __future__ import annotations

from collections.abc import AsyncGenerator
from pathlib import Path

import pytest
from asyncpg import create_pool as asyncpg_create_pool
from asyncpg.pool import Pool
from examples.basic import SampleController
from litestar import Litestar

from litestar_asyncpg.config import AsyncpgConfig
from litestar_asyncpg.plugin import AsyncpgPlugin

here = Path(__file__).parent


pytestmark = pytest.mark.anyio
pytest_plugins = [
    "pytest_databases.docker",
    "pytest_databases.docker.postgres",
]


@pytest.fixture(scope="session")
def anyio_backend() -> str:
    return "asyncio"



@pytest.fixture(name="connection_pool", scope="session")
async def connection_pool(postgres_docker_ip: str, postgres_user: str, postgres_password: str, postgres_database: str, postgres_port:int, postgres_service: None) -> AsyncGenerator[Pool, None]:
    """App fixture.

    Returns:
        An application instance, configured via plugin.
    """
    yield asyncpg_create_pool(dsn=f"postgresql://{postgres_user}:{postgres_password}@{postgres_docker_ip}:{postgres_port}/{postgres_database}", min_size=1, max_size=1)


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
