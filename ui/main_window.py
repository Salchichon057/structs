import sys
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGroupBox, QApplication, QSpacerItem, QSizePolicy
from PyQt6.QtGui import QIcon
from ui.styles import styles
from ui.components import create_button
from views.arrangements_view import ArrangementsView
from views.queue_stacks_view import QueueStacksView
from views.trees_view import TreesView
from views.searchs_view import SearchsView

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Ordenamiento y Estructuras de Datos')
        self.setGeometry(100, 100, 1200, 800)
        self.setWindowIcon(QIcon('./assets/icon.png'))
        
        # ? Layout principal
        main_layout = QHBoxLayout(self)

        # ? Barra lateral
        sidebar_layout = QVBoxLayout()
        main_layout.addLayout(sidebar_layout, 1)

        # ? Crear el QGroupBox para el sidebar
        sidebar_box = QGroupBox()
        sidebar_box_layout = QVBoxLayout(sidebar_box)

        # ? Botones del sidebar
        sidebar_box_layout.addWidget(create_button('Ordenamientos', self.show_arrangements_view))
        sidebar_box_layout.addWidget(create_button('Pilas y Colas', self.show_queue_stacks_view))
        sidebar_box_layout.addWidget(create_button('Árboles', self.show_trees_view))
        sidebar_box_layout.addWidget(create_button('Búsquedas', self.show_searchs_view))

        spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sidebar_box_layout.addItem(spacer)

        sidebar_layout.addWidget(sidebar_box)
        
        sidebar_box.setStyleSheet("""
            QGroupBox {
                background-color: #fff;
                border: 1px solid #d0d0d0;
                border-radius: 5px; /* Radio del borde para esquinas redondeadas */
            }
        """)

        # ? Área principal dinámica
        self.main_area_layout = QVBoxLayout()
        main_layout.addLayout(self.main_area_layout, 4)

        # ? Inicializar las vistas
        self.arrangements_view = ArrangementsView()
        self.queue_stacks_view = QueueStacksView()
        self.trees_view = TreesView()
        self.searchs_view = SearchsView()

        # ? Añadir las vistas al área principal, pero ocultarlas inicialmente
        self.main_area_layout.addWidget(self.arrangements_view)
        self.main_area_layout.addWidget(self.queue_stacks_view)
        self.main_area_layout.addWidget(self.trees_view)
        self.main_area_layout.addWidget(self.searchs_view)
        self.arrangements_view.hide()
        self.queue_stacks_view.hide()
        self.trees_view.hide()
        self.searchs_view.hide()

        # ? Aplicar estilos CSS
        self.apply_styles()

    def apply_styles(self):
        self.setStyleSheet(styles)

    def show_arrangements_view(self):
        self.hide_all_views()
        self.arrangements_view.show()

    def show_queue_stacks_view(self):
        self.hide_all_views()
        self.queue_stacks_view.show()

    def show_trees_view(self):
        self.hide_all_views()
        self.trees_view.show()

    def show_searchs_view(self):
        self.hide_all_views()
        self.searchs_view.show()

    def hide_all_views(self):
        self.arrangements_view.hide()
        self.queue_stacks_view.hide()
        self.trees_view.hide()
        self.searchs_view.hide()

    def no_op(self):
        pass

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
