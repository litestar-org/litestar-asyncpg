from contextlib import asynccontextmanager
from functools import partial
from typing import Any, AsyncGenerator

import pytest
from asyncpg import Connection
from litestar import Litestar, get
from litestar.testing import create_test_client

from litestar_asyncpg import AsyncpgConfig, AsyncpgPlugin, PoolConfig

pytestmark = pytest.mark.anyio


async def test_lifespan(postgres_service: None, docker_ip: str) -> None:
    @get("/")
    async def health_check(provide_connection: Connection) -> float:
        """Check database available and returns random number."""
        r = await provide_connection.fetch("select random()")
        return r[0]["random"]  # type: ignore

    @asynccontextmanager
    async def lifespan(_app: Litestar) -> AsyncGenerator[None, Any]:
        print(1)  # noqa: T201
        yield
        print(2)  # noqa: T201

    asyncpg_config = AsyncpgConfig(pool_config=PoolConfig(dsn=f"postgresql://app:app@{docker_ip}:5432/app"))
    asyncpg = AsyncpgPlugin(config=asyncpg_config)
    with create_test_client(route_handlers=[health_check], plugins=[asyncpg], lifespan=[partial(lifespan)]) as client:
        response = client.get("/")
        assert response.status_code == 200