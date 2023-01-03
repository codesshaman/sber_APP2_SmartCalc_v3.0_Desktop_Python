from tkinter import *
from views.graph_window import GraphWindow
from model.debug import check_debug
from views.buttons_views import CalcButton
debug = check_debug()

class CalcWindow():
    "Класс основного окна приложения"
    # Инициализация класса
    def __init__(self, width="550", height="350", title="SmartCalc_v3", resizable=(0, 0)):
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
        # Рамки основных секций
        display_frame = LabelFrame(self.win, bg="#808080", text="ЭЛЕКТРОНИКА - 224")
        buttons_frame = Frame(self.win, borderwidth=2, bg="#b0b0b0", relief=RIDGE)
        display_frame.pack(padx=10, pady=10, ipadx=15, ipady=5, fill=X)
        buttons_frame.place(x=10, y=100, width=530, height=240)
        Label(display_frame, text="0123456789", bg="#b0b0b0", relief=RIDGE, font="Calibri 36").pack(side=TOP)
        # Label(buttons_frame, text="Здесь будут кнопки", bg="#b0b0b0", relief=RIDGE, font="Calibri 36").pack(side=TOP)

    def open_buttons(self):
        Button(self.win, width=3, height=1, text="CCC", justify=LEFT).pack(padx=20, pady=5, anchor=NW)
        b2 = CalcButton(parent="win", text="CCC", width=3, height=1)
        b2.pack(padx=20, pady=5, anchor=NW)

    def open_graph(self, width, height, title="График", resizable=(0, 0), icon=None):
        "Функция открытия окна графика"
        GraphWindow(self.win, width, height, title, resizable, icon)