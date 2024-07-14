from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel

class StatisticsView(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Vista de Estadística Descriptiva"))
        
# TODO Agregar un botón de estadística descriptiva donde habrá un input para ingresar datos, datos aleatorios y de excel, y mostrará la media, mediana, moda, rango, varianza, desviación estándar, coeficiente de variación.