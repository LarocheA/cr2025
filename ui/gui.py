import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt
from portfolio.portfolio import Portfolio
from data.crypto_data import CryptoData
from analysis.visualization import plot_portfolio_allocation, plot_price_history

class CryptoPortfolioGUI(QMainWindow):
    def __init__(self, portfolio):
        super().__init__()
        self.portfolio = portfolio
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Crypto Portfolio Tracker')
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Boutons
        update_button = QPushButton('Mettre à jour les prix')
        update_button.clicked.connect(self.update_prices)
        layout.addWidget(update_button)

        plot_allocation_button = QPushButton('Afficher l\'allocation du portefeuille')
        plot_allocation_button.clicked.connect(self.show_portfolio_allocation)
        layout.addWidget(plot_allocation_button)

        plot_history_button = QPushButton('Afficher l\'historique des prix')
        plot_history_button.clicked.connect(self.show_price_history)
        layout.addWidget(plot_history_button)

        # Table pour afficher le portefeuille
        self.portfolio_table = QTableWidget()
        self.portfolio_table.setColumnCount(4)
        self.portfolio_table.setHorizontalHeaderLabels(['Crypto', 'Quantité', 'Prix', '
