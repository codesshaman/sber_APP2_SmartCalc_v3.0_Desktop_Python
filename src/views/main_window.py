from tkinter import *
from views.graph_window import GraphWindow
from model.debug import check_debug
from views.math_pannel import math_pannel
from views.numbers_pannel import nums_pannel
from views.operations_pannel import operations_panel
debug = check_debug()

class CalcWindow():
    "Класс основного окна приложения"
    # Инициализация класса
    def __init__(self, width="555", height="410", title="SmartCalc_v3", resizable=(0, 0)):
        super().__init__()
        if debug:
            print("Инициализация основного окна приложения")
        self.win = Tk()
        self.win.title(title)
        self.win.geometry(f"{width}x{height}+200+200")
        self.win.resizable(resizable[0], resizable[1])
        self.win.configure(bg='gray')
        # self.win.iconbitmap("icon.ico")

        self.label = Label(self.win, text="0123456789", bg="red", relief=RIDGE, font="Calibri 36")

    # SUNKEN GROOVE
    def run(self):
        "Функция запуска основного окна"
        self.open_wigets()
        self.open_buttons()
        self.win.mainloop()

    def __del__(self):
        "Функция удаления основного окна"
        if debug:
            print("Программа завершена")

    def open_wigets(self):
        "Функция открытия виджетов"
        # Секция дисплея
        display_frame = LabelFrame(self.win, bg="#808080", text="ЭЛЕКТРОНИКА МК - 4221")
        buttons_frame = Frame(self.win, borderwidth=2, bg="#b0b0b0", relief=RIDGE)
        display_frame.pack(padx=10, pady=10, ipadx=15, ipady=5, fill=X)
        Entry(display_frame, width=16, bg="#b0b0b0", relief=RIDGE, font="Calibri 36").pack(side=TOP)
        # Секция кнопок
        buttons_frame.place(x=10, y=100, width=535, height=260)

    def open_buttons(self):
        # Панель сложных математических функций
        math_pannel(0, 0)
        nums_pannel(225, 0)
        operations_panel(225, 0)

    def open_graph(self, width, height, title="График", resizable=(0, 0), icon=None):
        "Функция открытия окна графика"
        GraphWindow(self.win, width, height, title, resizable, icon)