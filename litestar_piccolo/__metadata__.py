"""Metadata for the Project."""
from __future__ import annotations

import importlib.metadata

__all__ = ["__version__", "__project__"]

__version__ = importlib.metadata.version("litestar_piccolo")
"""Version of the project."""
__project__ = importlib.metadata.metadata("litestar_piccolo")["Name"]
"""Name of the project."""
