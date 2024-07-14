from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtGui import QPixmap

def save_screenshot(window):
    file_name, _ = QFileDialog.getSaveFileName(None, 'Guardar Captura de Pantalla', '', 'Imágenes (*.png *.jpg *.bmp)')
    if file_name:
        pixmap = QPixmap(window.size())
        window.render(pixmap)
        pixmap.save(file_name)
