from __future__ import annotations

import asyncio
import os
from collections import abc
from typing import AsyncGenerator

import pytest
from piccolo.conf.apps import Finder
from piccolo.table import create_db_tables, drop_db_tables

os.environ["PICCOLO_CONF"] = "tests.piccolo_conf"

pytestmark = pytest.mark.anyio


@pytest.fixture(scope="session")
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


@pytest.fixture(autouse=True, scope="session")
async def scaffold_piccolo() -> AsyncGenerator:
    """Scaffolds Piccolo ORM and performs cleanup."""
    tables = Finder().get_table_classes()
    await drop_db_tables(*tables)
    await create_db_tables(*tables)
    yield
    await drop_db_tables(*tables)
