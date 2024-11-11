# analysis/visualization.py

import matplotlib.pyplot as plt
import seaborn as sns

def plot_asset_allocation(portfolio):
    allocation = portfolio.get_asset_allocation()
    plt.figure(figsize=(10, 6))
    plt.pie(allocation['allocation'], labels=allocation['symbol'], autopct='%1.1f%%')
    plt.title('Portfolio Asset Allocation')
    plt.axis('equal')
    plt.show()

def plot_efficient_frontier(efficient_frontier, optimal_portfolio):
    plt.figure(figsize=(10, 6))
    plt.scatter(efficient_frontier['Volatility'], efficient_frontier['Return'], c=efficient_frontier['Return'] / efficient_frontier['Volatility'], marker='o')
    plt.plot(optimal_portfolio['Volatility'], optimal_portfolio['Return'], 'r*', markersize=15)
    plt.colorbar(label='Sharpe ratio')
    plt.xlabel('Volatility')
    plt.ylabel('Return')
    plt.title('Efficient Frontier')
    plt.show()

def plot_correlation_heatmap(returns):
    plt.figure(figsize=(12, 10))
    sns.heatmap(returns.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Correlation Heatmap')
    plt.show()

def plot_optimized_weights(weights, symbols):
    plt.figure(figsize=(10, 6))
    plt.bar(symbols, weights)
    plt.title('Poids optimisés du portefeuille')
    plt.xlabel('Cryptomonnaies')
    plt.ylabel('Poids')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
