from tkinter import *
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
        self.entry_frame = Frame(self.gwin, borderwidth=2, bg="#b0b0b0", relief=RIDGE)
        self.entry_frame.pack(padx=10, pady=10, ipadx=15, ipady=5, fill=X)
        self.entry_x = Spinbox(self.entry_frame, from_=-10.0, to=10.0, increment=0.1, width=10, bg="#b0b0b0").pack()
        # Секция графика
        self.graphic_frame = Canvas(self.gwin, width=mx, height=my, relief=RIDGE)
        self.graphic_frame.create_line(0, my / 2, mx, my / 2, fill="#6b0f0f", arrow=LAST)
        self.graphic_frame.create_line(mx / 2, 0, mx / 2, my, fill="#6b0f0f", arrow=BOTH)
        self.graphic_frame.pack(padx=10, pady=10)
        # Деления на осях координат
        for i in range(0, max(mx, my), step):
            self.graphic_frame.create_line(i, my/2 - 5, i, my/2 + 5, fill="#6b0f0f")
            self.graphic_frame.create_line(mx / 2 - 5, i, mx / 2 + 5, i, fill="#6b0f0f")
        # График функции

    def choose_x(self, abc):
        choose = self.entry_x.get()
        print(choose)
        return choose
    def draw_graph(self, mx, my, step):
        b = 0
        k = 1
        x1=4
        x2=-4
        y1=k*x1+b
        y2=k*x2+b
        self.graphic_frame.create_line(x1 * step + mx / 2, y1 * step + my / 2, x2 * step + mx / 2, y2 * step + my / 2)

    def __del__(self):
        "Метод удаления окна графика"

    def coords_splitting(self, mx, my, step):
        "Вывод делений на осях координат"
        for i in range(0, max(mx, my), step):
            self.graphic_frame.create_line(i, my/2 - 5, i, my/2 + 5, fill="#6b0f0f")
            self.graphic_frame.create_line(mx / 2 - 5, i, mx / 2 + 5, i, fill="#6b0f0f")

    def run(self, mx, my, step):
        self.entry_frame.pack()
        # self.coords_lines(self, self.mx, self.my)
        self.draw_graph(mx, my, step)