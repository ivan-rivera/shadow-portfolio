"""Trade service for executing auto-trading flows."""

from functools import lru_cache


class TradeService:
    """Stateful service for running trade operations."""

    def run(self) -> None:
        """Execute the trade flow. Stub implementation prints hello world."""
        print("Hello, world!")  # noqa: T201

    def resume(self) -> None:
        """Resume a trade after receiving human approval or rejection.

        Currently, this is a stub which merely prints hello world.
        """
        print("Hello, world!")  # noqa: T201


@lru_cache
def get_trade_service() -> TradeService:
    """Return the shared TradeService instance (stateful, singleton)."""
    return TradeService()
