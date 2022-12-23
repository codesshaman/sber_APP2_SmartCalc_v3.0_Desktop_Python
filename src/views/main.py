from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
from controllers.buttons_actions import *
import sys

class CalcWindow(QMainWindow):
    def __init__(self):
        super(CalcWindow, self).__init__()
        self.setWindowTitle("SmartCalc v3.0.0")
        self.setGeometry(500, 300, 450, 300)
        # Окно для цифр
        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("1234567890")
        self.main_text.move(10, 10)
        self.main_text.setFixedWidth(480)
        # Кнопки
        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(10, 70)
        self.btn.setFixedWidth(65)
        self.btn.setText("C")
        self.btn.clicked.connect(btn_fnk)

def calculator():
    app = QApplication(sys.argv)
    window = CalcWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    calculator()