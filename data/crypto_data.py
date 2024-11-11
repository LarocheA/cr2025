# data/crypto_data.py

import pandas as pd
from .api_client import get_crypto_price, get_historical_data

class CryptoData:
    def __init__(self):
        self.current_prices = {}
        self.historical_data = {}

    def update_prices(self, symbols):
        for symbol in symbols:
            self.current_prices[symbol] = get_crypto_price(symbol)

    def get_historical_data(self, symbols, days=2000):
        for symbol in symbols:
            self.historical_data[symbol] = get_historical_data(symbol, limit=days)

    def to_dataframe(self):
        df = pd.DataFrame(self.current_prices.items(), columns=['symbol', 'price'])
        return df

    def get_historical_prices(symbols, days=365):
    historical_data = {}
        for symbol in symbols:
        data = get_historical_data(symbol, limit=days)
        historical_data[symbol] = pd.DataFrame(data)
        return historical_data

    def calculate_returns(historical_data):
    returns = {}
        for symbol, data in historical_data.items():
        returns[symbol] = data['close'].pct_change().dropna()
        return pd.DataFrame(returns)
