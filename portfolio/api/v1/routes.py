"""Define the routes for the API"""

from fastapi import APIRouter

from portfolio.api.v1.health import router as health_router

router = APIRouter()

router.include_router(health_router)
