from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel

class StatisticsView(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Vista de Estadística Descriptiva"))