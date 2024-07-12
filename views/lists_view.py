from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel

class ListsView(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Vista de Listas"))

# TODO Agregar métodos específicos para la funcionalidad de Listas.