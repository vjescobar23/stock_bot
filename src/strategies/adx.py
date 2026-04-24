import pandas as pd
import pandas_ta as ta 
from pandas import DataFrame

def generate_signals(df: DataFrame) -> DataFrame:
    df = df.copy()
    adx_df = ta.adx(df["High"], df["Low"], df["Close"], length=14)
    df = pd.concat([df, adx_df], axis=1)
    df["signal"] = "HOLD"
    return df