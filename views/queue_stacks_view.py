from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel

class QueueStacksView(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Vista de Pilas y Colas"))

# TODO Agregar métodos específicos para la funcionalidad de Pilas y Colas.