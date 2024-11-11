import pandas as pd
from .api_client import get_crypto_price, get_historical_data, get_fear_and_greed_index

class CryptoData:
    def __init__(self, portfolio):
        self.portfolio = portfolio
        self.current_prices = {}
        self.historical_data = {}
        self.fear_greed_index = None

    def update_prices(self):
        for crypto in self.portfolio:
            self.current_prices[crypto['symbol']] = get_crypto_price(crypto['symbol'])

    def get_historical_data(self, days=2000):
        for crypto in self.portfolio:
            self.historical_data[crypto['symbol']] = get_historical_data(crypto['symbol'], limit=days)

    def update_fear_greed_index(self):
        self.fear_greed_index = get_fear_and_greed_index()

    def to_dataframe(self):
        df = pd.DataFrame(self.portfolio)
        df['current_price'] = df['symbol'].map(self.current_prices)
        df['total_value'] = df['quantity'] * df['current_price']
        return df
