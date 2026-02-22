"""Technical indicator retrieval for a given ticker via Finnhub."""

import json
from collections.abc import Callable
from datetime import datetime, timedelta

import finnhub

from portfolio.config.constants import INDICATORS_LOOKBACK_DAYS
from portfolio.config.settings import get_settings
from portfolio.research import metrics as m
from portfolio.research.base import BaseResearch

_MetricFn = Callable[[finnhub.Client, str, datetime, datetime], dict]

_DEFAULT_METRICS: dict[str, _MetricFn] = {
    "candles": m.stock_candles,
    "insider_sentiment": m.insider_sentiment,
}


class IndicatorsResearch(BaseResearch[dict]):
    """Fetches indicator metrics for a ticker."""

    def __init__(
        self,
        lookback_days: int = INDICATORS_LOOKBACK_DAYS,
        metrics: dict[str, _MetricFn] | None = None,
    ):
        self._lookback_days = lookback_days
        self._metrics = metrics or _DEFAULT_METRICS
        self._client = finnhub.Client(api_key=get_settings().finnhub_api_key)

    def _fetch(self, ticker: str) -> dict:
        end = datetime.now()
        start = end - timedelta(days=self._lookback_days)
        return {name: fn(self._client, ticker, start, end) for name, fn in self._metrics.items()}

    def _compact(self, result: dict) -> str:
        return json.dumps(result)
