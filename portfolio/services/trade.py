"""Trade service for executing auto-trading flows."""

import logging
from functools import lru_cache

from portfolio.config.settings import Settings, get_settings

logger = logging.getLogger(__name__)


class TradeService:
    """Stateful service for running trade operations."""

    def __init__(self, settings: Settings) -> None:
        self._settings = settings

    def run(self) -> None:
        """Execute the trade flow. Stub implementation logs hello world."""
        logger.info("Hello, world! Trade background job started.")

    def resume(self) -> None:
        """Resume a trade after receiving human approval or rejection.

        Currently, this is a stub which merely logs hello world.
        """
        logger.info("Hello, world! Trade resume background job started.")


@lru_cache
def get_trade_service() -> TradeService:
    """Return the shared TradeService instance (stateful, singleton)."""
    settings = get_settings()
    return TradeService(settings)
