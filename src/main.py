import pandas as pd 
from src.data.universe import UNIVERSE
from src.data.fetcher import get_historical_data
from src.strategies.sma_crossover import generate_signals as sma_signals
from src.strategies.macd import generate_signals as macd_signals
from src.strategies.rsi import generate_signals as rsi_signals
from src.strategies.bollinger_bands import generate_signals as bb_signals
from src.strategies.atr import generate_signals as atr_signals
from src.strategies.adx import generate_signals as adx_signals
from src.strategies.obv import generate_signals as obv_signals
from src.strategies.stochastic import generate_signals as stoch_signals
from src.strategies.router import route_signal
from src.backtesting.engine import run_backtest

def main():
    short_window = 9
    long_window = 21
    tickers = UNIVERSE
    for ticker in tickers:
        df = get_historical_data(ticker, period="6mo", interval="1d")
        sma = sma_signals(df, short_window=short_window, long_window=long_window)
        macd = macd_signals(df)
        rsi = rsi_signals(df)
        bb = bb_signals(df)
        atr = atr_signals(df)
        adx = adx_signals(df)
        obv = obv_signals(df)
        stoch = stoch_signals(df)
        sma_latest = sma.iloc[-1]
        macd_latest = macd.iloc[-1]
        rsi_latest = rsi.iloc[-1]
        bb_latest = bb.iloc[-1]
        atr_latest = atr.iloc[-1]
        adx_latest = adx.iloc[-1]
        obv_latest = obv.iloc[-1]
        stoch_latest = stoch.iloc[-1]
        combined = route_signal(                                                                 
            adx_latest["ADX_14"],
            sma_latest["signal"],                                                               
            macd_latest["signal"],                                                                  
            rsi_latest["signal"],                                                                   
            bb_latest["signal"], 
            stoch_latest["signal"],                                                                   
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
            f"Stochastic: {stoch_latest['signal']}",
            f"Consensus: {combined}",                                                               
            ]                                                                                           
        print(" | ".join(parts))
        routed_signals = []                                                                                                                                                                         
        for i in range(len(df)):                                        
            row_signal = route_signal(
                adx=adx.iloc[i]["ADX_14"],
                sma=sma.iloc[i]["signal"],
                macd=macd.iloc[i]["signal"],                                                                                                                                                        
                rsi=rsi.iloc[i]["signal"],
                bb=bb.iloc[i]["signal"],                                                                                                                                                            
                stoch=stoch.iloc[i]["signal"],                          
                obv=obv.iloc[i]["signal"],
        )                                                                                                                                                                                        
            routed_signals.append(row_signal)                                                                                                                                                                                      
        routed_signals = pd.Series(routed_signals, index=df.index)      
        results = run_backtest(df, routed_signals)                                                                                                                                                                     
        print(                                                                                                                                                                                      
            f"  Backtest → "                                            
            f"Trades: {results['total_trades']} | "                                                                                                                                                 
            f"Win Rate: {results['win_rate']:.0%} | "                                                                                                                                               
            f"Max Drawdown: {results['max_drawdown']:.2%} | "
            f"Sharpe: {results['sharpe']:.2f}"                                                                                                                                                      
        )                                   
if __name__=="__main__":
    main()
