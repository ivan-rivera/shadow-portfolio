"""Base research abstractions."""

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class BaseResearch(ABC, Generic[T]):
    """Base class for all research data providers."""

    def fetch(self, ticker: str) -> str:
        """Fetches research data and optionally compacts the result."""
        result = self._fetch(ticker)
        return self._compact(result)

    @abstractmethod
    def _fetch(self, ticker: str) -> T:
        """Fetches research data for a ticker."""

    @abstractmethod
    def _compact(self, result: T) -> str:
        """Compacts fetched data into a string."""
