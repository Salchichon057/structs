import networkx as nx
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QLineEdit, QMessageBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from scripts.queue_stacks.stack import Stack
from scripts.queue_stacks.queue import Queue
from ui.components import create_button  # Importa la función create_button

class Visualizer:
    def __init__(self, canvas):
        self.canvas = canvas
        self.ax = self.canvas.figure.add_subplot(111)
        self.ax.axis('off')

    def draw_stack(self, stack):
        self.ax.clear()
        G = nx.DiGraph()
        for i, value in enumerate(reversed(stack.stack)):
            G.add_node(i, label=value)
            if i > 0:
                G.add_edge(i, i-1)

        pos = {i: (0, i) for i in range(len(stack.stack))}
        labels = nx.get_node_attributes(G, 'label')
        color_map = ['lightgreen'] * (len(stack.stack) - 1) + ['lightcoral']
        nx.draw(G, pos, labels=labels, with_labels=True, node_size=2000, node_color=color_map, font_size=14, font_weight='bold', ax=self.ax, arrows=False)
        self.ax.set_title("Pila")
        self.canvas.draw()

    def draw_queue(self, queue):
        self.ax.clear()
        G = nx.DiGraph()
        for i, value in enumerate(queue.queue):
            G.add_node(i, label=value)
            if i > 0:
                G.add_edge(i-1, i)

        pos = {i: (0, -i) for i in range(len(queue.queue))}
        labels = nx.get_node_attributes(G, 'label')
        color_map = ['lightblue'] * (len(queue.queue) - 1) + ['lightcoral']
        nx.draw(G, pos, labels=labels, with_labels=True, node_size=2000, node_color=color_map, font_size=14, font_weight='bold', ax=self.ax, arrows=True)
        self.ax.set_title("Cola")
        self.canvas.draw()

class QueueStacksView(QWidget):
    def __init__(self):
        super().__init__()

        self.stack = Stack()
        self.queue = Queue()

        layout = QVBoxLayout(self)

        self.data_type_combo = QComboBox()
        self.data_type_combo.addItems(['Seleccionar Estructura', 'Pila', 'Cola'])
        self.data_type_combo.currentIndexChanged.connect(self.update_view)
        layout.addWidget(self.data_type_combo)

        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText('Ingrese un valor')
        self.input_field.setStyleSheet("""
            QLineEdit {
                background-color: #fff;
                padding: 10px;
                font-size: 16px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
        """)
        layout.addWidget(self.input_field)

        button_layout = QHBoxLayout()
        self.push_button = create_button('Agregar', self.add_value)
        button_layout.addWidget(self.push_button)

        self.pop_button = create_button('Eliminar', self.remove_value)
        button_layout.addWidget(self.pop_button)

        layout.addLayout(button_layout)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        self.visualizer = Visualizer(self.canvas)

    def update_view(self):
        self.stack = Stack()
        self.queue = Queue()
        self.canvas.figure.clear()
        self.visualizer.ax = self.canvas.figure.add_subplot(111)
        self.visualizer.ax.axis('off')
        self.canvas.draw()

        if self.data_type_combo.currentText() == 'Pila':
            self.push_button.setText('Push')
            self.pop_button.setText('Pop')
            self.visualizer.ax.set_title("Pila")
        elif self.data_type_combo.currentText() == 'Cola':
            self.push_button.setText('Encolar')
            self.pop_button.setText('Desencolar')
            self.visualizer.ax.set_title("Cola")

    def add_value(self):
        value = self.input_field.text()
        if not value:
            self.show_error('Ingrese un valor para agregar')
            return

        try:
            if self.data_type_combo.currentText() == 'Pila':
                self.stack.push(value)
                self.visualizer.draw_stack(self.stack)
            elif self.data_type_combo.currentText() == 'Cola':
                self.queue.enqueue(value)
                self.visualizer.draw_queue(self.queue)
            else:
                self.show_error('Seleccione una estructura de datos')
        except ValueError as e:
            self.show_error(str(e))

    def remove_value(self):
        try:
            if self.data_type_combo.currentText() == 'Pila':
                self.stack.pop()
                self.visualizer.draw_stack(self.stack)
            elif self.data_type_combo.currentText() == 'Cola':
                self.queue.dequeue()
                self.visualizer.draw_queue(self.queue)
        except ValueError as e:
            self.show_error(str(e))

    def show_error(self, message):
        error_dialog = QMessageBox()
        error_dialog.setIcon(QMessageBox.Icon.Critical)
        error_dialog.setText(message)
        error_dialog.setWindowTitle("Error")
        error_dialog.exec()
