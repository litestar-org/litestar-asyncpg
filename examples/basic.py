from __future__ import annotations

from typing import TYPE_CHECKING

import msgspec
from litestar import Controller, Litestar, get
from litestar.exceptions import InternalServerException

from litestar_asyncpg import AsyncpgConfig, AsyncpgPlugin, PoolConfig

if TYPE_CHECKING:
    from asyncpg import Connection


class PostgresHealthCheck(msgspec.Struct):
    """A new type describing a User"""

    version: str
    uptime: float


class SampleController(Controller):
    @get(path="/sample")
    async def sample_route(self, db_connection: Connection) -> PostgresHealthCheck:
        """Check database available and returns app config info."""
        result = await db_connection.fetchrow(
            "select version() as version, extract(epoch from current_timestamp - pg_postmaster_start_time()) as uptime",
        )
        if result:
            return PostgresHealthCheck(version=result["version"], uptime=result["uptime"])
        raise InternalServerException


asyncpg = AsyncpgPlugin(config=AsyncpgConfig(pool_config=PoolConfig(dsn="postgresql://app:app@localhost:5423/app")))
app = Litestar(plugins=[asyncpg], route_handlers=[SampleController])
