# portfolio/portfolio.py

import pandas as pd
import numpy as np

class Portfolio:
    def __init__(self, crypto_list):
        self.crypto_list = crypto_list
        self.df = pd.DataFrame(crypto_list)

    def update_prices(self, crypto_data):
        self.df = self.df.merge(crypto_data.to_dataframe(), on='symbol', how='left')
        self.df['total_value'] = self.df['quantity'] * self.df['price']

    def get_total_value(self):
        return self.df['total_value'].sum()

    def get_asset_allocation(self):
        self.df['allocation'] = self.df['total_value'] / self.get_total_value() * 100
        return self.df[['symbol', 'allocation']]

    def calculate_returns(self):
        self.df['returns'] = self.df['price'].pct_change()
        return self.df['returns']

    def calculate_volatility(self):
        return self.df['returns'].std() * np.sqrt(252)  # Assuming 252 trading days in a year

    def calculate_sharpe_ratio(self, risk_free_rate=0.02):
        returns = self.calculate_returns()
        volatility = self.calculate_volatility()
        return (returns.mean() - risk_free_rate) / volatility

    def to_dataframe(self):
        return self.df
