from PyQt6.QtWidgets import QFileDialog
from data.data_converter import convert_xlsx_to_list, convert_txt_to_list

def load_data():
    file_name, _ = QFileDialog.getOpenFileName(None, 'Seleccionar Archivo', '', 'Archivos Excel (*.xlsx);;Archivos de Texto (*.txt)')
    if file_name:
        if file_name.endswith('.xlsx'):
            return convert_xlsx_to_list(file_name)
        elif file_name.endswith('.txt'):
            return convert_txt_to_list(file_name)
    return None
