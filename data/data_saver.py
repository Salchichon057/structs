from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtGui import QPixmap
import pandas as pd

def save_sorted_data(data):
    file_name, _ = QFileDialog.getSaveFileName(None, 'Guardar Archivo', '', 'Archivos de Excel (*.xlsx)')
    if file_name:
        data_list = [item.strip() for item in data.split(',') if item.strip()]
        df = pd.DataFrame(data_list, columns=['Números'])
        df.to_excel(file_name, index=False)

def save_screenshot(window):
    file_name, _ = QFileDialog.getSaveFileName(None, 'Guardar Captura de Pantalla', '', 'Imágenes (*.png *.jpg *.bmp)')
    if file_name:
        pixmap = QPixmap(window.size())
        window.render(pixmap)
        pixmap.save(file_name)
