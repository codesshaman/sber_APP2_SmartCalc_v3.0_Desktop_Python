import numpy as np
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

class GraphWindow:
    "Класс окна графиков"
    def __init__(self, parent, width, height, step, title, resizable=(0, 0)):
        super().__init__()
        mx = 400
        my = 400
        self.width = width
        self.icon = None
        self.gwin = Toplevel(parent)
        self.gwin.title(title)
        self.gwin.geometry(f"{width}x{height}+755+200")
        self.gwin.resizable(resizable[0], resizable[1])
        self.gwin.configure(bg='gray')
        # Секция ввода
        self.entry_frame = Frame(self.gwin, borderwidth=2, relief=RIDGE)
        self.entry_frame.pack(padx=10, pady=10, ipadx=15, ipady=5, fill=X)
        self.entry_x = Entry(self.entry_frame, width=10)
        self.entry_x.insert(0, "-5")
        self.entry_x.pack()
        self.entry_y = Entry(self.entry_frame, width=10)
        self.entry_y.insert(0, "5")
        self.entry_y.pack()
        # self.recount = GraphFunctions(self)
        # self.func = self.recount.graph_recount(self)
        # Секция вывода
        # self.recount = Button(self.entry_frame, text="Пересчитать", width=10, command = self.func)
        # self.recount.pack()
        # Секция графика
        # self.recount.pack()

    # def button

    def graphic_show(self, x):
        fig = Figure(figsize = (5, 5), dpi = 100)
        x = 2
        y = [i**2 for i in range(40)]
        plot1 = fig.add_subplot(111)
        plot1.plot(y)
        plot1.grid(which='major')
        plot1.grid(which='minor', linestyle=':')
        plot1.minorticks_on()
        canvas = FigureCanvasTkAgg(fig, master = self.gwin)
        canvas.draw()
        canvas.get_tk_widget().pack()
        toolbar = NavigationToolbar2Tk(canvas, self.gwin)
        toolbar.update()
        canvas.get_tk_widget().pack()

    def recount(self):
        print("recount")
        self.graphic_show()

    def graph_button(self):
        self.button = Button(self.entry_frame, text="Построить график", width=13, command=self.recount)
        self.button.pack()

    def graphic_params(self):
        print("Params")

    def get_value(self):
        self.entry_x.get()

    def __del__(self):
        "Метод удаления окна графика"

    def run(self, mx, my, step):
        self.entry_frame.pack()
        self.graph_button()