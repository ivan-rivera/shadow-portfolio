"""Main entry point for the API"""

from fastapi import FastAPI

from portfolio.api.routes import router

app = FastAPI()

app.include_router(router, prefix="/api")
