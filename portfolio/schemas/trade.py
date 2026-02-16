"""Schemas for the trade API."""

from pydantic import BaseModel


class TradeAcknowledgement(BaseModel):
    """Acknowledgement that a trade background job was triggered."""

    message: str
    status: str = "accepted"
