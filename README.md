<!-- markdownlint-disable -->
<p align="center">
  <!-- github-banner-start -->
  <img src="https://raw.githubusercontent.com/litestar-org/branding/main/assets/Branding%20-%20SVG%20-%20Transparent/asyncPG%20-%20Banner%20-%20Inline%20-%20Light.svg#gh-light-mode-only" alt="Litestar Logo - Light" width="100%" height="auto" />
  <img src="https://raw.githubusercontent.com/litestar-org/branding/main/assets/Branding%20-%20SVG%20-%20Transparent/asyncPG%20-%20Banner%20-%20Inline%20-%20Dark.svg#gh-dark-mode-only" alt="Litestar Logo - Dark" width="100%" height="auto" />
  <!-- github-banner-end -->
</p>
<!-- markdownlint-restore -->

<div align="center">

<!-- prettier-ignore-start -->

| Project   |     | Status                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|-----------|:----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CI/CD     |     | [![Latest Release](https://github.com/litestar-org/litestar-asyncpg/actions/workflows/publish.yml/badge.svg)](https://github.com/litestar-org/litestar-asyncpg/actions/workflows/publish.yml) [![ci](https://github.com/litestar-org/litestar-asyncpg/actions/workflows/ci.yml/badge.svg)](https://github.com/litestar-org/litestar-asyncpg/actions/workflows/ci.yml) [![Documentation Building](https://github.com/litestar-org/litestar-asyncpg/actions/workflows/docs.yml/badge.svg?branch=main)](https://github.com/litestar-org/litestar-asyncpg/actions/workflows/docs.yml)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Quality   |     | [![Coverage](https://codecov.io/github/litestar-org/litestar-asyncpg/graph/badge.svg?token=vKez4Pycrc)](https://codecov.io/github/litestar-org/litestar-asyncpg) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=litestar-org_litestar-asyncpg&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=litestar-org_litestar-asyncpg) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=litestar-org_litestar-asyncpg&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=litestar-org_litestar-asyncpg) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=litestar-org_litestar-asyncpg&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=litestar-org_litestar-asyncpg) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=litestar-org_litestar-asyncpg&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=litestar-org_litestar-asyncpg)                                                                                                    |
| Package   |     | [![PyPI - Version](https://img.shields.io/pypi/v/litestar-asyncpg?labelColor=202235&color=edb641&logo=python&logoColor=edb641)](https://badge.fury.io/py/litestar) ![PyPI - Support Python Versions](https://img.shields.io/pypi/pyversions/litestar?labelColor=202235&color=edb641&logo=python&logoColor=edb641) ![Advanced Alchemy PyPI - Downloads](https://img.shields.io/pypi/dm/litestar-asyncpg?logo=python&label=package%20downloads&labelColor=202235&color=edb641&logoColor=edb641)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Community |     | [![Reddit](https://img.shields.io/reddit/subreddit-subscribers/litestarapi?label=r%2FLitestar&logo=reddit&labelColor=202235&color=edb641&logoColor=edb641)](https://reddit.com/r/litestarapi) [![Discord](https://img.shields.io/discord/919193495116337154?labelColor=202235&color=edb641&label=chat%20on%20discord&logo=discord&logoColor=edb641)](https://discord.gg/litestar) [![Matrix](https://img.shields.io/badge/chat%20on%20Matrix-bridged-202235?labelColor=202235&color=edb641&logo=matrix&logoColor=edb641)](https://matrix.to/#/#litestar:matrix.org) [![Medium](https://img.shields.io/badge/Medium-202235?labelColor=202235&color=edb641&logo=medium&logoColor=edb641)](https://blog.litestar.dev) [![Twitter](https://img.shields.io/twitter/follow/LitestarAPI?labelColor=202235&color=edb641&logo=twitter&logoColor=edb641&style=flat)](https://twitter.com/LitestarAPI) [![Blog](https://img.shields.io/badge/Blog-litestar.dev-202235?logo=blogger&labelColor=202235&color=edb641&logoColor=edb641)](https://blog.litestar.dev)                                                             |
| Meta      |     | [![Litestar Project](https://img.shields.io/badge/Litestar%20Org-%E2%AD%90%20Advanced%20Alchemy-202235.svg?logo=python&labelColor=202235&color=edb641&logoColor=edb641)](https://github.com/litestar-org/litestar-asyncpg) [![types - Mypy](https://img.shields.io/badge/types-Mypy-202235.svg?logo=python&labelColor=202235&color=edb641&logoColor=edb641)](https://github.com/python/mypy) [![License - MIT](https://img.shields.io/badge/license-MIT-202235.svg?logo=python&labelColor=202235&color=edb641&logoColor=edb641)](https://spdx.org/licenses/) [![Litestar Sponsors](https://img.shields.io/badge/Sponsor-%E2%9D%A4-%23edb641.svg?&logo=github&logoColor=edb641&labelColor=202235)](https://github.com/sponsors/litestar-org) [![linting - Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json&labelColor=202235)](https://github.com/astral-sh/ruff) [![code style - Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/format.json&labelColor=202235)](https://github.com/psf/black) |

</div>
# Litestar Asyncpg

A barebones AsyncPG plugin for Litestar.  This plugin is useful for when you plan to use no ORM or need to manage the postgres connection separately.

## Usage

### Installation

```shell
pip install litestar-asyncpg
```

### Example

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
