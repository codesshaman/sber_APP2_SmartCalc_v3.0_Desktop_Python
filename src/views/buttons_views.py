import tkinter as tk
from main import check_debug
from presenter.press_buttons import *

debug = check_debug()

class Button(QtWidgets):
    "Класс обычной кнопки"
    # Инициализация класса
    def __init__(self, x, y, width, text):
        super().__init__()
        if debug:
            print("Инициализация кнопки")
        self.btn = QPushButton(self)
        self.btn.move(x, y)
        self.btn.setFixedWidth(width)
        self.btn.setText(text)
        self.btn.clicked.connect(press_button)

def button_show():
    btn = Button(90, 70, 65, "B")
    btn.show()


# # Класс маленькой кнопки
# class SimpleButton(QPushButton):
#     "Класс обычной короткой кнопки"
#     # Инициализация класса
#     def __init__(self):
#         super().__init__()
#         if debug:
#             print("Инициализация короткой кнопки")
#         self.btn = QtWidgets.QPushButton(self)
#         self.btn.move(10, 70)
#         self.btn.setFixedWidth(65)
#         self.btn.setText("C")
#         self.btn.clicked.connect(press_button)
#
#     # Назначение координат кнопки
#     def coordinates(self, x, y):
#         self.btn.move(x, y)
#
#     # Назначение цвета кнопки
#
#     # Назначение функции кнопки
#     def action(self, btn_function):
#         self.btn.clicked.connect(btn_function)

# # Класс большой кнопки
# class LongButton(QPushButton):
def little_btn():
    btn = SimpleButton()