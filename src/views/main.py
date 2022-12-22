from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
from controllers.buttons_actions import *
import sys

def calculator():
    app = QApplication(sys.argv)
    window = QMainWindow()
    # Заголовок и отступы
    window.setWindowTitle("SmartCalc v3.0.0")
    window.setGeometry(500, 300, 450, 300)
    # Окно для цифр
    main_text = QtWidgets.QLabel(window)
    main_text.setText("1234567890")
    main_text.move(10, 10)
    main_text.setFixedWidth(480)
    # Кнопки
    btn = QtWidgets.QPushButton(window)
    btn.move(10, 70)
    btn.setFixedWidth(65)
    btn.setText("C")
    btn.clicked.connect(btn_fnk)
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    calculator()