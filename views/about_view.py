from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QGroupBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class AboutView(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title_label = QLabel("Acerca de la aplicación")
        title_label.setStyleSheet("font-size: 36px; font-weight: bold;")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)

        group_box = QGroupBox()
        group_box_layout = QVBoxLayout(group_box)

        course_label = QLabel("Curso")
        course_label.setStyleSheet("font-size: 24px; font-weight: bold; background-color: #fff")
        course_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        group_box_layout.addWidget(course_label)
        
        name_course_label = QLabel("Estructura de Datos")
        name_course_label.setStyleSheet("font-size: 18px; background-color: #fff; font-weight: normal;")
        name_course_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        group_box_layout.addWidget(name_course_label)

        team_label = QLabel("Integrantes del equipo")
        team_label.setStyleSheet("font-size: 24px; font-weight: bold; background-color: #fff")
        team_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        group_box_layout.addWidget(team_label)

        members = [
            "1. Oropeza Luna Elizabeth",
            "2. Rafael Coral Antonny",
            "3. Valvas Roblex Félix",
            "4. Violeta De La Cruz Alvaro",
            "5. Zarzosa Caqui Valeriano"
        ]

        for member in members:
            member_label = QLabel(member)
            member_label.setFont(QFont("Arial", 18, QFont.Weight.Medium))
            member_label.setStyleSheet("font-size: 18px; background-color: #fff; font-weight: normal;")
            member_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            group_box_layout.addWidget(member_label)

        year_label = QLabel("2024")
        year_label.setStyleSheet("font-size: 18px; background-color: #fff; font-weight: bold;")
        year_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        group_box_layout.addWidget(year_label)
        
        layout.addWidget(group_box)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)
