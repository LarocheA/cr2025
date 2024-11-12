import pytest
from analysis.calculations import calculate_portfolio_return, calculate_sharpe_ratio

def test_calculate_portfolio_return():
    portfolio_value = 11000
    initial_value = 10000
    returns = calculate_portfolio_return(portfolio_value, initial_value)
    assert returns == 10.0

def test_calculate_sharpe_ratio():
    returns = [0.05, 0.03, 0.08, -0.01]
    risk_free_rate = 0.02
    ratio = calculate_sharpe_ratio(returns, risk_free_rate)
    assert isinstance(ratio, float)