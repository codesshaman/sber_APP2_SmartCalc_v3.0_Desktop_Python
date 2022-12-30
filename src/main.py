import tkinter as tk
from views.buttons_views import *
from presenter.press_buttons import *
import sys

print(sys.path)

def check_debug():
    file = open("debug.txt")
    check = (file.read())
    check = (file.read())
    if check == 'true':
        return True
    elif check == 'false':
        return False
    else:
        return None

debug = check_debug()

# Класс основного окна
class CalcWindow(QMainWindow):
    "Класс основного окна приложения"
    # Инициализация класса
    def __init__(self):
        super().__init__()
        super(CalcWindow, self).__init__()
        if debug:
            print("Инициализация основного окна приложения")
        # Заголовок окна
        super(CalcWindow, self).__init__()
        self.setWindowTitle("SmartCalc v3.0.0")
        self.setGeometry(500, 300, 450, 300)
        # Цифровое поле
        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("1234567890")
        self.main_text.move(10, 10)
        self.main_text.setFixedWidth(480)
        # Кнопки
        self.btn3 = QtWidgets.QPushButton(self)
        self.btn3.move(10, 70)
        self.btn3.setFixedWidth(65)
        self.btn3.setText("C")
        self.btn3.clicked.connect(press_button)
        self.btn2 = Button(90, 100, 65, "D")

    def __del__(self):
        "Функция удаления класса"
        if debug:
            print("Программа завершена")

def calculator():
    "Функция вызова приложения"
    app = QApplication(sys.argv)
    window = CalcWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    "Функция запуска приложения"
    if debug:
        print("Программа запущена")
    calculator()