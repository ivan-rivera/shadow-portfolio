"""Constants for the project.

This module is intentionally import-only: it should not import from other
project modules to avoid circular dependencies.
"""

SAMPLER = "simple"

NEWS_LOOKBACK_DAYS = 30
FUNDAMENTALS_LOOKBACK_DAYS = 365
INDICATORS_LOOKBACK_DAYS = 30

INDICATORS_INTERVAL = "1day"

RSI_TIME_PERIOD = 14
ATR_TIME_PERIOD = 14

BBANDS_TIME_PERIOD = 20
BBANDS_SD = 2

ADX_TIME_PERIOD = 14

SMA_50_TIME_PERIOD = 50
SMA_200_TIME_PERIOD = 200

TWELVEDATA_REQUESTS_PER_MINUTE = 8
FINNHUB_REQUESTS_PER_MINUTE = 30
