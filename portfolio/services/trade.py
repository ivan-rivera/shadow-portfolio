"""Trade service for executing auto-trading flows."""

import logging
from functools import lru_cache

from alpaca.data.historical.stock import StockHistoricalDataClient
from alpaca.data.requests import StockLatestTradeRequest

from portfolio.config.settings import Settings, get_settings

logger = logging.getLogger(__name__)


class TradeService:
    """Stateful service for running trade operations."""

    def __init__(self, settings: Settings) -> None:
        self._settings = settings

    def run(self) -> None:
        """Execute the trade flow by fetching and printing the latest MSFT price."""
        # TODO: clean this up! This is just a test to see if we can call the API
        client = StockHistoricalDataClient(
            api_key=self._settings.alpaca_api_key,
            secret_key=self._settings.alpaca_secret_key,
        )
        request = StockLatestTradeRequest(symbol_or_symbols="MSFT")
        latest_trades = client.get_stock_latest_trade(request)
        msft_trade = latest_trades["MSFT"]

        logger.info("MSFT latest trade price: %s", msft_trade.price)

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
