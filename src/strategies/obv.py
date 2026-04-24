import pandas as pd
import pandas_ta as ta
from pandas import DataFrame

def generate_signals(df: DataFrame) -> DataFrame:
    df = df.copy()
    df["OBV"] = ta.obv(df["Close"], df["Volume"])
    df["OBV_SMA"] = ta.sma(df["OBV"], length=20)
    df["signal"] = "HOLD"
    df.loc[df["OBV"] > df["OBV_SMA"], "signal"] = "BUY"
    df.loc[df["OBV"] < df["OBV_SMA"], "signal"] = "SELL"
    return df