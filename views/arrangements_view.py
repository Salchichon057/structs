from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QLabel, QComboBox, QSizePolicy
from ui.components import create_button
from data.data_loader import load_data
from data.data_saver import save_sorted_data
from scripts.sortings.sorting_algorithms import (
    bubble_sort,
    insertion_sort,
    selection_sort,
    merge_sort,
    heap_sort,
    counting_sort,
    radix_sort,
    quick_sort_wrapper
)

class ArrangementsView(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        # ? Botones "Datos Aleatorios" y "Ordenar"
        buttons_layout = QHBoxLayout()
        self.input_type_combo = QComboBox()
        self.input_type_combo.addItems([
            'Seleccionar Tipo de Input',
            'Cargar Datos',
            'Datos Aleatorios',
            'Ingresar Datos Manualmente'
        ])
        self.input_type_combo.currentIndexChanged.connect(self.update_input_area)
        buttons_layout.addWidget(self.input_type_combo)

        self.sort_button = create_button('Ordenar', self.sort_data)
        self.sort_button.setVisible(False)
        buttons_layout.addWidget(self.sort_button)

        layout.addLayout(buttons_layout)

        # ? Input para datos
        self.input_button = create_button('Seleccionar Archivo', self.load_data)
        self.input_button.setVisible(False)
        layout.addWidget(self.input_button)

        # ? Campo de texto para ingresar datos manualmente
        self.manual_input = QTextEdit()
        self.manual_input.setVisible(False)
        self.manual_input.setMinimumHeight(30)
        layout.addWidget(self.manual_input)

        # ? Output de datos
        self.unsorted_data_label = QLabel('Números Desordenados')
        self.unsorted_data_label.setVisible(False)
        layout.addWidget(self.unsorted_data_label)
        
        self.unsorted_data = QTextEdit()
        self.unsorted_data.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding))
        self.unsorted_data.setVisible(False)
        self.unsorted_data.setMinimumHeight(150)
        layout.addWidget(self.unsorted_data)

        self.sorted_data_label = QLabel('Números Ordenados')
        self.sorted_data_label.setVisible(False)
        layout.addWidget(self.sorted_data_label)
        
        self.sorted_data = QTextEdit()
        self.sorted_data.setReadOnly(True)
        self.sorted_data.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding))
        self.sorted_data.setVisible(False)
        self.sorted_data.setMinimumHeight(150)
        layout.addWidget(self.sorted_data)

        # ? ComboBox de selección de algoritmos en el área dinámica
        self.sort_combo = QComboBox()
        self.sort_combo.addItems([
            'Bubble Sort',
            'Insertion Sort',
            'Selection Sort',
            'Merge Sort',
            'Heap Sort',
            'Counting Sort',
            'Radix Sort',
            'Quick Sort'
        ])
        self.sort_combo.setVisible(False)
        layout.addWidget(self.sort_combo)

        self.setLayout(layout)

    def update_input_area(self):
        self.clear_fields()
        
        input_type = self.input_type_combo.currentText()

        if input_type == 'Cargar Datos':
            self.input_button.setVisible(True)
            self.manual_input.setVisible(False)
            self.unsorted_data_label.setVisible(True)
            self.unsorted_data.setVisible(True)
            self.unsorted_data.setReadOnly(True)
        elif input_type == 'Datos Aleatorios':
            self.input_button.setVisible(False)
            self.manual_input.setVisible(False)
            self.unsorted_data_label.setVisible(True)
            self.unsorted_data.setVisible(True)
            self.generate_random_data()
        elif input_type == 'Ingresar Datos Manualmente':
            self.input_button.setVisible(False)
            self.manual_input.setVisible(True)
            self.unsorted_data.setReadOnly(False)
            self.unsorted_data_label.setVisible(False)
            self.unsorted_data.setVisible(False)
        else:
            self.input_button.setVisible(False)
            self.manual_input.setVisible(False)
            self.unsorted_data_label.setVisible(False)
            self.unsorted_data.setVisible(False)
            self.sorted_data_label.setVisible(False)
            self.sorted_data.setVisible(False)
        
        self.sort_combo.setVisible(True)
        self.sort_button.setVisible(True)

    def clear_fields(self):
        self.unsorted_data.setText('')
        self.sorted_data.setText('')
        self.unsorted_data_label.setVisible(False)
        self.sorted_data_label.setVisible(False)
        self.unsorted_data.setVisible(False)
        self.sorted_data.setVisible(False)

    def generate_random_data(self):
        import random
        random_data = ', '.join(map(str, [random.randint(0, 100) for _ in range(10)]))
        self.unsorted_data.setText(random_data)
        self.unsorted_data.setReadOnly(True)
        self.unsorted_data.setVisible(True)
        self.unsorted_data_label.setVisible(True)

    def load_data(self):
        data = load_data()
        if data:
            self.unsorted_data.setText(', '.join(map(str, data)))
            self.unsorted_data.setVisible(True)
            self.unsorted_data_label.setVisible(True)

    def sort_data(self):
        if self.input_type_combo.currentText() == 'Ingresar Datos Manualmente':
            data_text = self.manual_input.toPlainText().strip()
        else:
            data_text = self.unsorted_data.toPlainText().strip()
        
        # ? Validar y limpiar la entrada de datos
        if not data_text:
            self.sorted_data.setText('No se encontraron datos para ordenar')
            self.sorted_data.setVisible(True)
            self.sorted_data_label.setVisible(True)
            return
        
        try:
            data = list(map(int, [item.strip() for item in data_text.split(',') if item.strip()]))
        except ValueError:
            self.sorted_data.setText('Los datos ingresados no son válidos')
            self.sorted_data.setVisible(True)
            self.sorted_data_label.setVisible(True)
            return
        
        if self.sort_combo.currentText() == 'Bubble Sort':
            sorted_data = bubble_sort(data)
        elif self.sort_combo.currentText() == 'Insertion Sort':
            sorted_data = insertion_sort(data)
        elif self.sort_combo.currentText() == 'Selection Sort':
            sorted_data = selection_sort(data)
        elif self.sort_combo.currentText() == 'Merge Sort':
            sorted_data = merge_sort(data)
        elif self.sort_combo.currentText() == 'Heap Sort':
            sorted_data = heap_sort(data)
        elif self.sort_combo.currentText() == 'Counting Sort':
            sorted_data = counting_sort(data)
        elif self.sort_combo.currentText() == 'Radix Sort':
            sorted_data = radix_sort(data)
        elif self.sort_combo.currentText() == 'Quick Sort':
            sorted_data = quick_sort_wrapper(data)
        
        self.sorted_data.setText(', '.join(map(str, sorted_data)))
        self.sorted_data.setVisible(True)
        self.sorted_data_label.setVisible(True)

    def download_data(self):
        save_sorted_data(self.sorted_data.toPlainText())
