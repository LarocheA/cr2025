import pytest
from data.crypto_data import CryptoData
from portfolio.portfolio import Portfolio

@pytest.fixture
def sample_crypto_data():
    return CryptoData([
        {'symbol': 'BTC', 'quantity': 1},
        {'symbol': 'ETH', 'quantity': 10}
    ])

@pytest.fixture
def sample_portfolio(sample_crypto_data):
    return Portfolio(sample_crypto_data)
