import pandas as pd
import numpy as np
from .api_client import get_crypto_price, get_historical_data, get_fear_and_greed_index

class CryptoData:
    def __init__(self, portfolio):
        self.portfolio = portfolio
        self.current_prices = {}
        self.historical_data = {}
        self.fear_greed_index = None

    def update_prices(self):
        for crypto in self.portfolio:
            try:
                self.current_prices[crypto['symbol']] = get_crypto_price(crypto['symbol'])
            except Exception as e:
                print(f"Erreur lors de la mise à jour du prix pour {crypto['symbol']}: {str(e)}")

    def get_historical_data(self, days=2000):
        for crypto in self.portfolio:
            try:
                self.historical_data[crypto['symbol']] = get_historical_data(crypto['symbol'], limit=days)
            except Exception as e:
                print(f"Erreur lors de la récupération des données historiques pour {crypto['symbol']}: {str(e)}")

    def update_fear_greed_index(self):
        try:
            self.fear_greed_index = get_fear_and_greed_index()
        except Exception as e:
            print(f"Erreur lors de la mise à jour de l'indice Fear and Greed: {str(e)}")

    def to_dataframe(self):
        df = pd.DataFrame(self.portfolio)
        df['current_price'] = df['symbol'].map(self.current_prices)
        df['total_value'] = df['quantity'] * df['current_price']
        return df

    def calculate_volatility(self, window=30):
        volatility = {}
        for symbol, data in self.historical_data.items():
            prices = [d['close'] for d in data]
            returns = pd.Series(prices).pct_change()
            volatility[symbol] = returns.rolling(window=window).std().iloc[-1]
        return volatility

    # 
