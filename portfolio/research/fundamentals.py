"""Fundamentals retrieval for a given ticker via Finnhub."""

import json
from datetime import UTC, datetime, timedelta

import finnhub

from portfolio.config.constants import FUNDAMENTALS_LOOKBACK_DAYS
from portfolio.config.settings import get_settings
from portfolio.research.base import BaseResearch

_METRIC_KEYS = (
    "52WeekHigh",
    "52WeekLow",
    "52WeekPriceReturnDaily",
    "beta",
    "peNormalizedAnnual",
    "roeTTM",
)

_QUARTERLY_SERIES_KEYS = (
    "netMargin",
    "salesPerShare",
)


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
        metric = {k: result["metric"][k] for k in _METRIC_KEYS if k in result.get("metric", {})}

        cutoff = datetime.now(tz=UTC).date() - timedelta(days=self._lookback_days)
        quarterly = result.get("series", {}).get("quarterly", {})
        series = {
            k: [e for e in quarterly.get(k, []) if e["period"] >= cutoff.isoformat()] for k in _QUARTERLY_SERIES_KEYS
        }

        return json.dumps({"metric": metric, "series": {"quarterly": series}})
