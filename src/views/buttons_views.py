from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QPushButton
from controllers.buttons_actions import *
# Класс маленькой кнопки
class SimpleButton(QPushButton):
    "Класс обычной короткой кнопки"
    # Инициализация класса
    def __init__(self):
        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(10, 70)
        self.btn.setFixedWidth(65)
        self.btn.setText("C")
        self.btn.clicked.connect(btn_fnk)

    # Назначение координат кнопки
    def coordinates(self, x, y):
        self.btn.move(x, y)

    # Назначение цвета кнопки

    # Назначение функции кнопки
    def action(self, btn_function):
        self.btn.clicked.connect(btn_function)

# # Класс большой кнопки
# class LongButton(QPushButton):
def little_btn():
    btn = SimpleButton()