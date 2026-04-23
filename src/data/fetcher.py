import yfinance as yf
from pandas import DataFrame

def get_historical_data(ticker: str, period: str, interval: str) -> DataFrame:
    data = yf.Ticker(ticker).history(period=period, interval=interval)
    data = data[["Open", "High", "Low", "Close", "Volume"]]
    return data
