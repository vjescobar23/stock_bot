import pytest
import pandas as pd
from src.strategies.sma_crossover import generate_signals

def test_do_signal_columns_exists():
    df = pd.DataFrame({"Close" : [150] * 25})
    result = generate_signals(df)
    assert "SMA_9" in result.columns
    assert "SMA_21" in result.columns
    assert "signal" in result.columns

def test_buy_short_over_long():
    df = pd.DataFrame({"Close" : list(range(100, 125))})
    result = generate_signals(df)
    latest = result.iloc[-1]
    assert latest["signal"] == "BUY"
