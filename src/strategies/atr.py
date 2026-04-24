import pandas_ta as ta 
from pandas import DataFrame

def generate_signals(df: DataFrame) -> DataFrame:
    df = df.copy()
    df["ATR"] = ta.atr(df["High"], df["Low"], df["Close"], length=14)
    df["signal"] = "HOLD"
    return df
