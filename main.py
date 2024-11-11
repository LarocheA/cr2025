from config import PORTFOLIO
from data.crypto_data import CryptoData
from portfolio.portfolio import Portfolio
from analysis.calculations import calculate_portfolio_return, calculate_sharpe_ratio, calculate_correlation_matrix

def main():
    crypto_data = CryptoData(PORTFOLIO)
    crypto_data.update_prices()
    crypto_data.get_historical_data()
    crypto_data.update_fear_greed_index()

    portfolio = Portfolio(crypto_data)

    print(f"Total Portfolio Value: ${portfolio.get_total_value():.2f}")
    print(f"Portfolio Return: {calculate_portfolio_return(portfolio):.2f}%")
    print(f"Sharpe Ratio: {calculate_sharpe_ratio(portfolio):.2f}")
    print(f"Fear and Greed Index: {crypto_data.fear_greed_index}")

    correlation_matrix = calculate_correlation_matrix(portfolio)
    print("Correlation Matrix:")
    print(correlation_matrix)

if __name__ == "__main__":
    main()
