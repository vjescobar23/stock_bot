import pandas as pd 
from pandas import DataFrame, Series

def run_backtest(df: DataFrame, signals: Series) -> dict:
    cash = 100000.0
    shares = 0.0
    in_position = False
    buy_price = None
    trades = []
    portfolio_values = []
    for i in range(len(df)):
        price = df["Close"].iloc[i]
        signal = signals.iloc[i]
        if signal == "BUY" and in_position == False:
            shares = cash / price
            cash = 0
            in_position = True
            buy_price = price
        elif signal =="SELL" and in_position == True:
            cash = shares * price
            trade_return = (price - buy_price) / buy_price
            trades.append(trade_return)
            in_position = False
            shares = 0
        portfolio_values.append(cash + shares * price)
    if trades:                                                                                                                                                                                  
        win_rate = len([t for t in trades if t > 0]) / len(trades)  
    else:                                                         
        win_rate = 0.0
    portfolio_series = pd.Series(portfolio_values)
    rolling_max = portfolio_series.cummax()                                                                                                                                                     
    drawdown = (portfolio_series - rolling_max) / rolling_max       
    max_drawdown = drawdown.min()
    daily_returns = portfolio_series.pct_change().dropna()
    if daily_returns.std() == 0:                                                                                                                                                                
        sharpe = 0.0                                                
    else:           
        sharpe = (daily_returns.mean() / daily_returns.std()) * (252 ** 0.5)
    return {                                                                                                                                                                                    
        "win_rate": win_rate,                                       
        "max_drawdown": max_drawdown,
        "sharpe": sharpe,                                                                                                                                                                       
        "total_trades": len(trades)
    }
