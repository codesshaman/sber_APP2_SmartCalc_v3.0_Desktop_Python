# from tkinter import *
from views.main_window import CalcWindow
# from presenter.press_buttons import *
import sys

print(sys.path)

# Класс основного окна

window = CalcWindow()
window.run()

def calculator():
    "Функция вызова приложения"
    window = CalcWindow()

if __name__ == "__main__":
    "Функция запуска приложения"
    if debug:
        print("Программа запущена")
    window = CalcWindow()
    window.run()