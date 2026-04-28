def route_signal(adx: float, sma: str, macd: str, rsi: str, bb: str, stoch: str, obv: str) -> str:
    if adx > 25:
        signals = [sma, macd]
    elif adx <20: 
        signals = [rsi, bb, stoch]
    else:
        signals =[sma, macd, rsi, bb, stoch]
    if signals.count("BUY") > signals.count("SELL"):
        consensus = "BUY"
    elif signals.count("BUY") < signals.count("SELL"):
        consensus = "SELL"
    else:
        consensus = "HOLD"
    if consensus == "BUY" and obv == "SELL":
        consensus = "HOLD"
    elif consensus == "SELL" and obv == "BUY":
        consensus = "HOLD"
    return consensus
