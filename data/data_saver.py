from PyQt6.QtWidgets import QFileDialog

# TODO Falta verificar
def save_sorted_data(data):
    file_name, _ = QFileDialog.getSaveFileName(None, 'Guardar Archivo', '', 'Archivos de Texto (*.txt)')
    if file_name:
        with open(file_name, 'w') as file:
            file.write(data)
