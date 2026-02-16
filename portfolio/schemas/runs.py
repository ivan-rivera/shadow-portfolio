"""Schemas for the runs API."""

from datetime import datetime
from typing import Literal

from pydantic import BaseModel


class RunSummary(BaseModel):
    """Summary of a trading run for list views."""

    run_id: str
    timestamp: datetime
    run_status: str
    trades_conducted: int
    total_value_purchased: float
    total_value_spent: float


class RunTrade(BaseModel):
    """Individual trade within a run."""

    ticker: str
    quantity: float
    price: float
    position: str
    buy_sell: Literal["buy", "sell"]
    justification: str


class RunDetail(BaseModel):
    """Full detail of a trading run with its trades."""

    run_id: str
    trades: list[RunTrade]
