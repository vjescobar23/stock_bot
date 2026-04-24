from src.data.fetcher import get_historical_data
from src.strategies.sma_crossover import generate_signals as sma_signals
from src.strategies.macd import generate_signals as macd_signals
from src.strategies.rsi import generate_signals as rsi_signals
from src.strategies.bollinger_bands import generate_signals as bb_signals
from src.strategies.atr import generate_signals as atr_signals
from src.strategies.adx import generate_signals as adx_signals
from src.strategies.obv import generate_signals as obv_signals

def signal_majority(sma: str, macd: str, rsi: str, bb: str, obv:str) -> str:
    signals = [sma, macd, rsi, bb, obv]
    if signals.count("BUY") > signals.count("SELL"):
        simple_consensus = "BUY"
    elif signals.count("BUY") < signals.count("SELL"):
        simple_consensus = "SELL"
    else:
        simple_consensus = "HOLD"
    return simple_consensus
def main():
    short_window = 9
    long_window = 21
    tickers = ["AAPL", "MSFT", "NVDA", "INTC"]
    for ticker in tickers:
        df = get_historical_data(ticker, period="6mo", interval="1d")
        sma = sma_signals(df, short_window=short_window, long_window=long_window)
        macd = macd_signals(df)
        rsi = rsi_signals(df)
        bb = bb_signals(df)
        atr = atr_signals(df)
        adx = adx_signals(df)
        obv = obv_signals(df)
        sma_latest = sma.iloc[-1]
        macd_latest = macd.iloc[-1]
        rsi_latest = rsi.iloc[-1]
        bb_latest = bb.iloc[-1]
        atr_latest = atr.iloc[-1]
        adx_latest = adx.iloc[-1]
        obv_latest = obv.iloc[-1]
        combined = signal_majority(                                                                 
            sma_latest["signal"],                                                                   
            macd_latest["signal"],                                                                  
            rsi_latest["signal"],                                                                   
            bb_latest["signal"],                                                                    
            obv_latest["signal"],                                       
        )
        parts = [                                                                                   
            f"{ticker}",
            f"Close: {sma_latest['Close']:.2f}",                                                    
            f"SMA: {sma_latest['signal']}",
            f"MACD: {macd_latest['signal']}",                                                       
            f"RSI: {rsi_latest['signal']}",                             
            f"Bollinger Bands: {bb_latest['signal']}",
            f"OBV: {obv_latest['signal']}",
            f"ATR: {atr_latest['ATR']:.2f}",                                                        
            f"ADX: {adx_latest['ADX_14']:.2f}", 
            f"Consensus: {combined}",                                                               
            ]                                                                                           
        print(" | ".join(parts))
if __name__=="__main__":
    main()
