"""Main entry point for the API"""

from fastapi import FastAPI

from portfolio.api.routes import router
from portfolio.config.logging import configure_logging
from portfolio.config.settings import get_settings

settings = get_settings()
configure_logging(settings.app_log_level)

app = FastAPI()
app.include_router(router, prefix="/api")
