"""Simple hard-coded ticker sampler."""

from portfolio.config.settings import Settings
from portfolio.services.sampler.base import BaseSampler

_TICKERS = [
    "AAPL",
    "MSFT",
    "GOOGL",
    "AMZN",
    "NVDA",
    "META",
    "TSLA",
    "BRK.B",
    "JPM",
    "V",
]


class SimpleSampler(BaseSampler):
    """Returns a fixed hard-coded list of tickers.

    Assumes n will never exceed the size of the hard-coded set.
    """

    def __init__(self, settings: Settings, tickers: list[str] = _TICKERS) -> None:
        super().__init__(settings)
        self._tickers = tickers

    def get(self, n: int) -> list[str]:
        return self._tickers[:n]
