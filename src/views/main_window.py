from tkinter import *
from model.debug import check_debug
debug = check_debug()

class CalcWindow():
    "Класс основного окна приложения"
    # Инициализация класса
    def __init__(self, width="450", height="350", title="SmartCalc_v3", resizable=(0, 0)):
        super().__init__()
        if debug:
            print("Инициализация основного окна приложения")
        self.win = Tk()
        self.win.title(title)
        self.win.geometry(f"{width}x{height}+200+200")
        self.win.resizable(resizable[0], resizable[1])
        self.win.configure(bg='gray')

    def run(self):
        "Функция запуска основного окна"
        self.win.mainloop()

    def __del__(self):
        "Функция удаления основного окна"
        if debug:
            print("Программа завершена")

    def open_graph(self):
        "Функция открытия окна графика"