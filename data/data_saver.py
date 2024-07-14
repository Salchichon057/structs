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

def save_statistics_data(data, stats):
    file_name, _ = QFileDialog.getSaveFileName(None, 'Guardar Archivo', '', 'Archivos de Excel (*.xlsx)')
    if file_name:
        data_list = [item.strip() for item in data.split(',') if item.strip()]
        stats_list = [
            ["Datos", ', '.join(data_list)],
            ["Media", stats['mean']],
            ["Mediana", stats['median']],
            ["Moda", stats['mode']],
            ["Rango", stats['range']],
            ["Varianza", stats['variance']],
            ["Desviación Estándar", stats['std_deviation']],
            ["Coeficiente de Variación", stats['coefficient_variation']]
        ]
        
        df_stats = pd.DataFrame(stats_list, columns=["Descripción", "Valor"])
        df_stats.to_excel(file_name, index=False, sheet_name='Estadísticas')