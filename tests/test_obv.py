import pytest                                                                               
import pandas as pd                                                                         
from src.strategies.obv import generate_signals                                             
                                                                                              
def test_columns_exist():                   
      closes = [float(i) for i in range(50, 100)]                                             
      df = pd.DataFrame({                                         
          "Close": closes,                                                                    
          "Volume": [1000000.0] * 50
      })                                                                                      
      result = generate_signals(df)                               
      assert "OBV" in result.columns
      assert "OBV_SMA" in result.columns                                                      
      assert "signal" in result.columns
                                                                                              
def test_buy_signal_on_rising_price():                          
      closes = [float(i) for i in range(50, 100)]
      df = pd.DataFrame({                                                                     
          "Close": closes,
          "Volume": [1000000.0] * 50                                                          
      })                                                          
      result = generate_signals(df)
      assert result.iloc[-1]["signal"] == "BUY"