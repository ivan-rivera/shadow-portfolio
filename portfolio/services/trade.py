"""Trade service for executing auto-trading flows."""

import logging
from functools import lru_cache

from portfolio.config.settings import Settings, get_settings
from portfolio.research.aggregator import ResearchAggregator
from portfolio.services.sampler import BaseSampler, get_sampler

logger = logging.getLogger(__name__)


class TradeService:
    """Stateful service for running trade operations."""

    def __init__(self, settings: Settings, sampler: BaseSampler, research: ResearchAggregator) -> None:
        self._settings = settings
        self._sampler = sampler
        self._research = research

    def run(self) -> None:
        """Execute the trade flow by fetching and printing the latest MSFT price."""
        tickers = self._sampler.get(1)
        for ticker in tickers:
            research = self._research.fetch(ticker)
            logger.info("Research: %s", research)

    def resume(self) -> None:
        """Resume a trade after receiving human approval or rejection.

        Currently, this is a stub which merely logs hello world.
        """
        logger.info("Hello, world! Trade resume background job started.")


@lru_cache
def get_trade_service() -> TradeService:
    """Return the shared TradeService instance (stateful, singleton)."""
    return TradeService(
        settings=get_settings(),
        sampler=get_sampler(),
        research=ResearchAggregator(),
    )
