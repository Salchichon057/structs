import sys
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QInputDialog, QHBoxLayout, QLabel, QMessageBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from scripts.trees.binary_tree import BinaryTree, TreeNode

class TreesView(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        self.setLayout(layout)

        # Crear figura de matplotlib
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        # Crear botones
        button_layout = QHBoxLayout()
        self.add_button = QPushButton('Agregar Nodo', self)
        self.add_button.clicked.connect(self.add_node)
        button_layout.addWidget(self.add_button)

        self.delete_button = QPushButton('Eliminar Nodo', self)
        self.delete_button.clicked.connect(self.delete_node)
        button_layout.addWidget(self.delete_button)

        self.clear_button = QPushButton('Limpiar Árbol', self)
        self.clear_button.clicked.connect(self.clear_tree)
        button_layout.addWidget(self.clear_button)

        self.show_traversals_button = QPushButton('Mostrar Recorridos', self)
        self.show_traversals_button.clicked.connect(self.show_traversals)
        button_layout.addWidget(self.show_traversals_button)

        self.show_height_button = QPushButton('Mostrar Altura', self)
        self.show_height_button.clicked.connect(self.show_height)
        button_layout.addWidget(self.show_height_button)

        layout.addLayout(button_layout)

        # Crear etiquetas para mostrar información
        self.info_label = QLabel("")
        layout.addWidget(self.info_label)

        # Crear el árbol binario vacío
        self.tree = BinaryTree()

        self.ax = self.figure.add_subplot(111)
        self.canvas.draw()

    def add_node(self):
        value, ok = QInputDialog.getInt(self, "Valor del Nodo", "Ingrese el valor del nuevo nodo:")
        if not ok:
            return

        if value == 0 or value in self.tree.values:
            self.show_error("Error: Valor inválido o ya existente")
            return

        if self.tree.root is None:
            self.tree.root = TreeNode(value)
            self.tree.values.add(value)
        else:
            parent_value, ok = QInputDialog.getInt(self, "Valor del Nodo Padre", "Ingrese el valor del nodo padre:")
            if not ok:
                return
            parent_node = self.find_node(self.tree.root, parent_value)
            if parent_node is None:
                self.show_error(f"No se encontró el nodo con valor {parent_value}")
                return
            side, ok = QInputDialog.getItem(self, "Lado del Nodo", "Seleccione el lado:", ["left", "right"], 0, False)
            if not ok:
                return
            self.tree.insert(parent_node, side, value, self)

        self.redraw_tree()

    def delete_node(self):
        value, ok = QInputDialog.getInt(self, "Eliminar Nodo", "Ingrese el valor del nodo a eliminar:")
        if ok:
            # TODO Verificar que recorra el arbol correctamente para encontrar el nodo y si no lo encuentra, mostrar un mensaje de error 
            if value not in self.tree.values: 
                self.show_error(f"Error: El nodo con valor {value} no existe")
                return
            self.tree.delete_node(value, self)
            self.redraw_tree()

    def clear_tree(self):
        self.tree.clear()
        self.redraw_tree()

    def show_traversals(self):
        pre_order = []
        self.tree.pre_order(self.tree.root, pre_order)
        in_order = []
        self.tree.in_order(self.tree.root, in_order)
        post_order = []
        self.tree.post_order(self.tree.root, post_order)
        self.info_label.setText(f"Pre-Order: {pre_order}\nIn-Order: {in_order}\nPost-Order: {post_order}")

    def show_height(self):
        height = self.tree.height(self.tree.root)
        self.info_label.setText(f"Altura del árbol: {height}")

    def redraw_tree(self):
        self.ax.clear()
        self.tree.draw_tree(self.ax, self.tree.root)
        self.canvas.draw()

    def find_node(self, node, value):
        if node is None:
            return None
        if node.data == value:
            return node
        left_result = self.find_node(node.left, value)
        if left_result is not None:
            return left_result
        return self.find_node(node.right, value)

    def show_error(self, message):
        error_dialog = QMessageBox()
        error_dialog.setIcon(QMessageBox.Icon.Critical)
        error_dialog.setText(message)
        error_dialog.setWindowTitle("Error")
        error_dialog.exec()
