import pandas_ta as ta
import pandas as pd
from pandas import DataFrame

def generate_signals(df: DataFrame) -> DataFrame:
    df = df.copy()
    macd_df = ta.macd(df["Close"], fast=12, slow=26, signal=9)
    df = pd.concat([df, macd_df], axis=1)
    df["signal"] = "HOLD"
    df.loc[df["MACD_12_26_9"] > df["MACDs_12_26_9"], "signal"] = "BUY"
    df.loc[df["MACD_12_26_9"] < df["MACDs_12_26_9"], "signal"] = "SELL"
    return df
