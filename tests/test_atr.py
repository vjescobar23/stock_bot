import pytest
import pandas as pd
from src.strategies.atr import generate_signals

def test_columns_exist():
    df = pd.DataFrame({"High": [155.0] * 50, "Low": [145] * 50, "Close": [150.0] * 50})
    result = generate_signals(df)
    assert "ATR" in result.columns
    assert "signal" in result.columns

def test_signal_logic():
    df = pd.DataFrame({"High": [155.0] * 50, "Low": [145] * 50, "Close": [150.0] * 50})
    result = generate_signals(df)
    latest = result.iloc[-1]
    assert not pd.isna(latest["ATR"]) 
    assert latest["ATR"] > 0 
