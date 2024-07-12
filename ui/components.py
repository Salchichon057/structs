from PyQt6.QtWidgets import QPushButton

def create_button(text, callback):
    button = QPushButton(text)
    button.setStyleSheet("""
        QPushButton {
            text-align: center;
            padding: 10px;
            margin: 5px 0;
            font-size: 16px;
            background-color: #36BA98;
            border: none;
            color: white;
            border-radius: 5px;
        }
        QPushButton:hover {
            background-color: #45a049;
        }
        QPushButton:pressed {
            background-color: #3e8e41;
        }
    """)
    button.clicked.connect(callback)
    return button
