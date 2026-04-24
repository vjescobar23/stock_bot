from src.data.fetcher import get_historical_data
from src.strategies.sma_crossover import generate_signals as sma_signals
from src.strategies.macd import generate_signals as macd_signals
from src.strategies.rsi import generate_signals as rsi_signals

def signal_majority(sma: str, macd: str, rsi: str) -> str:
    signals = [sma, macd, rsi]
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
    tickers = ["AAPL", "MSFT", "NVDA"]
    for ticker in tickers:
        df = get_historical_data(ticker, period="6mo", interval="1d")
        sma = sma_signals(df, short_window=short_window, long_window=long_window)
        macd = macd_signals(df)
        rsi = rsi_signals(df)
        sma_latest = sma.iloc[-1]
        macd_latest = macd.iloc[-1]
        rsi_latest = rsi.iloc[-1]
        combined = signal_majority(sma_latest["signal"], macd_latest["signal"], rsi_latest["signal"])
        print(f"{ticker} | Close: {sma_latest['Close']:.2f} | SMA: {sma_latest['signal']} | MACD: {macd_latest['signal']} | RSI: {rsi_latest['signal']} | Consensus: {combined}") 
if __name__=="__main__":
    main()
