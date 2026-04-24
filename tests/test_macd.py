import pytest
import pandas as pd
from src.strategies.macd import generate_signals

def test_do_signal_columns_exist():
    df = pd.DataFrame({"Close" : [150] * 125})
    result = generate_signals(df)
    assert "MACD_12_26_9" in result.columns
    assert "MACDs_12_26_9" in result.columns
    assert "signal" in result.columns

def test_signal_logic():
    df = pd.DataFrame({"Close": [100.0] * 35 + [float(100 + i * 3) for i in range(15)]})
    result = generate_signals(df)
    latest = result.iloc[-1]
    assert latest["signal"] == "BUY"
