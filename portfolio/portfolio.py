import pandas as pd
import numpy as np

class Portfolio:
    def __init__(self, crypto_data):
        self.crypto_data = crypto_data
        self.df = self.crypto_data.to_dataframe()

    def get_total_value(self):
        return self.df['total_value'].sum()

    def get_asset_allocation(self):
        self.df['allocation'] = self.df['total_value'] / self.get_total_value() * 100
        return self.df[['symbol', 'allocation']]

    def calculate_returns(self):
        for symbol in self.df['symbol']:
            hist_data = pd.DataFrame(self.crypto_data.historical_data[symbol])
            self.df.loc[self.df['symbol'] == symbol, 'returns'] = hist_data['close'].pct_change().mean()
        return self.df['returns']

    def calculate_volatility(self):
        for symbol in self.df['symbol']:
            hist_data = pd.DataFrame(self.crypto_data.historical_data[symbol])
            self.df.loc[self.df['symbol'] == symbol, 'volatility'] = hist_data['close'].pct_change().std() * np.sqrt(365)
        return self.df['volatility']

    def to_dataframe(self):
        return self.df
