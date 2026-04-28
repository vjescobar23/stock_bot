from src.strategies.router import route_signal 

from src.strategies.router import route_signal                                                                                                                                              
                                                                                                                                                                                              
def test_trending_buy():                                                                                                                                                                    
   result = route_signal(adx=30, sma="BUY", macd="BUY", rsi="HOLD", bb="HOLD", stoch="HOLD", obv="BUY")
   assert result == "BUY"                                                                                                                                                                  
   
def test_ranging_sell():                                                                                                                                                                    
    result = route_signal(adx=15, sma="HOLD", macd="HOLD", rsi="SELL", bb="SELL", stoch="SELL", obv="SELL")
    assert result == "SELL"                                                                                                                                                                 
   
def test_obv_downgrades():                                                                                                                                                                  
    result = route_signal(adx=30, sma="BUY", macd="BUY", rsi="HOLD", bb="HOLD", stoch="HOLD", obv="SELL")
    assert result == "HOLD"                                                                                                                                                                 
   
def test_ambiguous_hold():                                                                                                                                                                  
    result = route_signal(adx=22, sma="BUY", macd="SELL", rsi="BUY", bb="SELL", stoch="HOLD", obv="HOLD")
    assert result == "HOLD"