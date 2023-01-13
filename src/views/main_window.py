from views.buttons_panels.math_pannel import math_pannel
from views.graph_window import *
from views.buttons_panels.numbers_pannel import nums_pannel
from presenter.buttons_functions.num_buttons_functions import *
from views.buttons_panels.operations_pannel import operations_panel
from views.credit_deposit_view import credit_deposit_buttons

class CalcWindow():
    "Класс основного окна приложения"
    # Инициализация класса
    def __init__(self, width="555", height="444", title="SmartCalc_v3", resizable=(0, 0)):
        super().__init__()
        self.win = Tk()
        self.win.title(title)
        self.win.geometry(f"{width}x{height}+200+200")
        self.win.resizable(resizable[0], resizable[1])
        self.win.configure(bg='gray')
        # self.win.iconbitmap("icon.ico")
        # Секция дисплея
        self.display_frame = LabelFrame(self.win, bg="#808080", text="ЭЛЕКТРОНИКА МК - 4221")
        # Окно ввода
        self.input_display = Entry(self.display_frame, width=17, bg="#b0b0b0", relief=RIDGE, font="Calibri 36")
        # Секция кнопок
        self.buttons_frame = Frame(self.win, borderwidth=2, bg="#b0b0b0", relief=RIDGE)

    def __del__(self):
        "Метод удаления основного окна"

    def open_wigets(self):
        "Метод открытия виджетов"
        # Секция дисплея
        self.display_frame.pack(padx=10, pady=10, ipadx=15, ipady=5, fill=X)
        # Окно ввода
        self.input_display.pack(side=TOP)
        # Секция кнопок
        self.buttons_frame.place(x=10, y=100, width=535, height=260)

    def open_buttons(self):
        "Методы открытия панелей с кнопками"
        # Панель математических операций
        math_pannel(self, 0, 0)
        # Числовая панель
        nums_pannel(self, 225, 0)
        # Панель простых операций
        operations_panel(self, 225, 0)
        # Кнопки кредита и депозита
        credit_deposit_buttons()

    def open_graph(self, width, height, title="SmartCalc Graph", resizable=(0, 0)):
        "Метод открытия окна графика"
        # graph = vp_start_gui(self.win)
        graph = GraphWindow(self.win, width, height, title, resizable)
        graph.run()
        # graph.coords_splitting(self.win, mx=400, my=400, step=40)

    def press_key(self, event):
        "Метод вызова функций по нажатию клавиш"
        # print(event)
        func = NumButtonsActions(self)
        # matf = MathButtonsActions(self)
        if event.char in '0123456789+-*/()^%':
            self.display(event.char)
        elif event.char == "\r":
            func.calculate()
        elif event.char == "\x03":
            func.calculate()
        elif event.char == '\x7f':
            self.clean_last()
        elif event.char == '\x08':
            self.clean_last()
        elif event.char in 'cCсС':
            self.clean()
        elif event.char in 'pPзЗ':
            matf.press_pi()
        elif event.char in 'eEуУ':
            matf.press_e()

    def key_catch(self):
        "Метод захвата нажатий клавиш"
        self.win.bind('<Key>', self.press_key)

    def clean(self):
        "Метод сброса ввода"
        self.input_display.delete(0, END)

    def clean_last(self):
        "Метод стирания последнего символа"
        length = len(self.input_display.get())
        self.input_display.delete(length-1)

    def display(self, symbol):
        "Метод вывода чисел на дисплей"
        self.input_display.insert(END, symbol)

    def get(self):
        "Метод захвата содержимого дисплея"
        return self.input_display.get()

    def run(self):
        "Метод запуска основного окна"
        self.open_wigets()
        self.open_buttons()
        self.key_catch()
        self.win.mainloop()