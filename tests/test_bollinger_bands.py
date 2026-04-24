import pytest
import pandas as pd
from src.strategies.bollinger_bands import generate_signals

def test_signal_column_exist():
    df = pd.DataFrame({"Close" : [150] * 125})
    result = generate_signals(df)
    assert "BBL_20_2.0_2.0" in result.columns
    assert "BBU_20_2.0_2.0" in result.columns
    assert "BBM_20_2.0_2.0" in result.columns
    assert "signal" in result.columns

def test_signal_logic():
    df = pd.DataFrame({"Close": [100.0] * 49 + [30.0]})
    result = generate_signals(df)
    latest = result.iloc[-1]
    assert latest["signal"] == "BUY"

