# from turtle import width
from views.buttons_views import CalcButton
from views.main_window import CalcWindow
from views.graph_window import GraphWindow
# from presenter.press_buttons import *
import sys

graph_launch = False

def graph_show():
    "Функция открытия окна графика"
    window.open_graph(400, 500)

if __name__ == "__main__":
    "Функция запуска приложения"
    window = CalcWindow()
    if graph_launch:
        graph_show()

    window.run()