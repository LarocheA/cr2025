import cvxpy as cp
import numpy as np

def optimize_portfolio(returns, risk_free_rate=0.02):
    n = returns.shape[1]
    mu = returns.mean().values
    Sigma = returns.cov().values

    w = cp.Variable(n)
    ret = mu.T @ w
    risk = cp.quad_form(w, Sigma)
    sharpe_ratio = (ret - risk_free_rate) / cp.sqrt(risk)

    prob = cp.Problem(cp.Maximize(sharpe_ratio),
                      [cp.sum(w) == 1, w >= 0])
    prob.solve()

    return w.value

def get_efficient_frontier(returns, num_portfolios=100):
    n = returns.shape[1]
    mu = returns.mean().values
    Sigma = returns.cov().values

    efficient_portfolios = []
    for target_return in np.linspace(mu.min(), mu.max(), num_portfolios):
        w = cp.Variable(n)
        risk = cp.quad_form(w, Sigma)
        prob = cp.Problem(cp.Minimize(risk),
                          [mu.T @ w >= target_return,
                           cp.sum(w) == 1,
                           w >= 0])
        prob.solve()
        if prob.status == 'optimal':
            efficient_portfolios.append({
                'weights': w.value,
                'return': target_return,
                'risk': np.sqrt(risk.value)
            })

    return efficient_portfolios
