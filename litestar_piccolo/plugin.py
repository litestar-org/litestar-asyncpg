from __future__ import annotations

from typing import TYPE_CHECKING, Any, TypeVar

from litestar.plugins import InitPluginProtocol, SerializationPluginProtocol
from piccolo.table import Table

from litestar_piccolo.dto import PiccoloDTO

if TYPE_CHECKING:
    from litestar.config.app import AppConfig
    from litestar.typing import FieldDefinition

T = TypeVar("T", bound=Table)


class PiccoloSerializationPlugin(SerializationPluginProtocol):
    def __init__(self) -> None:
        self._type_dto_map: dict[type[Table], type[PiccoloDTO[Any]]] = {}

    def supports_type(self, field_definition: FieldDefinition) -> bool:
        return (
            field_definition.is_collection and field_definition.has_inner_subclass_of(Table)
        ) or field_definition.is_subclass_of(Table)

    def create_dto_for_type(self, field_definition: FieldDefinition) -> type[PiccoloDTO[Any]]:
        # assumes that the type is a container of Piccolo models or a single Piccolo model
        annotation = next(
            (inner_type.annotation for inner_type in field_definition.inner_types if inner_type.is_subclass_of(Table)),
            field_definition.annotation,
        )
        if annotation in self._type_dto_map:
            return self._type_dto_map[annotation]

        self._type_dto_map[annotation] = dto_type = PiccoloDTO[annotation]  # type:ignore[valid-type]

        return dto_type


class PiccoloPlugin(InitPluginProtocol):
    """A plugin that provides Piccolo integration."""

    def __init__(self) -> None:
        """Initialize ``PiccoloPlugin``."""

    def on_app_init(self, app_config: AppConfig) -> AppConfig:
        """Configure application for use with Piccolo.

        Args:
            app_config: The :class:`AppConfig <.config.app.AppConfig>` instance.
        """
        app_config.plugins.extend([PiccoloSerializationPlugin()])
        return app_config
