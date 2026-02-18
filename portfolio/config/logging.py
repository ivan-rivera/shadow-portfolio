"""Application logging configuration."""

from __future__ import annotations

import logging
from logging.config import dictConfig

DEFAULT_LOG_LEVEL = "INFO"
ALLOWED_LOG_LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}
LOG_FORMAT = "%(asctime)s %(levelname)s [%(name)s] [process=%(process)d thread=%(threadName)s] %(message)s"
LOG_DATE_FORMAT = "%Y-%m-%dT%H:%M:%S%z"


def configure_logging(log_level: str = DEFAULT_LOG_LEVEL) -> None:
    """Configure process-wide logging for application and server logs."""
    normalized_level = log_level.upper()
    if normalized_level not in ALLOWED_LOG_LEVELS:
        normalized_level = DEFAULT_LOG_LEVEL

    dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "standard": {
                    "format": LOG_FORMAT,
                    "datefmt": LOG_DATE_FORMAT,
                },
            },
            "handlers": {
                "default": {
                    "class": "logging.StreamHandler",
                    "formatter": "standard",
                    "stream": "ext://sys.stdout",
                },
            },
            "root": {
                "handlers": ["default"],
                "level": normalized_level,
            },
            "loggers": {
                "uvicorn.error": {
                    "level": normalized_level,
                },
                "uvicorn.access": {
                    "level": normalized_level,
                },
                "portfolio": {
                    "level": normalized_level,
                },
            },
        },
    )
    logging.getLogger(__name__).info("Logging configured with level %s", normalized_level)
