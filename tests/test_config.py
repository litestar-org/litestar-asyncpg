

import pytest
from pytest_databases.docker.postgres import PostgresService

from litestar_asyncpg import AsyncpgConfig, PoolConfig

pytestmark = pytest.mark.anyio


async def test_get_connection(postgres_service: PostgresService) -> None:
    asyncpg_config = AsyncpgConfig(pool_config=PoolConfig(dsn=f"postgresql://{postgres_service.user}:{postgres_service.password}@{postgres_service.host}:{postgres_service.port}/{postgres_service.database}"))


    async with asyncpg_config.get_connection() as db_connection:
        r = await db_connection.fetch("select 1 as one")
        assert r[0]["one"] == 1
