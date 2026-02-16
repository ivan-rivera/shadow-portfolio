"""Schemas for the health API."""

from importlib.metadata import version
from typing import Literal

from pydantic import BaseModel, Field


def _get_app_version() -> str:
    """Return the application version from package metadata."""
    try:
        return version("shadow-portfolio")
    except Exception:
        return "dev"


class HealthResponse(BaseModel):
    """Health check response with API status and version."""

    status: Literal["ok"] = "ok"
    version: str = Field(default_factory=_get_app_version)
