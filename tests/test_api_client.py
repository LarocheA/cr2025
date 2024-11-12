import pytest
from data.api_client import get_crypto_price, get_historical_data, get_fear_and_greed_index

def test_get_crypto_price():
    price = get_crypto_price('BTC')
    assert isinstance(price, float)
    assert price > 0

def test_get_historical_data():
    data = get_historical_data('BTC', limit=10)
    assert isinstance(data, list)
    assert len(data) == 10
    assert 'close' in data[0]

def test_get_fear_and_greed_index():
    index = get_fear_and_greed_index()
    assert isinstance(index, int)
    assert 0 <= index <= 100
