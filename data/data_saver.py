from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtGui import QPixmap

def save_sorted_data(data):
    file_name, _ = QFileDialog.getSaveFileName(None, 'Guardar Archivo', '', 'Archivos de Texto (*.txt)')
    if file_name:
        with open(file_name, 'w') as file:
            file.write(data)

def save_screenshot(window):
    file_name, _ = QFileDialog.getSaveFileName(None, 'Guardar Captura de Pantalla', '', 'Imágenes (*.png *.jpg *.bmp)')
    if file_name:
        pixmap = QPixmap(window.size())
        window.render(pixmap)
        pixmap.save(file_name)
