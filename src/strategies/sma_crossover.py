import pandas_ta as ta
from pandas import DataFrame

def generate_signals(df: DataFrame, short_window: int = 9, long_window: int = 21) -> DataFrame:
    df = df.copy()
    df[f"SMA_{short_window}"] = ta.sma(df["Close"], length=short_window)
    df[f"SMA_{long_window}"] = ta.sma(df["Close"], length=long_window)
    df["signal"] = "HOLD"
    df.loc[df[f"SMA_{short_window}"] > df[f"SMA_{long_window}"], "signal"] = "BUY"
    df.loc[df[f"SMA_{short_window}"] < df[f"SMA_{long_window}"], "signal"] = "SELL"
    return df



