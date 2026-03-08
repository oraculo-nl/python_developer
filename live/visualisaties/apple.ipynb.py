import yfinance as yf

# Download daily OHLCV data (default: ~1 month)
df = yf.download("AAPL", period="1y", interval="1d")

