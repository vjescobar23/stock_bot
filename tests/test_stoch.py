import pytest                                                                                                                                                                               
import pandas as pd                                                                                                                                                                         
from src.strategies.stochastic import generate_signals
                                                                                                                                                                                              
def test_columns_exist():                                       
    closes = [float(i) for i in range(50, 100)]
    df = pd.DataFrame({
        "High": [c + 2.0 for c in closes],
        "Low": [c - 2.0 for c in closes],                                                                                                                                                   
        "Close": closes
    })                                                                                                                                                                                      
    result = generate_signals(df)                               
    assert "STOCHk_14_3_3" in result.columns
    assert "STOCHd_14_3_3" in result.columns                                                                                                                                                
    assert "signal" in result.columns
                                                                                                                                                                                              
def test_buy_signal():                                          
    closes = [float(i) for i in range(100, 50, -1)]
    df = pd.DataFrame({
        "High": [c + 2.0 for c in closes],                                                                                                                                                  
        "Low": [c - 2.0 for c in closes],
        "Close": closes                                                                                                                                                                     
    })                                                          
    result = generate_signals(df)
    assert result.iloc[-1]["signal"] == "BUY"
                                                                                                                                                                                              
def test_sell_signal():
    closes = [float(i) for i in range(50, 100)]                                                                                                                                             
    df = pd.DataFrame({                                         
        "High": [c + 2.0 for c in closes],
        "Low": [c - 2.0 for c in closes],                                                                                                                                                   
        "Close": closes
    })                                                                                                                                                                                      
    result = generate_signals(df)                               
    assert result.iloc[-1]["signal"] == "SELL"
