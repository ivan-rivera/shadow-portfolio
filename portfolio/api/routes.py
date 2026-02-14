"""Define the routes for the API"""

from fastapi import APIRouter

from portfolio.api.v1.routes import router as v1_router

router = APIRouter()

router.include_router(v1_router, prefix="/v1")
