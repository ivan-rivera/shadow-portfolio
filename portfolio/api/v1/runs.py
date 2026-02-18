"""
Runs API endpoints.

**GET /runs: fetch all runs for a given period**
List all run IDs for a given period. Run IDs come with timestamp executed,
run status, trades conducted, total value purchased, total value spent.

**GET /runs/{run_id}: fetch a specific run by its ID**
Each run contains ticker, quantity, price, position, buy/sell, justification.

For now, both endpoints return hardcoded placeholder data.
# TODO: implement actual endpoint logic
"""

from datetime import UTC, datetime
from typing import Literal

from fastapi import APIRouter

from portfolio.schemas.runs import RunDetail, RunSummary, RunTrade

router = APIRouter()


def _placeholder_runs() -> list[RunSummary]:
    """Return hardcoded placeholder run summaries."""
    return [
        RunSummary(
            run_id="run-001",
            timestamp=datetime(2025, 2, 15, 10, 30, 0, tzinfo=UTC),
            run_status="completed",
            trades_conducted=2,
            total_value_purchased=1500.00,
            total_value_spent=1500.00,
        ),
        RunSummary(
            run_id="run-002",
            timestamp=datetime(2025, 2, 14, 14, 0, 0, tzinfo=UTC),
            run_status="completed",
            trades_conducted=1,
            total_value_purchased=500.00,
            total_value_spent=500.00,
        ),
    ]


def _placeholder_run_detail(run_id: str) -> RunDetail:
    """Return hardcoded placeholder run detail."""
    return RunDetail(
        run_id=run_id,
        trades=[
            RunTrade(
                ticker="AAPL",
                quantity=10.0,
                price=150.00,
                position="long",
                buy_sell="buy",
                justification="Momentum signal triggered buy.",
            ),
            RunTrade(
                ticker="GOOGL",
                quantity=5.0,
                price=140.00,
                position="long",
                buy_sell="sell",
                justification="Take profit on position.",
            ),
        ],
    )


@router.get(
    "/runs",
    response_model=list[RunSummary],
    tags=["runs"],
    summary="List runs for a period",
    description="List all run IDs for a given period with timestamp, status, and trade totals.",
    response_description="List of run summaries",
)
async def list_runs(
    period: Literal["hour", "day", "week", "month"] = "day",  # noqa: ARG001, pylint: disable=unused-argument
) -> list[RunSummary]:
    """Fetch all runs for a given period. Stub returns placeholder data."""
    return _placeholder_runs()


@router.get(
    "/runs/{run_id}",
    response_model=RunDetail,
    tags=["runs"],
    summary="Fetch run by ID",
    description="Fetch a specific run by its ID with full trade details.",
    response_description="Run detail with trades",
)
async def get_run(run_id: str) -> RunDetail:
    """Fetch a specific run by ID. Stub returns placeholder data."""
    return _placeholder_run_detail(run_id)
