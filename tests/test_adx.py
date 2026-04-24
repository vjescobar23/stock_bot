import pytest
import pandas as pd
from src.strategies.adx import generate_signals 

def test_signal_column_exist():
    closes = [float(i) for i in range(50,100)]
    df = pd.DataFrame({"High": [c + 2.0 for c in closes], "Low": [c- 2.0 for c in closes], "Close": closes})
    result = generate_signals(df)                               
    assert "ADX_14" in result.columns
    assert "signal" in result.columns   

def test_signal_logic():
    closes = [float(i) for i in range(50,100)]
    df = pd.DataFrame({"High": [c + 2.0 for c in closes], "Low": [c- 2.0 for c in closes], "Close": closes})
    result = generate_signals(df)
    latest = result.iloc[-1]
    assert latest["signal"] == "HOLD"                                                       
    assert not pd.isna(latest["ADX_14"])                        
    assert 0 <= latest["ADX_14"] <= 100
