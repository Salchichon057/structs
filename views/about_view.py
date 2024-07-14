from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QGroupBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class AboutView(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title_label = QLabel("Acerca de la aplicación")
        title_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)

        group_box = QGroupBox()
        group_box_layout = QVBoxLayout(group_box)

        course_label = QLabel("Curso: Estructura de Datos")
        course_label.setStyleSheet("font-size: 18px; background-color: #fff")
        course_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        group_box_layout.addWidget(course_label)

        team_label = QLabel("Integrantes del equipo:")
        team_label.setStyleSheet("font-size: 18px; font-weight: bold; background-color: #fff")
        team_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        group_box_layout.addWidget(team_label)

        members = [
            "1. Nombre del Integrante 1",
            "2. Nombre del Integrante 2",
            "3. Nombre del Integrante 3",
            "4. Nombre del Integrante 4",
        ]

        for member in members:
            member_label = QLabel(member)
            member_label.setFont(QFont("Arial", 16))
            member_label.setStyleSheet("background-color: #fff, ")
            member_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            group_box_layout.addWidget(member_label)

        year_label = QLabel("2024")
        year_label.setStyleSheet("font-size: 18px; background-color: #fff")
        year_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        group_box_layout.addWidget(year_label)
        
        layout.addWidget(group_box)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)
