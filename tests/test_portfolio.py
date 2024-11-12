import pytest
from portfolio.portfolio import Portfolio
from data.crypto_data import CryptoData

@pytest.fixture
def sample_portfolio():
    crypto_data = CryptoData([{'symbol': 'BTC', 'quantity': 1}])
    return Portfolio(crypto_data)

def test_get_total_value(sample_portfolio):
    total_value = sample_portfolio.get_total_value()
    assert isinstance(total_value, float)
    assert total_value >= 0

def test_get_asset_allocation(sample_portfolio):
    allocation = sample_portfolio.get_asset_allocation()
    assert isinstance(allocation, dict)
    assert 'BTC' in allocation
    assert 0 <= allocation['BTC'] <= 100
