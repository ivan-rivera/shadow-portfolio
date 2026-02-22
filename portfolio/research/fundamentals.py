"""Fundamentals retrieval for a given ticker via Finnhub."""

import json

import finnhub

from portfolio.config.constants import FUNDAMENTALS_LOOKBACK_DAYS
from portfolio.config.settings import get_settings
from portfolio.research.base import BaseResearch


class FundamentalsResearch(BaseResearch[dict]):
    """Fetches basic financial statements for a ticker."""

    def __init__(self, lookback_days: int = FUNDAMENTALS_LOOKBACK_DAYS):
        self._lookback_days = lookback_days
        self._client = finnhub.Client(api_key=get_settings().finnhub_api_key)

    def _fetch(self, ticker: str) -> dict:
        """
        Fetches basic financial statements for a ticker.
        """
        return self._client.company_basic_financials(ticker, "all")

    def _compact(self, result: dict) -> str:
        return json.dumps(result)
