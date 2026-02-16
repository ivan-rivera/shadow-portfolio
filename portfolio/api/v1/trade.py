"""
Initiate auto-trading flow

Currently this endpoint is a stub. It returns an acknowledgement of the request
and triggers a background job to trigger the trade service. For now the background
job merely prints a message to the console.
"""

from functools import lru_cache
from typing import Annotated

from fastapi import APIRouter, BackgroundTasks, Depends

from portfolio.schemas.trade import TradeAcknowledgement
from portfolio.services.trade import TradeService

router = APIRouter()


@lru_cache
def get_trade_service() -> TradeService:
    """Return the shared TradeService instance (stateful, singleton)."""
    return TradeService()


@router.post(
    "/trade",
    response_model=TradeAcknowledgement,
    status_code=202,
    tags=["trade"],
    summary="Initiate auto-trading",
    description=(
        "Triggers a background job to run the auto-trading flow. "
        "Returns immediately with an acknowledgement. The actual trade execution "
        "runs asynchronously after the response is sent."
    ),
    response_description="Acknowledgement that the trade job was queued",
)
async def initiate_trade(
    background_tasks: BackgroundTasks,
    trade_service: Annotated[TradeService, Depends(get_trade_service)],
) -> TradeAcknowledgement:
    """Initiate the auto-trading flow as a background job."""
    background_tasks.add_task(trade_service.run)
    return TradeAcknowledgement(
        message="Trade job triggered. Processing in background.",
        status="accepted",
    )
