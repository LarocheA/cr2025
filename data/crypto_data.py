# data/crypto_data.py

import pandas as pd
from .api_client import get_crypto_price, get_historical_data

def update_portfolio_prices(portfolio):
    for crypto in portfolio:
        crypto['price'] = get_crypto_price(crypto['symbol'])
    return portfolio

def get_historical_dataframe(portfolio):
    historical_data = {}
    for crypto in portfolio:
        historical_data[crypto['symbol']] = get_historical_data(crypto['symbol'])
    return pd.DataFrame(historical_data)
