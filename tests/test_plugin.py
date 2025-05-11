from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from functools import partial
from typing import Any

import pytest
from asyncpg import Connection
from litestar import Litestar, get
from litestar.testing import create_test_client
from pytest_databases.docker.postgres import PostgresService

from litestar_asyncpg import AsyncpgConfig, AsyncpgPlugin, PoolConfig

pytestmark = pytest.mark.anyio


async def test_lifespan(postgres_service: PostgresService) -> None:
    @get("/")
    async def health_check(db_connection: Connection) -> float:
        """Check database available and returns random number."""
        r = await db_connection.fetch("select random()")
        return r[0]["random"]  # type: ignore[no-any-return]

    @asynccontextmanager
    async def lifespan(_app: Litestar) -> AsyncGenerator[None, Any]:
        print(1)  # noqa: T201
        yield
        print(2)  # noqa: T201

    asyncpg_config = AsyncpgConfig(pool_config=PoolConfig(dsn=f"postgresql://{postgres_service.user}:{postgres_service.password}@{postgres_service.host}:{postgres_service.port}/{postgres_service.database}"))
    asyncpg = AsyncpgPlugin(config=asyncpg_config)
    with create_test_client(route_handlers=[health_check], plugins=[asyncpg], lifespan=[partial(lifespan)]) as client:
        response = client.get("/")
        assert response.status_code == 200
