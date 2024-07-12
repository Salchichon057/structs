from PyQt6.QtWidgets import QPushButton

def create_button(text, callback):
    button = QPushButton(text)
    button.setStyleSheet("text-align: left; padding: 10px; margin: 5px 0; font-size: 16px;")
    button.clicked.connect(callback)
    return button
