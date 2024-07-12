from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel

class TreesView(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Vista de Árboles"))

    # TODO Agregar métodos específicos para la funcionalidad de Árboles.
