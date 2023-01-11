import time
import numpy as np
import numexpr as ne
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

class GraphWindow:
    "Класс окна графиков"
    def __init__(self, parent, width, height, step, title, resizable=(0, 0)):
        super().__init__()
        self.command = False
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
        self.entry_func = Entry(self.entry_frame, width=10)
        self.entry_func.insert(0, "x^2")
        self.entry_func.pack()

    def recount(self):
        if self.command == True:
            func = self.entry_func.get()
            fig = Figure(figsize = (5, 5), dpi = 100)
            # y = [i**2 for i in range(40)]
            x_vals = np.arange(-5, 5, 100)
            y = []
            func = func.replace('^', '**').strip('')
            func = func.replace('X', 'x')
            for x in x_vals:
                y.append(ne.evaluate(func))
            # plot_instance = axes.plot(x_vals, y, '-', lw=1)
            # axes.set_xlim(-5, 5)
            # axes.set_ylim(-5, 5)
            # axes.legend(legend, loc='best', )
            self.plot1 = fig.add_subplot(111)
            self.plot1.plot(x_vals, y, lw=1)
            self.plot1.grid(which='major')
            self.plot1.grid(which='minor', linestyle=':')
            self.plot1.minorticks_on()
            self.canvas = FigureCanvasTkAgg(fig, master = self.gwin)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack()
            self.command = True
        else:
            # self.plot1.destroy()
            func = self.entry_func.get()
            fig = Figure(figsize=(5, 5), dpi=100)
            # y = [i**2 for i in range(40)]
            x, y = np.meshgrid(np.linspace(-5, 5, 100), np.linspace(-5, 5, 100))
            self.plot1 = fig.add_subplot(111)
            z = eval(func)
            self.plot1.plot(x, y, z)
            self.plot1.grid(which='major')
            self.plot1.grid(which='minor', linestyle=':')
            self.plot1.minorticks_on()
            self.canvas = FigureCanvasTkAgg(fig, master=self.gwin)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack()
            self.command = True

    def graphic_del(self):
        self.canvas.get_tk_widget.destroy()

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