from tkinter import *
class GraphWindow:
    "Класс окна графиков"
    def __init__(self, parent, width, height, title="SmartCalc_v3", resizable=(0, 0), icon=None):
        super().__init__()
        mx = 400
        my = 400
        self.width = width
        self.gwin = Toplevel(parent)
        self.gwin.title(title)
        self.gwin.geometry(f"{width}x{height}+755+200")
        self.gwin.resizable(resizable[0], resizable[1])
        self.gwin.configure(bg='gray')
        # Секция ввода
        self.entry_frame = Frame(self.gwin, borderwidth=2, bg="#b0b0b0", relief=RIDGE)
        self.entry_frame.pack(padx=10, pady=10, ipadx=15, ipady=5, fill=X)
        # Секция графика
        self.graphic_frame = Canvas(self.gwin, width=mx, height=my, relief=RIDGE)
        self.graphic_frame.create_line(0, my / 2, mx, my / 2, fill="#6b0f0f", arrow=LAST)
        self.graphic_frame.create_line(mx / 2, 0, mx / 2, my, fill="#6b0f0f", arrow=BOTH)
        self.graphic_frame.pack(padx=10, pady=10)
        # Деления на осях координат
        for i in range(0, max(mx, my), 40):
            self.graphic_frame.create_line(i, my/2 - 5, i, my/2 + 5, fill="#6b0f0f")
            self.graphic_frame.create_line(mx / 2 - 5, i, mx / 2 + 5, i, fill="#6b0f0f")
    def __del__(self):
        "Метод удаления окна графика"

    def run(self):
        self.entry_frame.pack()
        # self.coords_lines(self, self.mx, self.my)
def graph_show(parent):
    "Функция открытия окна графика"
    parent.open_graph(400, 500)