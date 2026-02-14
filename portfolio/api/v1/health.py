"""Check the health of the API"""

from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
async def health() -> dict[str, str]:
    """Check the health of the API"""
    return {"status": "ok"}
