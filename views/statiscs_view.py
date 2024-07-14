import numpy as np
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit, QComboBox, QMessageBox, QSpacerItem, QSizePolicy
from data.data_loader import load_data
from scripts.statics.statistics_algorithms import calculate_statistics
from data.data_saver import save_statistics_data
from ui.components import create_button

class StatisticsView(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Estadísticas Descriptivas")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout(self)

        self.input_combo = QComboBox()
        self.input_combo.addItems(["Seleccionar Fuente de Datos", "Ingresar Datos Manualmente", "Datos Aleatorios", "Cargar Archivo"])
        self.input_combo.currentIndexChanged.connect(self.update_input_area)
        layout.addWidget(self.input_combo)

        self.load_button = create_button("Cargar Datos", self.load_data_from_file)
        self.load_button.setVisible(False)
        layout.addWidget(self.load_button)

        self.calculate_button = create_button("Calcular Estadísticas", self.calculate_statistics)
        layout.addWidget(self.calculate_button)

        self.download_button = create_button("Descargar Datos", self.download_data)
        layout.addWidget(self.download_button)

        self.input_area = QTextEdit()
        self.input_area.setPlaceholderText("Ingrese los datos separados por comas")
        self.input_area.setVisible(False)
        layout.addWidget(self.input_area)
        
        self.result_area = QTextEdit()
        self.result_area.setReadOnly(True)
        layout.addWidget(self.result_area)

        layout.addItem(QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        self.setLayout(layout)

    def update_input_area(self):
        self.input_area.clear()
        self.result_area.clear()
        
        selected_option = self.input_combo.currentText()
        if selected_option == "Ingresar Datos Manualmente":
            self.input_area.setVisible(True)
            self.load_button.setVisible(False)
        elif selected_option == "Datos Aleatorios":
            self.input_area.setVisible(True)
            self.load_button.setVisible(False)
            self.generate_random_data()
        elif selected_option == "Cargar Archivo":
            self.input_area.setVisible(False)
            self.load_button.setVisible(True)
        else:
            self.input_area.setVisible(False)
            self.load_button.setVisible(False)

    def generate_random_data(self):
        random_data = np.random.randint(1, 100, size=20).tolist()
        self.input_area.setText(', '.join(map(str, random_data)))

    def load_data_from_file(self):
        data = load_data()
        if data is not None:
            self.input_area.setText(', '.join(map(str, data)))
            self.input_area.setVisible(True)
        else:
            self.show_error("Error al cargar los datos")

    def calculate_statistics(self):
        data_text = self.input_area.toPlainText()
        if not data_text:
            self.show_error("Ingrese o cargue datos para calcular las estadísticas")
            return

        try:
            data = list(map(float, data_text.split(',')))
        except ValueError:
            self.show_error("Asegúrese de que todos los datos sean números válidos")
            return

        self.stats = calculate_statistics(data)
        self.display_statistics(self.stats)

    def display_statistics(self, stats):
        result_text = (
            f"Media: {stats['mean']:.2f}\n"
            f"Mediana: {stats['median']:.2f}\n"
            f"Moda: {stats['mode']}\n"
            f"Rango: {stats['range']:.2f}\n"
            f"Varianza: {stats['variance']:.4f}\n"
            f"Desviación Estándar: {stats['std_deviation']:.4f}\n"
            f"Coeficiente de Variación: {stats['coefficient_variation']:.2f}%"
        )
        self.result_area.setText(result_text)

    def download_data(self):
        if not self.input_area.toPlainText():
            self.show_error("No hay datos para descargar")
            return
        save_statistics_data(self.input_area.toPlainText(), self.stats)

    def show_error(self, message):
        error_dialog = QMessageBox()
        error_dialog.setIcon(QMessageBox.Icon.Critical)
        error_dialog.setText(message)
        error_dialog.setWindowTitle("Error")
        error_dialog.exec()