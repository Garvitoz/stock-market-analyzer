import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def analyze_stock(ticker):
    stock = yf.Ticker(ticker)
    data = stock.history(period="6mo")
    data['SMA20'] = data['Close'].rolling(window=20).mean()
    data['SMA50'] = data['Close'].rolling(window=50).mean()

    print(f"\nStock: {ticker}")
    print("Last 5 Days Data:")
    print(data.tail())

    plt.figure(figsize=(10,5))
    plt.plot(data['Close'], label='Close Price', linewidth=1.5)
    plt.plot(data['SMA20'], label='SMA 20', linestyle='--')
    plt.plot(data['SMA50'], label='SMA 50', linestyle='--')
    plt.title(f'{ticker} - Price & Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price (INR)')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    ticker = input("Enter Stock Symbol (e.g., TCS.NS): ").upper()
    analyze_stock(ticker)
