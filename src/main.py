# from tkinter import *
from turtle import width

from views.main_window import CalcWindow
from views.graph_window import GraphWindow
# from presenter.press_buttons import *
from model.debug import check_debug
import sys

debug = check_debug()
graph_launch = False

print(sys.path)

def graph_show():
    "Функция открытия окна графика"
    if debug:
        print("Окно с графиком открыто")
    window.open_graph(400, 500)

if __name__ == "__main__":
    "Функция запуска приложения"
    if debug:
        print("Программа запущена")
    window = CalcWindow()
    if graph_launch:
        graph_show()

    window.run()