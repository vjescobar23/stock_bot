import pandas_ta as ta
import pandas as pd
from pandas import DataFrame

def generate_signals(df: DataFrame) -> DataFrame:
    df = df.copy()
    bb_df = ta.bbands(df["Close"], length=20)
    df = pd.concat([df, bb_df], axis=1)
    df["signal"] = "HOLD"
    df.loc[df["Close"] < df["BBL_20_2.0_2.0"], "signal"] = "BUY"
    df.loc[df["Close"] > df["BBU_20_2.0_2.0"], "signal"] = "SELL"
    return df
