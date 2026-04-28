import pandas_ta as ta
from pandas import DataFrame
import pandas as pd



def generate_signals(df: DataFrame) -> DataFrame:
    df = df.copy()
    stoch_df = ta.stoch(df["High"], df["Low"], df["Close"], k=14, d=3, smooth_k=3)
    df = pd.concat([df, stoch_df], axis=1)
    df["signal"] = "HOLD"
    df.loc[df["STOCHk_14_3_3"] < 20, "signal"] = "BUY"
    df.loc[df["STOCHk_14_3_3"] > 70, "signal"] = "SELL"
    return df 


