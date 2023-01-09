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
        self.entry_x = Spinbox(self.entry_frame, from_=0, to=10.0, increment=0.1, width=10).pack()
        self.entry_y = Spinbox(self.entry_frame, from_=0, to=10.0, increment=0.1, width=10).pack()

        # self.x1 = entry_x.get()
        # Поля ввода
        # xvar = StringVar(value="5.0")
        # self.entry_x = Spinbox(self.entry_frame, from_=-10.0, to=10.0,
        #                        increment=0.1, width=10, bg="#b0b0b0",
        #                        command=self.choose_x(self))
        # self.entry_x.pack()
        # Секция графика
        # self.graphic_frame = Canvas(self.gwin, width=mx, height=my, relief=RIDGE)
        # self.graphic_frame.create_line(0, my / 2, mx, my / 2, fill="#6b0f0f", arrow=LAST)
        # self.graphic_frame.create_line(mx / 2, 0, mx / 2, my, fill="#6b0f0f", arrow=BOTH)
        # self.graphic_frame.pack(padx=10, pady=10)
        # # Деления на осях координат
        # for i in range(0, max(mx, my), step):
        #     self.graphic_frame.create_line(i, my/2 - 5, i, my/2 + 5, fill="#6b0f0f")
        #     self.graphic_frame.create_line(mx / 2 - 5, i, mx / 2 + 5, i, fill="#6b0f0f")
        # График функции
    def graphic_show(self):
  
        # the figure that will contain the plot
        fig = Figure(figsize = (5, 5), dpi = 100)
        # list of squares
        y = [i**2 for i in range(40)]
        # adding the subplot
        plot1 = fig.add_subplot(111)
        # plotting the graph
        plot1.plot(y)
        plot1.grid()
        # creating the Tkinter canvas
        # containing the Matplotlib figure
        canvas = FigureCanvasTkAgg(fig, master = self.gwin)  
        canvas.draw()
        # placing the canvas on the Tkinter window
        canvas.get_tk_widget().pack()
        # creating the Matplotlib toolbar
        toolbar = NavigationToolbar2Tk(canvas, self.gwin)
        toolbar.update()
        # placing the toolbar on the Tkinter window
        canvas.get_tk_widget().pack()

    def graphic_params(self):
        print("Params")

    def __del__(self):
        "Метод удаления окна графика"

    def run(self, mx, my, step):
        self.entry_frame.pack()
        self.graphic_show()