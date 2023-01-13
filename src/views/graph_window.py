from tkinter import *
try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

from views.graphic_window import gui_support

def destroy_app(root):
    root.destroy()
    exit(0)

class GraphWindow:
    "Класс окна графиков"
    def __init__(self, parent, width, height, title, resizable=(0, 0)):
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
        self.entry_frame.pack(padx=10, pady=10, ipadx=5, ipady=5, fill=X)
        # Надпись "f(x)="
        self.labelfx = Label(self.entry_frame)
        self.labelfx.place(relx=0.04, rely=0.06, height=18, width=35)
        self.labelfx.configure(text='''f(x)=''')
        self.labelfx.configure(fg='#000000')
        self.labelfx.configure(background='#c4c4c4')
        # Поле ввода
        self.fx = Entry(self.entry_frame, width=37)
        self.fx.insert(0, "(x**2)-(7**x)")
        self.fx.pack()
        # Кнопка
        self.bt_plot = Button(self.entry_frame, text="Построить график", width=13, command=self.toPlot)
        self.bt_plot.pack()
        # Холст
        self.graph_canvas = Canvas(self.gwin)
        self.graph_canvas.place(relx=0.04, rely=0.24, relheight=0.70, relwidth=0.92)
        self.graph_canvas.configure(background='#b0b0b0')
        self.graph_canvas.configure(borderwidth="2")
        self.graph_canvas.configure(relief=RIDGE)
        self.graph_canvas.configure(selectbackground="#c4c4c4")
        self.graph_canvas.configure(width=394)
        self.protocol('WM_DELETE_WINDOW', lambda: (self.gwin.destroy()))

    def toPlot(self):
        "Метод отрисовки графика"
        gui_support.Plot(self.fx.get(), range(1, 100, 1), '#FF0000',
                         self.graph_canvas, '-', '')

    def __del__(self):
        "Метод удаления окна графика"
        # root = parent
        self.protocol('WM_DELETE_WINDOW', destroy_app(self))

    def run(self, mx, my, step):
        self.entry_frame.pack()