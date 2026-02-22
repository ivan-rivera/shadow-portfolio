"""Technical indicator retrieval for a given ticker via Twelve Data."""

import json
import time

from twelvedata import TDClient

from portfolio.config.constants import INDICATORS_LOOKBACK_DAYS, TWELVEDATA_REQUESTS_PER_MINUTE
from portfolio.config.settings import get_settings
from portfolio.research.base import BaseResearch
from portfolio.research.metrics import _DEFAULT_METRICS, _MetricFn


class IndicatorsResearch(BaseResearch[dict]):
    """Fetches indicator metrics for a ticker."""

    def __init__(
        self,
        lookback_days: int = INDICATORS_LOOKBACK_DAYS,
        metrics: dict[str, _MetricFn] | None = None,
    ):
        settings = get_settings()
        self._lookback_days = lookback_days
        self._metrics = metrics or _DEFAULT_METRICS
        self._client = TDClient(apikey=settings.twelvedata_api_key)
        self._requests_per_minute = TWELVEDATA_REQUESTS_PER_MINUTE

    def _fetch(self, ticker: str) -> dict:
        results: dict[str, dict] = {}
        for i, (name, fn) in enumerate(self._metrics.items()):
            if i > 0:
                time.sleep(60 / self._requests_per_minute)
            results[name] = fn(self._client, ticker, self._lookback_days)
        return results

    def _compact(self, result: dict) -> str:
        return json.dumps(result)
