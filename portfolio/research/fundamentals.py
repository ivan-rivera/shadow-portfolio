"""Fundamentals retrieval for a given ticker via Finnhub."""

import finnhub

from portfolio.config.constants import FUNDAMENTALS_LOOKBACK_DAYS
from portfolio.config.settings import get_settings


class FundamentalsRetriever:
    """Fetches basic financial statements for a ticker."""

    def __init__(self, lookback_days: int = FUNDAMENTALS_LOOKBACK_DAYS):
        self._lookback_days = lookback_days
        self._client = finnhub.Client(api_key=get_settings().finnhub_api_key)

    def fetch(self, ticker: str) -> dict:
        return self._client.company_basic_financials(ticker, "all")
