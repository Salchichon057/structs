styles = """
    QWidget {
        background-color: #F5F7F8;
        color: #2E2E2E;
        font-family: Arial, sans-serif;
    }
    QGroupBox {
        background-color: #FFFFFF;
        border: 1px solid #D3D3D3;
        border-radius: 8px;
        margin-top: 20px;
        padding: 10px;
    }
    QPushButton {
        font-size: 16px;
        padding: 10px 15px;
        margin: 10px 0;
        border: 1px solid #2E2E2E;
        border-radius: 5px;
        background-color: #FFFFFF;
        color: #2E2E2E;
        font-weight: bold;
    }
    QPushButton:hover {
        background-color: #E0E0E0;
    }
    QPushButton:pressed {
        background-color: #D0D0D0;
    }
    QComboBox {
        font-size: 16px;
        padding: 10px;
        margin: 10px 0;
        border: 1px solid #D3D3D3;
        border-radius: 5px;
        background-color: #FFFFFF;
        color: #2E2E2E;
        font-weight: normal;
    }
    QComboBox::drop-down {
        subcontrol-origin: padding;
        subcontrol-position: top right;
        width: 15px;
        border-left-width: 1px;
        border-left-color: #D3D3D3;
        border-left-style: solid;
        border-top-right-radius: 3px;
        border-bottom-right-radius: 3px;
    }
    QComboBox::down-arrow {
        image: url(down_arrow.png);
        width: 10px;
        height: 10px;
    }
    QComboBox QAbstractItemView {
        border: 1px solid #D3D3D3;
        selection-background-color: #2E2E2E;
        selection-color: #FFFFFF;
    }
    QLabel {
        font-size: 16px;
        margin: 10px 0;
        color: #2E2E2E;
        font-weight: bold;
    }
    QTextEdit {
        font-size: 16px;
        margin: 10px 0;
        padding: 10px;
        border: 1px solid #D3D3D3;
        border-radius: 5px;
        background-color: #FFFFFF;
        min-height: 100px;
        font-weight: normal;
    }
    QScrollBar:vertical {
        border: 1px solid #D3D3D3;
        background: #FFFFFF;
        width: 15px;
        margin: 22px 0 22px 0;
    }
    QScrollBar::handle:vertical {
        background: #B0B0B0;
        min-height: 20px;
        border-radius: 5px;
    }
    QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
        border: 1px solid #D3D3D3;
        background: #E0E0E0;
        height: 20px;
        subcontrol-position: top;
        subcontrol-origin: margin;
    }
    QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
        border: 1px solid #D3D3D3;
        width: 3px;
        height: 3px;
        background: #2E2E2E;
    }
    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
        background: none;
    }
"""
