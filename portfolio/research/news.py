"""News retrieval for a given ticker via Finnhub."""

import json
from datetime import date, timedelta

import finnhub

from portfolio.config.constants import NEWS_LOOKBACK_DAYS
from portfolio.config.settings import get_settings
from portfolio.research.base import BaseResearch


class NewsResearch(BaseResearch[list[dict]]):
    """Fetches recent news articles for a ticker."""

    def __init__(self, lookback_days: int = NEWS_LOOKBACK_DAYS):
        self._lookback_days = lookback_days
        self._client = finnhub.Client(api_key=get_settings().finnhub_api_key)

    def _fetch(self, ticker: str) -> list[dict]:
        """
        Fetches recent news articles for a ticker.
        """
        end = date.today()
        start = end - timedelta(days=self._lookback_days)
        return self._client.company_news(
            ticker,
            _from=start.isoformat(),
            to=end.isoformat(),
        )

    def _compact(self, result: list[dict]) -> str:
        return json.dumps(result)
