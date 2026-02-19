"""Technical indicator retrieval for a given ticker via Finnhub."""

from datetime import datetime, timedelta

import finnhub

from portfolio.config.constants import INDICATORS_LOOKBACK_DAYS
from portfolio.config.settings import get_settings


class IndicatorsRetriever:
    """Fetches daily OHLCV candlestick data for a ticker."""

    def __init__(self, lookback_days: int = INDICATORS_LOOKBACK_DAYS):
        self._lookback_days = lookback_days
        self._client = finnhub.Client(api_key=get_settings().finnhub_api_key)

    def fetch(self, ticker: str) -> dict:
        end = datetime.now()
        start = end - timedelta(days=self._lookback_days)
        return self._client.stock_candles(
            ticker,
            "D",
            int(start.timestamp()),
            int(end.timestamp()),
        )
