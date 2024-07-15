# indicators.py
import backtrader.indicators as btind

def add_indicators(data):
    data['sma'] = btind.SimpleMovingAverage(data.close, period=20)
    data['ema'] = btind.ExponentialMovingAverage(data.close, period=20)
    data['bollinger'] = btind.BollingerBands(data.close, period=20)
    data['rsi'] = btind.RelativeStrengthIndex(data.close, period=14)

    return data
