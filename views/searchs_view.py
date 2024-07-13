from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel

class SearchsView(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Vista de Búsquedas"))

# ! Para búqsueda binaria
# TODO Buscar un dato en una lista binario
# TODO Mostrar el numero mayor y menor de la lista
# TODO Posición en la que está el dato
# TODO Si hay más de un dato, que se indiquen las posiciones de los datos
    # ? Ejemplo de lista binaria
    # Lista     -> [1, 2, 3, 4, 5, 6, 7, 7, 7, 8, 9, 10]
    # Posición  -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Si hay más:
        # * El número 7 está en las posiciones 6, 7 y 8

# TODO Mostrar un mensaje de error si el dato no existe

# ! Para búqsueda lineal
# TODO Buscar un dato en una lista lineal
# TODO Mostrar el numero mayor y menor de la lista
# TODO Posición en la que está el dato
# TODO Si hay más de un dato, que se indiquen las posiciones de los datos

# TODO Mostrar un mensaje de error si el dato no existe