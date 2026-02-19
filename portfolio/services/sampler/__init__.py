"""Sampler implementations and construction helpers."""

from __future__ import annotations

from functools import lru_cache

from portfolio.config import constants
from portfolio.config.settings import get_settings
from portfolio.services.sampler.base import BaseSampler
from portfolio.services.sampler.simple import SimpleSampler

_REGISTRY: dict[str, type[BaseSampler]] = {
    "simple": SimpleSampler,
}


@lru_cache
def get_sampler() -> BaseSampler:
    """Return the shared sampler instance."""
    settings = get_settings()
    return _REGISTRY[constants.SAMPLER](settings)


__all__ = [
    "BaseSampler",
    "get_sampler",
]
