"""Company profile retrieval for a given ticker via Finnhub."""

import json

import finnhub

from portfolio.config.settings import get_settings
from portfolio.research.base import BaseResearch


class ProfileResearch(BaseResearch[dict]):
    """Fetches company profile information for a ticker."""

    def __init__(self) -> None:
        self._client = finnhub.Client(api_key=get_settings().finnhub_api_key)

    def _fetch(self, ticker: str) -> dict:
        """
        Fetches company profile information for a ticker.
        """
        return self._client.company_profile2(symbol=ticker)

    def _compact(self, result: dict) -> str:
        return json.dumps(result)
