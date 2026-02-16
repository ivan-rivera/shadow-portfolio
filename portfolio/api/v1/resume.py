"""
Resume a trade after receiving approval or a rejection

This endpoint is used to resume a trade after receiving human approval or rejection.
Uses the trading service to resume a trade job as a background task.
"""

from typing import Annotated

from fastapi import APIRouter, BackgroundTasks, Depends

from portfolio.schemas.trade import TradeAcknowledgement
from portfolio.services.trade import TradeService, get_trade_service

router = APIRouter()


@router.post(
    "/resume",
    response_model=TradeAcknowledgement,
    status_code=202,
    tags=["trade"],
    summary="Resume trade after approval/rejection",
    description=(
        "Triggers a background job to resume a trade after receiving human "
        "approval or rejection. Returns immediately with an acknowledgement. "
        "The actual resume processing runs asynchronously after the response is sent."
    ),
    response_description="Acknowledgement that the resume job was queued",
)
async def resume_trade(
    background_tasks: BackgroundTasks,
    trade_service: Annotated[TradeService, Depends(get_trade_service)],
) -> TradeAcknowledgement:
    """Resume a trade after approval or rejection as a background job."""
    background_tasks.add_task(trade_service.resume)
    return TradeAcknowledgement(
        message="Resume job triggered. Processing in background.",
        status="accepted",
    )
