"""Metadata for the Project."""

from importlib.metadata import PackageNotFoundError, metadata, version

__all__ = ("__project__", "__version__")

try:
    __version__ = version("litestar_asyncpg")
    """Version of the project."""
    __project__ = metadata("litestar_asyncpg")["Name"]
    """Name of the project."""
except PackageNotFoundError:  # pragma: no cover
    __version__ = "0.0.1"
    __project__ = "Litestar AsyncPG"
finally:
    del version, PackageNotFoundError, metadata
