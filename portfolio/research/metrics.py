"""Indicator metric fetcher functions for use with IndicatorsResearch."""

import math
from collections.abc import Callable
from typing import Any

from twelvedata import TDClient

from portfolio.config.constants import (
    ADX_TIME_PERIOD,
    ATR_TIME_PERIOD,
    BBANDS_SD,
    BBANDS_TIME_PERIOD,
    INDICATORS_INTERVAL,
    RSI_TIME_PERIOD,
    SMA_50_TIME_PERIOD,
    SMA_200_TIME_PERIOD,
)

_MetricFn = Callable[[TDClient, str, int], dict]

_MetricValue = dict[str, float | str | None]


def _to_optional_float(value: Any) -> float | None:
    if value is None:
        return None
    try:
        f = float(value)
    except (TypeError, ValueError):
        return None
    if math.isnan(f) or math.isinf(f):
        return None
    return f


def _dataframe_values(df: Any) -> list[_MetricValue]:
    columns = list(df.columns)
    values: list[_MetricValue] = []
    for idx, row in df.iterrows():
        item: _MetricValue = {"datetime": str(idx)}
        for col in columns:
            item[str(col)] = _to_optional_float(row[col])
        values.append(item)
    return values


def hlc3(client: TDClient, ticker: str, outputsize: int) -> dict:
    df = client.time_series(
        symbol=ticker,
        interval=INDICATORS_INTERVAL,
        outputsize=outputsize,
    ).as_pandas()
    values = [
        {
            "datetime": str(idx),
            "hlc3": (float(row["high"]) + float(row["low"]) + float(row["close"])) / 3,
        }
        for idx, row in df.iterrows()
    ]
    return {"values": values}


def macd(client: TDClient, ticker: str, outputsize: int) -> dict:
    df = (
        client.time_series(symbol=ticker, interval=INDICATORS_INTERVAL, outputsize=outputsize)
        .without_ohlc()
        .with_macd()
        .as_pandas()
    )
    return {"values": _dataframe_values(df)}


def rsi(client: TDClient, ticker: str, outputsize: int) -> dict:
    df = (
        client.time_series(symbol=ticker, interval=INDICATORS_INTERVAL, outputsize=outputsize)
        .without_ohlc()
        .with_rsi(time_period=RSI_TIME_PERIOD, series_type="close")
        .as_pandas()
    )
    return {"values": _dataframe_values(df)}


def atr(client: TDClient, ticker: str, outputsize: int) -> dict:
    df = (
        client.time_series(symbol=ticker, interval=INDICATORS_INTERVAL, outputsize=outputsize)
        .without_ohlc()
        .with_atr(time_period=ATR_TIME_PERIOD)
        .as_pandas()
    )
    return {"values": _dataframe_values(df)}


def bbands(client: TDClient, ticker: str, outputsize: int) -> dict:
    df = (
        client.time_series(symbol=ticker, interval=INDICATORS_INTERVAL, outputsize=outputsize)
        .without_ohlc()
        .with_bbands(series_type="close", time_period=BBANDS_TIME_PERIOD, sd=BBANDS_SD, ma_type="SMA")
        .as_pandas()
    )
    return {"values": _dataframe_values(df)}


def adx_di(client: TDClient, ticker: str, outputsize: int) -> dict:
    df = (
        client.time_series(symbol=ticker, interval=INDICATORS_INTERVAL, outputsize=outputsize)
        .without_ohlc()
        .with_adx(time_period=ADX_TIME_PERIOD)
        .with_plus_di(time_period=ADX_TIME_PERIOD)
        .with_minus_di(time_period=ADX_TIME_PERIOD)
        .as_pandas()
    )
    return {"values": _dataframe_values(df)}


def sma_50(client: TDClient, ticker: str, outputsize: int) -> dict:
    df = (
        client.time_series(symbol=ticker, interval=INDICATORS_INTERVAL, outputsize=outputsize)
        .without_ohlc()
        .with_sma(time_period=SMA_50_TIME_PERIOD, series_type="close")
        .as_pandas()
    )
    return {"values": _dataframe_values(df)}


def sma_200(client: TDClient, ticker: str, outputsize: int) -> dict:
    df = (
        client.time_series(symbol=ticker, interval=INDICATORS_INTERVAL, outputsize=outputsize)
        .without_ohlc()
        .with_sma(time_period=SMA_200_TIME_PERIOD, series_type="close")
        .as_pandas()
    )
    return {"values": _dataframe_values(df)}


_DEFAULT_METRICS: dict[str, _MetricFn] = {
    "hlc3": hlc3,
    "macd": macd,
    "rsi": rsi,
    # "atr": atr,
    # "bbands": bbands,
    "adx_di": adx_di,
    "sma_50": sma_50,
    # "sma_200": sma_200,
}
