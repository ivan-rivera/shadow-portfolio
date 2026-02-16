"""Check the health of the API"""

from fastapi import APIRouter

from portfolio.schemas.health import HealthResponse

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
async def health() -> HealthResponse:
    """Check the health of the API."""
    return HealthResponse()
