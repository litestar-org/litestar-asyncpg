from typing import TYPE_CHECKING

from asyncpg.pgproto import pgproto
from litestar.di import Provide
from litestar.plugins import InitPluginProtocol

if TYPE_CHECKING:
    from litestar.config.app import AppConfig

    from litestar_asyncpg.config import AsyncpgConfig


class SlotsBase:
    __slots__ = ("_config",)


class AsyncpgPlugin(InitPluginProtocol, SlotsBase):
    """Asyncpg plugin."""

    __slots__ = ()

    def __init__(self, config: "AsyncpgConfig") -> None:
        """Initialize ``AsyncpgPlugin``.

        Args:
            config: configure and start Asyncpg.
        """
        self._config = config

    @property
    def config(self) -> "AsyncpgConfig":
        """Return the plugin config.

        Returns:
            AsyncpgConfig.
        """
        return self._config

    def on_app_init(self, app_config: "AppConfig") -> "AppConfig":
        """Configure application for use with Asyncpg.

        Args:
            app_config: The :class:`AppConfig <.config.app.AppConfig>` instance.
        """

        app_config.dependencies.update(
            {
                self._config.pool_dependency_key: Provide(self._config.provide_pool, sync_to_thread=False),
                self._config.connection_dependency_key: Provide(self._config.provide_connection),
            },
        )
        app_config.type_encoders = {pgproto.UUID: str, **(app_config.type_encoders or {})}
        app_config.before_send.append(self._config.before_send_handler)
        app_config.lifespan.append(self._config.lifespan)
        app_config.signature_namespace.update(self._config.signature_namespace)

        return app_config
