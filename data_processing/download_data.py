# download_data.py
import yfinance as yf
import pandas as pd

def download_stock_data(tickers, start_date, end_date):
    data = {}
    for ticker in tickers:
        stock_data = yf.download(ticker, start=start_date, end=end_date)
        data[ticker] = stock_data
    return data

if __name__ == "__main__":
    tickers = ['AAPL', 'MSFT', 'AMZN', 'GOOGL', 'FB', 'TSLA', 'BRK-B', 'JNJ', 'V', 'NVDA']
    start_date = '2020-01-01'
    end_date = '2023-01-01'
    data = download_stock_data(tickers, start_date, end_date)
    for ticker, df in data.items():
        df.to_csv(f'data/{ticker}.csv')
