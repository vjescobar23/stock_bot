import pytest
import pandas as pd
from src.strategies.rsi import generate_signals

def test_do_signal_columns_exist():
    df = pd.DataFrame({"Close" : [150] * 125})
    result = generate_signals(df)
    assert "RSI" in result.columns
    assert "signal" in result.columns

def test_signal_logic():
    df = pd.DataFrame({"Close": [float(x) for x in range(100, 50, -1)]})
    result = generate_signals(df)
    latest = result.iloc[-1]
    assert latest["signal"] == "BUY"
