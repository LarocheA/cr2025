import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtChart import QChart, QChartView, QPieSeries
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
        self.portfolio_table.setHorizontalHeaderLabels(['Crypto', 'Quantité', 'Prix', 'Valeur Totale'])
        self.portfolio_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.portfolio_table.setSortingEnabled(True)
        layout.addWidget(self.portfolio_table)

        # Graphique en camembert pour l'allocation
        self.chart_view = QChartView()
        layout.addWidget(self.chart_view)

        self.update_portfolio_table()
        self.update_allocation_chart()

        # Timer pour mettre à jour automatiquement les données
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_prices)
        self.timer.start(60000)  # Mise à jour toutes les minutes

    def update_prices(self):
        crypto_data = CryptoData()
        crypto_data.update_prices()
        self.portfolio.update_prices(crypto_data)
        self.update_portfolio_table()
        self.update_allocation_chart()

    def update_portfolio_table(self):
        df = self.portfolio.to_dataframe()
        self.portfolio_table.setRowCount(len(df))
        for i, (index, row) in enumerate(df.iterrows()):
            self.portfolio_table.setItem(i, 0, QTableWidgetItem(row['symbol']))
            self.portfolio_table.setItem(i, 1, QTableWidgetItem(str(row['quantity'])))
            self.portfolio_table.setItem(i, 2, QTableWidgetItem(f"${row['price']:.2f}"))
            self.portfolio_table.setItem(i, 3, QTableWidgetItem(f"${row['total_value']:.2f}"))

    def update_allocation_chart(self):
        series = QPieSeries()
        for index, row in self.portfolio.to_dataframe().iterrows():
            series.append(row['symbol'], row['total_value'])

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Allocation du portefeuille")
        self.chart_view.setChart(chart)

    def show_portfolio_allocation(self):
        plot_portfolio_allocation(self.portfolio)

    def show_price_history(self):
        plot_price_history(self.portfolio)

def run_gui(portfolio):
    app = QApplication(sys.argv)
    ex = CryptoPortfolioGUI(portfolio)
    ex.show()
    sys.exit(app.exec_())
