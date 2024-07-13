from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QTextEdit, QPushButton, QSizePolicy, QMessageBox, QSpacerItem, QSizePolicy
from scripts.search.search_algorithms import binary_search_all, linear_search_all, is_sorted, bubble_sort
from ui.components import create_button
import random

class SearchsView(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        # ComboBox para seleccionar el tipo de datos
        self.data_type_combo = QComboBox()
        self.data_type_combo.addItems(['Seleccionar Tipo de Datos', 'Generar Datos Aleatorios', 'Ingresar Datos Manualmente'])
        self.data_type_combo.currentIndexChanged.connect(self.update_input_area)
        layout.addWidget(self.data_type_combo)

        # ComboBox para seleccionar el tipo de búsqueda
        self.search_type_combo = QComboBox()
        self.search_type_combo.addItems(['Seleccionar Tipo de Búsqueda', 'Búsqueda Binaria', 'Búsqueda Lineal'])
        self.search_type_combo.setVisible(False)
        layout.addWidget(self.search_type_combo)

        # Botón para realizar la búsqueda
        self.search_button = create_button('Buscar', self.search_data)
        self.search_button.setVisible(False)
        layout.addWidget(self.search_button)

        # Input para datos
        self.input_button = create_button('Generar Datos', self.generate_random_data)
        self.input_button.setVisible(False)
        layout.addWidget(self.input_button)

        # Campo de texto para ingresar datos manualmente
        self.manual_input = QTextEdit()
        self.manual_input.setPlaceholderText('Ingrese los datos, separados por comas')
        self.manual_input.setVisible(False)
        self.manual_input.setStyleSheet("QTextEdit { min-height: 30px; max-height: 30px; }")
        layout.addWidget(self.manual_input)

        # Campo de texto para ingresar el dato a buscar
        self.search_input = QTextEdit()
        self.search_input.setPlaceholderText('Ingrese el dato a buscar')
        self.search_input.setVisible(False)
        self.search_input.setStyleSheet("QTextEdit { min-height: 30px; max-height: 30px; }")
        layout.addWidget(self.search_input)

        # Output de datos
        self.unsorted_data_label = QLabel('Datos Desordenados')
        self.unsorted_data_label.setVisible(False)
        layout.addWidget(self.unsorted_data_label)
        
        self.unsorted_data = QTextEdit()
        self.unsorted_data.setReadOnly(True)
        self.unsorted_data.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding))
        self.unsorted_data.setVisible(False)
        self.unsorted_data.setStyleSheet("QTextEdit { min-height: 70px; max-height: 70px; }")
        layout.addWidget(self.unsorted_data)

        self.sorted_data_label = QLabel('Datos Ordenados')
        self.sorted_data_label.setVisible(False)
        layout.addWidget(self.sorted_data_label)
        
        self.sorted_data = QTextEdit()
        self.sorted_data.setReadOnly(True)
        self.sorted_data.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding))
        self.sorted_data.setVisible(False)
        self.sorted_data.setStyleSheet("QTextEdit { min-height: 70px; max-height: 70px; }")
        layout.addWidget(self.sorted_data)

        self.search_result_label = QLabel('Resultado de la Búsqueda')
        self.search_result_label.setVisible(False)
        layout.addWidget(self.search_result_label)
        
        self.search_result = QTextEdit()
        self.search_result.setReadOnly(True)
        self.search_result.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding))
        self.search_result.setVisible(False)
        self.search_result.setStyleSheet("QTextEdit { min-height: 70px; max-height: 70px; }")
        layout.addWidget(self.search_result)

        # Agregar espaciador
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        self.setLayout(layout)

    def update_input_area(self):
        self.clear_fields()
        
        data_type = self.data_type_combo.currentText()

        if data_type == 'Generar Datos Aleatorios':
            self.input_button.setVisible(True)
            self.manual_input.setVisible(False)
            self.search_input.setVisible(True)
            self.search_button.setVisible(True)
            self.search_type_combo.setVisible(True)
            self.unsorted_data_label.setVisible(False)
            self.unsorted_data.setVisible(False)
        elif data_type == 'Ingresar Datos Manualmente':
            self.input_button.setVisible(False)
            self.manual_input.setVisible(True)
            self.search_input.setVisible(True)
            self.search_button.setVisible(True)
            self.search_type_combo.setVisible(True)
            self.unsorted_data_label.setVisible(False)
            self.unsorted_data.setVisible(False)
        else:
            self.input_button.setVisible(False)
            self.manual_input.setVisible(False)
            self.search_input.setVisible(False)
            self.search_button.setVisible(False)
            self.search_type_combo.setVisible(False)
            self.unsorted_data_label.setVisible(False)
            self.unsorted_data.setVisible(False)
            self.sorted_data_label.setVisible(False)
            self.sorted_data.setVisible(False)
            self.search_result_label.setVisible(False)
            self.search_result.setVisible(False)

    def clear_fields(self):
        self.unsorted_data.setText('')
        self.sorted_data.setText('')
        self.search_result.setText('')
        self.unsorted_data_label.setVisible(False)
        self.sorted_data_label.setVisible(False)
        self.search_result_label.setVisible(False)
        self.unsorted_data.setVisible(False)
        self.sorted_data.setVisible(False)
        self.search_result.setVisible(False)

    def generate_random_data(self):
        random_data = [random.randint(0, 100) for _ in range(20)]
        self.unsorted_data.setText(', '.join(map(str, random_data)))
        self.unsorted_data_label.setVisible(True)
        self.unsorted_data.setVisible(True)

    def search_data(self):
        if self.search_type_combo.currentText() == 'Seleccionar Tipo de Búsqueda':
            self.show_error('Seleccione un tipo de búsqueda')
            return

        data_text = self.manual_input.toPlainText().strip() if self.data_type_combo.currentText() == 'Ingresar Datos Manualmente' else self.unsorted_data.toPlainText().strip()
        if not data_text:
            self.show_error('No se encontraron datos para buscar')
            return

        data = [item.strip() for item in data_text.split(',') if item.strip()]
        data = [int(item) if item.isdigit() else item for item in data]

        if not data:
            self.show_error('No se encontraron datos válidos para buscar')
            return

        search_value = self.search_input.toPlainText().strip()
        if not search_value:
            self.show_error('Ingrese un valor para buscar')
            return

        if search_value.isdigit():
            search_value = int(search_value)

        search_type = self.search_type_combo.currentText()

        result_indices = []
        if search_type == 'Búsqueda Binaria':
            if not all(isinstance(item, int) for item in data):
                self.show_error('La búsqueda binaria solo funciona con datos numéricos')
                return
            if not is_sorted(data):
                self.unsorted_data.setText(', '.join(map(str, data)))
                self.unsorted_data_label.setVisible(True)
                self.unsorted_data.setVisible(True)
                self.unsorted_data.setReadOnly(True)
                data = bubble_sort(data)
            self.sorted_data.setText(', '.join(map(str, data)))
            self.sorted_data_label.setVisible(True)
            self.sorted_data.setVisible(True)
            result_indices = binary_search_all(data, search_value)
        elif search_type == 'Búsqueda Lineal':
            if self.data_type_combo.currentText() != 'Ingresar Datos Manualmente':
                self.unsorted_data.setText(', '.join(map(str, data)))
                self.unsorted_data_label.setVisible(True)
                self.unsorted_data.setVisible(True)
                self.unsorted_data.setReadOnly(True)
            result_indices = linear_search_all(data, search_value)
        
        if result_indices:
            if len(result_indices) == 1:
                self.search_result.setText(f'El valor {search_value} se encuentra en la posición: {result_indices[0]}')
            else:
                positions = ', '.join(map(str, result_indices))
                self.search_result.setText(f'El valor {search_value} se encuentra en las posiciones: {positions}')
        else:
            self.search_result.setText(f'El valor {search_value} no se encuentra en la lista')
        self.search_result_label.setVisible(True)
        self.search_result.setVisible(True)

    def show_error(self, message):
        error_dialog = QMessageBox()
        error_dialog.setIcon(QMessageBox.Icon.Critical)
        error_dialog.setText(message)
        error_dialog.setWindowTitle("Error")
        error_dialog.exec()
