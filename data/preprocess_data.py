# preprocess_data.py
import pandas as pd

def preprocess_data(data):
    for ticker, df in data.items():
        df.dropna(inplace=True)
        df['Date'] = pd.to_datetime(df.index)
        df.set_index('Date', inplace=True)
    return data

if __name__ == "__main__":
    tickers = ['AAPL', 'MSFT', 'AMZN', 'GOOGL', 'FB', 'TSLA', 'BRK-B', 'JNJ', 'V', 'NVDA']
    data = {}
    for ticker in tickers:
        df = pd.read_csv(f'data/{ticker}.csv', index_col=0)
        data[ticker] = df
    processed_data = preprocess_data(data)
    for ticker, df in processed_data.items():
        df.to_csv(f'data/processed_{ticker}.csv')
