from src.data.fetcher import get_historical_data
from src.strategies.sma_crossover import generate_signals

def main():
    short_window = 9
    long_window = 21
    tickers = ["AAPL", "MSFT", "NVDA"]
    for ticker in tickers:
        df = get_historical_data(ticker, period="6mo", interval="1d")
        df = generate_signals(df, short_window=short_window, long_window=long_window)
        latest = df.iloc[-1]
        print(f"{ticker} | Signal: {latest['signal']} | Close: {latest['Close']:.2f} | SMA Short: {latest[f'SMA_{short_window}']:.2f} | SMA Long: {latest[f'SMA_{long_window}']:.2f}")
        
if __name__=="__main__":
    main()
