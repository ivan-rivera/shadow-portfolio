"""Company profile retrieval for a given ticker via Finnhub."""

import finnhub

from portfolio.config.settings import get_settings


class ProfileRetriever:
    """Fetches company profile information for a ticker."""

    def __init__(self, lookback_days: int = 0):
        self._client = finnhub.Client(api_key=get_settings().finnhub_api_key)

    def fetch(self, ticker: str) -> dict:
        return self._client.company_profile2(symbol=ticker)
