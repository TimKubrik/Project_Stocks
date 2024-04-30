import yfinance as yf
import talib as ta

def fetch_stock_data(ticker, period='1mo'):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data

def add_moving_average(data, window_size=5):
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data

def add_rsi(data, time_period=14):

    data['RSI'] = ta.RSI(data['Close'].values, timeperiod=time_period)
    return data

def add_macd(data):

    macd, signal, hist = ta.MACD(data['Close'].values, fastperiod=10, slowperiod=2, signalperiod=5)
    data['MACD'] = macd
    data['MACD_Signal'] = signal
    data['MACD_Histogram'] = hist
    return data
