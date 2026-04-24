import pandas_ta as ta
from pandas import DataFrame

def generate_signals(df: DataFrame) -> DataFrame:
    df = df.copy()
    df["RSI"] = ta.rsi(df["Close"], length=14)
    df["signal"] = "HOLD"
    df.loc[df["RSI"] < 30, "signal"] = "BUY"
    df.loc[df["RSI"] > 70, "signal"] = "SELL"
    return df 
