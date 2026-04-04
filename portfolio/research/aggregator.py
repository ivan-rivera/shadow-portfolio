"""Aggregation of all research capabilities for a given ticker."""

from collections.abc import Iterable

from portfolio.research.base import BaseResearch
from portfolio.research.fundamentals import FundamentalsResearch
from portfolio.research.indicators import IndicatorsResearch
from portfolio.research.news import NewsResearch
from portfolio.research.profile import ProfileResearch


_DEFAULT_PROVIDER_CLASSES = (
    FundamentalsResearch,
    IndicatorsResearch,
    NewsResearch,
    ProfileResearch,
)


class ResearchAggregator:
    """Runs all available research providers and composes one response string."""

    def __init__(self, providers: Iterable[BaseResearch] | None = None):
        self._providers = list(providers or self._build_default_providers())

    def fetch(self, ticker: str) -> str:
        """Fetches and composes all research outputs for a ticker."""
        return "\n".join(f"{provider.__class__.__name__}: {provider.fetch(ticker)}" for provider in self._providers)

    def _build_default_providers(self) -> list[BaseResearch]:
        return [cls() for cls in _DEFAULT_PROVIDER_CLASSES]
