# data/crypto_data.py

from .api_client import get_crypto_price

def update_portfolio_prices(portfolio):
    for crypto in portfolio:
        crypto['price'] = get_crypto_price(crypto['symbol'])
    return portfolio
