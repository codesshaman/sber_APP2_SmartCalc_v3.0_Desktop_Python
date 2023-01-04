from tkinter import *
from model.debug import check_debug
from views.math_pannel import math_pannel
from views.graph_window import GraphWindow
from views.numbers_pannel import nums_pannel
from views.operations_pannel import operations_panel
from views.credit_deposit_view import credit_deposit_buttons

debug = check_debug()

class CalcWindow():
    "Класс основного окна приложения"
    # Инициализация класса
    def __init__(self, width="555", height="444", title="SmartCalc_v3", resizable=(0, 0)):
        super().__init__()
        if debug:
            print("Инициализация основного окна приложения")
        self.win = Tk()
        self.win.title(title)
        self.win.geometry(f"{width}x{height}+200+200")
        self.win.resizable(resizable[0], resizable[1])
        self.win.configure(bg='gray')
        # self.win.iconbitmap("icon.ico")
        # Секция дисплея
        self.display_frame = LabelFrame(self.win, bg="#808080", text="ЭЛЕКТРОНИКА МК - 4221")
        # Окно ввода
        self.input_display = Entry(self.display_frame, width=16, bg="#b0b0b0", relief=RIDGE, font="Calibri 36")
        # Секция кнопок
        self.buttons_frame = Frame(self.win, borderwidth=2, bg="#b0b0b0", relief=RIDGE)

    def __del__(self):
        "Метод удаления основного окна"
        if debug:
            print("Программа завершена")

    def open_wigets(self):
        "Метод открытия виджетов"
        # Секция дисплея
        self.display_frame.pack(padx=10, pady=10, ipadx=15, ipady=5, fill=X)
        # Окно ввода
        self.input_display.pack(side=TOP)
        # Секция кнопок
        self.buttons_frame.place(x=10, y=100, width=535, height=260)

    def open_buttons(self):
        "Метод открытия панелей с кнопками"
        math_pannel(self, 0, 0)
        nums_pannel(self, 225, 0)
        operations_panel(self, 225, 0)
        credit_deposit_buttons()

    def open_graph(self, width, height, title="График", resizable=(0, 0), icon=None):
        "Метод открытия окна графика"
        GraphWindow(self.win, width, height, title, resizable, icon)

    def clear(self):
        "Метод сброса ввода"
        self.input_display.delete(0, END)

    def display(self, symbol):
        "Метод вывода чисел на дисплей"
        self.input_display.insert(END, symbol)

    def run(self):
        "Метод запуска основного окна"
        self.open_wigets()
        self.open_buttons()
        self.win.mainloop()