import pandas as pd                                                                                                                                                                         
import pytest                                                                                                                                                                               
from src.backtesting.engine import run_backtest                                                                                                                                             
                                                                                                                                                                                              
def test_returns_dict():                                                                                                                                                                    
    df = pd.DataFrame({"Close": [100.0] * 50})                                                                                                                                              
    signals = pd.Series(["HOLD"] * 50)                                                                                                                                                      
    result = run_backtest(df, signals)                          
    assert "win_rate" in result                                                                                                                                                             
    assert "max_drawdown" in result                                                                                                                                                         
    assert "sharpe" in result
    assert "total_trades" in result                                                                                                                                                         
                                                                  
def test_no_trades():                                                                                                                                                                       
    df = pd.DataFrame({"Close": [100.0] * 50})
    signals = pd.Series(["HOLD"] * 50)                                                                                                                                                      
    result = run_backtest(df, signals)                          
    assert result["total_trades"] == 0                                                                                                                                                      
    assert result["win_rate"] == 0.0
                                                                                                                                                                                            
def test_perfect_uptrend():                                     
    closes = [float(i) for i in range(50, 100)]
    df = pd.DataFrame({"Close": closes})                                                                                                                                                    
    signals = pd.Series(["HOLD"] * 50)
    signals.iloc[0] = "BUY"                                                                                                                                                                 
    signals.iloc[-1] = "SELL"                                                                                                                                                               
    result = run_backtest(df, signals)
    assert result["total_trades"] == 1                                                                                                                                                      
    assert result["win_rate"] == 1.0 