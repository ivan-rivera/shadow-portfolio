"""Abstract base class for ticker sampling strategies."""

from abc import ABC, abstractmethod

from portfolio.config.settings import Settings


class BaseSampler(ABC):
    """Returns a list of ticker symbols for trade consideration.

    Subclasses implement different sampling strategies (hard-coded lists,
    screener APIs, LLM-based selection, etc.).
    """

    def __init__(self, settings: Settings) -> None:
        self._settings = settings

    @abstractmethod
    def get(self, n: int) -> list[str]:
        """Return up to n ticker symbols for consideration.

        Args:
            n: Maximum number of tickers to return.

        Returns:
            A list of ticker symbol strings, at most n items long.
        """
