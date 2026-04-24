# Stock Bot
This is a wip automated stock trading bot built as a python learning exercise. Currently, the program uses data from Yahoo Finance (yf) and determines BUY/SELL consensus from signals derived from DataFrames of common stock trading metrics.

## Dependencies
pandas
pandas_ta
pytest
python-dotenv
yfinance
alpaca-py
### Signals Tracked
Simple Moving Average Crossover (sma or sma_crossover)
Moving Average Convergence/Divergence (macd)
Relative Strength Index (rsi)
Bollinger Bands (bb)
Average True Range (atr)

# Alpaca API*
In order to connect the bot to a trading platform a free API key from Alpaca is needed. these should be stored securely in a .env 






WIP*