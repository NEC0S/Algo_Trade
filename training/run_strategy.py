# run_strategy.py
import backtrader as bt
from strategies.trend_following import TrendFollowing
from strategies.mean_reversion import MeanReversion

if __name__ == "__main__":
    cerebro = bt.Cerebro()

    # Add data feed here (example):
    # data = bt.feeds.YahooFinanceCSVData(dataname='data/processed_AAPL.csv')
    # cerebro.adddata(data)

    cerebro.addstrategy(TrendFollowing)
    cerebro.addstrategy(MeanReversion)

    cerebro.run()
    cerebro.plot()

