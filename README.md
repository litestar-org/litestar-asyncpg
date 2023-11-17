# Litestar asyncpg

## Installation

```shell
pip install litestar-asyncpg
```

## Usage

Here is a basic application that demonstrates how to use the plugin.

```python
from __future__ import annotations

from typing import TYPE_CHECKING

from litestar import Controller, Litestar, get
from litestar_asyncpg import AsyncpgConfig, AsyncpgPlugin, PoolConfig

if TYPE_CHECKING:
    from asyncpg import Connection


class SampleController(Controller):
    @get(path="/sample")
    async def sample_route(self, db_connection: Connection) -> dict[str, str]:
        """Check database available and returns app config info."""
        result = await db_connection.fetch("select 1")
        return {"select_1": str(result)}


asyncpg = AsyncpgPlugin(config=AsyncpgConfig(pool_config=PoolConfig(dsn="postgresql://app:app@localhost:5432/app")))
app = Litestar(plugins=[asyncpg], route_handlers=[SampleController])

```
