"""
Initiate auto-trading flow

This endpoint uses the trading service to trigger a trading run.
"""

from typing import Annotated

from fastapi import APIRouter, BackgroundTasks, Depends

from portfolio.schemas.trade import TradeAcknowledgement
from portfolio.services.trade import TradeService, get_trade_service

router = APIRouter()


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
