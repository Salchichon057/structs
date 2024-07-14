import random
import string
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QLabel, QComboBox, QSizePolicy, QMessageBox
from ui.components import create_button
from data.data_loader import load_data
from data.data_saver import save_sorted_data  # Asegúrate de importar save_sorted_data
from scripts.sortings.sorting_algorithms_numeric import (
    bubble_sort,
    insertion_sort,
    selection_sort,
    merge_sort,
    heap_sort,
    counting_sort,
    radix_sort,
    quick_sort_wrapper
)
from scripts.sortings.sorting_algorithms_str import (
    bubble_sort_str,
    insertion_sort_str,
    selection_sort_str,
    merge_sort_str,
    heap_sort_str,
    counting_sort_str,
    radix_sort_str,
    quick_sort_wrapper_str
)

class ArrangementsView(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        # Botones "Datos Aleatorios" y "Ordenar"
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

        # Añadir botón para descargar datos
        self.download_button = create_button('Descargar Datos', self.download_data)
        self.download_button.setVisible(False)
        buttons_layout.addWidget(self.download_button)

        layout.addLayout(buttons_layout)

        # ComboBox para seleccionar el tipo de datos aleatorios
        self.random_data_type_combo = QComboBox()
        self.random_data_type_combo.addItems([
            'Seleccionar Tipo de Datos Aleatorios',
            'Numérico',
            'Alfabético',
            'Mezclado'
        ])
        self.random_data_type_combo.currentIndexChanged.connect(self.update_random_data_type)
        self.random_data_type_combo.setVisible(False)
        layout.addWidget(self.random_data_type_combo)

        # ComboBox para seleccionar la forma de generar datos numéricos
        self.numeric_data_type_combo = QComboBox()
        self.numeric_data_type_combo.addItems([
            'Seleccionar Forma de Generar',
            'Default',
            'Primos',
            'Primos Únicos'
        ])
        self.numeric_data_type_combo.setVisible(False)
        layout.addWidget(self.numeric_data_type_combo)

        # Botón para generar datos aleatorios
        self.generate_button = create_button('Generar Datos', self.generate_random_data)
        self.generate_button.setVisible(False)
        layout.addWidget(self.generate_button)

        # Input para datos
        self.input_button = create_button('Seleccionar Archivo', self.load_data)
        self.input_button.setVisible(False)
        layout.addWidget(self.input_button)

        # Campo de texto para ingresar datos manualmente
        self.manual_input = QTextEdit()
        self.manual_input.setVisible(False)
        self.manual_input.setMinimumHeight(30)
        layout.addWidget(self.manual_input)

        # Output de datos
        self.unsorted_data_label = QLabel('Datos Desordenados')
        self.unsorted_data_label.setVisible(False)
        layout.addWidget(self.unsorted_data_label)
        
        self.unsorted_data = QTextEdit()
        self.unsorted_data.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding))
        self.unsorted_data.setVisible(False)
        self.unsorted_data.setMinimumHeight(150)
        layout.addWidget(self.unsorted_data)

        self.sorted_data_label = QLabel('Datos Ordenados')
        self.sorted_data_label.setVisible(False)
        layout.addWidget(self.sorted_data_label)
        
        self.sorted_data = QTextEdit()
        self.sorted_data.setReadOnly(True)
        self.sorted_data.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding))
        self.sorted_data.setVisible(False)
        self.sorted_data.setMinimumHeight(150)
        layout.addWidget(self.sorted_data)

        self.sort_type_label = QLabel('Ordenado como:')
        self.sort_type_label.setVisible(False)
        layout.addWidget(self.sort_type_label)

        # ComboBox de selección de algoritmos en el área dinámica
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
            self.random_data_type_combo.setVisible(False)
            self.numeric_data_type_combo.setVisible(False)
            self.generate_button.setVisible(False)
            self.unsorted_data_label.setVisible(True)
            self.unsorted_data.setVisible(True)
            self.unsorted_data.setReadOnly(True)
        elif input_type == 'Datos Aleatorios':
            self.input_button.setVisible(False)
            self.manual_input.setVisible(False)
            self.random_data_type_combo.setVisible(True)
            self.generate_button.setVisible(True)
            self.unsorted_data_label.setVisible(True)
            self.unsorted_data.setVisible(True)
        elif input_type == 'Ingresar Datos Manualmente':
            self.input_button.setVisible(False)
            self.manual_input.setVisible(True)
            self.random_data_type_combo.setVisible(False)
            self.numeric_data_type_combo.setVisible(False)
            self.generate_button.setVisible(False)
            self.unsorted_data.setReadOnly(False)
            self.unsorted_data_label.setVisible(False)
            self.unsorted_data.setVisible(False)
        else:
            self.input_button.setVisible(False)
            self.manual_input.setVisible(False)
            self.random_data_type_combo.setVisible(False)
            self.numeric_data_type_combo.setVisible(False)
            self.generate_button.setVisible(False)
            self.unsorted_data_label.setVisible(False)
            self.unsorted_data.setVisible(False)
            self.sorted_data_label.setVisible(False)
            self.sorted_data.setVisible(False)
        
        self.sort_combo.setVisible(True)
        self.sort_button.setVisible(True)
        self.download_button.setVisible(True)

    def update_random_data_type(self):
        if self.random_data_type_combo.currentText() == 'Numérico':
            self.numeric_data_type_combo.setVisible(True)
        else:
            self.numeric_data_type_combo.setVisible(False)


    def clear_fields(self):
        self.unsorted_data.setText('')
        self.sorted_data.setText('')
        self.unsorted_data_label.setVisible(False)
        self.sorted_data_label.setVisible(False)
        self.unsorted_data.setVisible(False)
        self.sorted_data.setVisible(False)

    def generate_random_data(self):
        data_type = self.random_data_type_combo.currentText()
        numeric_data_type = self.numeric_data_type_combo.currentText()
        
        if data_type == 'Numérico':
            if numeric_data_type == 'Primos':
                random_data = ', '.join(str(self.generate_prime()) for _ in range(20))
            elif numeric_data_type == 'Primos Únicos':
                random_data = ', '.join(str(prime) for prime in self.generate_unique_primes(20))
            else:
                random_data = ', '.join(str(random.randint(1, 100)) for _ in range(20))
        elif data_type == 'Alfabético':
            random_data = ', '.join(random.choice(string.ascii_letters) for _ in range(20))
        elif data_type == 'Mezclado':
            random_data = ', '.join(
                random.choice([str(random.randint(1, 100)), random.choice(string.ascii_letters)])
                for _ in range(20)
            )
        else:
            self.show_error('Seleccione un tipo válido de datos aleatorios')
            return
        
        self.unsorted_data.setText(random_data)
        self.unsorted_data.setReadOnly(True)
        self.unsorted_data.setVisible(True)
        self.unsorted_data_label.setVisible(True)

    def generate_prime(self):
        while True:
            num = random.randint(2, 100)
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                return num

    def generate_unique_primes(self, n):
        primes = []
        num = 2
        while len(primes) < n:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
            num += 1
        random.shuffle(primes)
        return primes

    def load_data(self):
        data = load_data()
        if data:
            self.unsorted_data.setText(', '.join(map(str, data)))
            self.unsorted_data.setVisible(True)
            self.unsorted_data_label.setVisible(True)

    def validate_data(self, data_text):
        if not data_text:
            self.show_error('No se encontraron datos para ordenar')
            return None, None
        
        data = [item.strip() for item in data_text.split(',') if item.strip()]
        contains_str = any(not item.isdigit() for item in data)
        
        data = [int(item) if item.isdigit() else item for item in data]
        data_type = str if contains_str else int

        return data, data_type

    def sort_data(self):
        if self.input_type_combo.currentText() == 'Ingresar Datos Manualmente':
            data_text = self.manual_input.toPlainText().strip()
        else:
            data_text = self.unsorted_data.toPlainText().strip()
        
        data, data_type = self.validate_data(data_text)
        
        if data is None:
            return
        
        if data_type == int:
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
            self.sort_type_label.setText('Ordenado como: Numérico')
        else:
            if self.sort_combo.currentText() == 'Bubble Sort':
                sorted_data = bubble_sort_str(data)
            elif self.sort_combo.currentText() == 'Insertion Sort':
                sorted_data = insertion_sort_str(data)
            elif self.sort_combo.currentText() == 'Selection Sort':
                sorted_data = selection_sort_str(data)
            elif self.sort_combo.currentText() == 'Merge Sort':
                sorted_data = merge_sort_str(data)
            elif self.sort_combo.currentText() == 'Heap Sort':
                sorted_data = heap_sort_str(data)
            elif self.sort_combo.currentText() == 'Counting Sort':
                sorted_data = counting_sort_str(data)
            elif self.sort_combo.currentText() == 'Radix Sort':
                sorted_data = radix_sort_str(data)
            elif self.sort_combo.currentText() == 'Quick Sort':
                sorted_data = quick_sort_wrapper_str(data)
            self.sort_type_label.setText('Ordenado como: Alfabético')
        
        self.sorted_data.setText(', '.join(map(str, sorted_data)))
        self.sorted_data.setVisible(True)
        self.sorted_data_label.setVisible(True)
        self.sort_type_label.setVisible(True)

    def download_data(self):
        if not self.sorted_data.toPlainText().strip():
            self.show_error('No hay datos ordenados para guardar')
            return
        save_sorted_data(self.sorted_data.toPlainText())

    def show_error(self, message):
        error_dialog = QMessageBox()
        error_dialog.setIcon(QMessageBox.Icon.Critical)
        error_dialog.setText(message)
        error_dialog.setWindowTitle("Error")
        error_dialog.exec()
