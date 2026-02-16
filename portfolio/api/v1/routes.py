"""Define the routes for the API"""

from fastapi import APIRouter

from portfolio.api.v1.health import router as health_router
from portfolio.api.v1.resume import router as resume_router
from portfolio.api.v1.runs import router as runs_router
from portfolio.api.v1.trade import router as trade_router

router = APIRouter()

router.include_router(health_router)
router.include_router(trade_router)
router.include_router(resume_router)
router.include_router(runs_router)
