"""Indicator metric fetcher functions for use with IndicatorsResearch."""

from datetime import datetime

import finnhub


def stock_candles(
    client: finnhub.Client, ticker: str, start: datetime, end: datetime
) -> dict:
    return client.stock_candles(ticker, "D", int(start.timestamp()), int(end.timestamp()))


def insider_sentiment(
    client: finnhub.Client, ticker: str, start: datetime, end: datetime
) -> dict:
    return client.stock_insider_sentiment(
        ticker, _from=start.date().isoformat(), to=end.date().isoformat()
    )
