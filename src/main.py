# from tkinter import *
from turtle import width

from views.main_window import CalcWindow
from views.graphwindow import GraphWindow
# from presenter.press_buttons import *
from model.debug import check_debug
import sys

debug = check_debug()

print(sys.path)

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
    window.open_graph(400, 500)

    window.run()