

import pytest

from litestar_asyncpg import AsyncpgConfig, PoolConfig

pytestmark = pytest.mark.anyio


async def test_get_connection(postgres_service: None, postgres_docker_ip: str,  postgres_user: str, postgres_password: str, postgres_database: str, postgres_port:int) -> None:
    asyncpg_config = AsyncpgConfig(pool_config=PoolConfig(dsn=f"postgresql://{postgres_user}:{postgres_password}@{postgres_docker_ip}:{postgres_port}/{postgres_database}"))


    async with asyncpg_config.get_connection() as db_connection:
        r = await db_connection.fetch("select 1 as one")
        assert r[0]["one"] == 1
