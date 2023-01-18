import tkinter as tk
from tkinter import messagebox as mb
from views.graph_window import GraphWindow
from presenter.buttons_functions import logs
from views.credit_window import CreditWindow
from views.buttons_panels.math_pannel import math_pannel
from views.buttons_panels.numbers_pannel import nums_pannel
from views.buttons_panels.credit_deposit_view import credit_deposit_buttons
from presenter.buttons_functions import num_buttons_functions
from presenter.buttons_functions import math_buttons_functions
from views.buttons_panels.operations_pannel import operations_panel


class CalcWindow():
    "Класс основного окна приложения"
    # Инициализация класса
    def __init__(self, width="555", height="444",
                 title="SmartCalc_v3", resizable=(0, 0)):
        super().__init__()
        self.win = tk.Tk()
        self.counter = 0
        self.flag = False
        self.x_flag = False
        self.x_variable = ""
        self.win.title(title)
        self.logs = logs.CalcLogs()
        self.win.geometry(f"{width}x{height}+200+200")
        self.win.resizable(resizable[0], resizable[1])
        self.win.configure(bg='gray')
        # self.win.iconbitmap("icon.ico")
        # Секция дисплея
        self.display_frame = tk.LabelFrame(self.win, bg="#808080",
                                           text="ЭЛЕКТРОНИКА МК - 4221")
        # Окно ввода
        self.input_display = tk.Entry(self.display_frame, width=17,
                                      bg="#b0b0b0", relief=tk.RIDGE,
                                      font="Calibri 36")
        # Секция кнопок
        self.buttons_frame = tk.Frame(self.win, borderwidth=2,
                                      bg="#b0b0b0", relief=tk.RIDGE)

    def __del__(self):
        "Метод удаления основного окна"


    def open_wigets(self):
        "Метод открытия виджетов"
        # Секция дисплея
        self.display_frame.pack(padx=10, pady=10, ipadx=15, ipady=5, fill=tk.X)
        # Окно ввода
        self.input_display.pack(side=tk.TOP)
        # Секция кнопок
        self.buttons_frame.place(x=10, y=100, width=535, height=260)

    def clear_logs_file(self):
        self.logs.clean_old_logs(0)

    def open_buttons(self):
        "Методы открытия панелей с кнопками"
        # Панель математических операций
        math_pannel(self, 0, 0)
        # Числовая панель
        nums_pannel(self, 225, 0)
        # Панель простых операций
        operations_panel(self, 225, 0)
        # Кнопки кредита и депозита
        credit_deposit_buttons(self)

    def open_graph(self, width, height, title="SmartCalc Graph",
                   resizable=(0, 0)):
        "Метод открытия окна графика"
        graph = GraphWindow(self.win, width, height, title, resizable)
        graph.run()

    def open_credit(self):
        credit = CreditWindow(self.win)
        credit.run()

    def open_depos(self):
        depos = CreditWindow(self.win)
        depos.run()

    def press_key(self, event):
        "Метод вызова функций по нажатию клавиш"
        # print(event)
        func = num_buttons_functions.NumButtonsActions(self)
        matf = math_buttons_functions.MathButtonsActions(self)
        if event.char in '0123456789':
            if self.flag:
                self.flag = False
                self.clean()
            self.display(event.char)
        elif event.char in '+-*/()^%.,':
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
        elif event.char in 'XxЧч':
            matf.x_func()
        elif event.char in 'pPзЗ':
            matf.press_pi()
        elif event.char in 'eEуУ':
            matf.press_e()
        elif event.char == '\uf700':
            func.history_back()
        elif event.char == '\uf701':
            func.history_for()
        elif event.char in '[х':
            func.history_back()
        elif event.char in ']ъ':
            func.history_for()
        elif event.char in 'рh':
            self.about()

    def key_catch(self):
        "Метод захвата нажатий клавиш"
        self.win.bind('<Key>', self.press_key)

    def clean(self):
        "Метод сброса ввода"
        self.input_display.delete(0, tk.END)

    def clean_last(self):
        "Метод стирания последнего символа"
        length = len(self.input_display.get())
        self.input_display.delete(length-1)

    def display(self, symbol):
        "Метод вывода чисел на дисплей"
        self.input_display.insert(tk.END, symbol)

    def get(self):
        "Метод захвата содержимого дисплея"
        return self.input_display.get()

    def about(self):
        mb.showinfo("SmartCalc_v3",
                    'РЕАЛИЗОВАННЫЙ ФУНКЦИОНАЛ:\n'
                    '-раздел справки (это окно)\n'
                    '-окно калькулятора(ну ты его полюбому уже видел)\n'
                    '-окно графиков(жмякнуть кнопку "graph" перед 0)\n'
                    '-кредитный калькулятор (кнопка слева снизу)\n'
                    '-депозитный калькулятор (кнопка справа снизу)\n'
                    '\n'
                    'Данное приложение реализовано в рамках '
                    'федеральной программы развития отечественных '
                    'вычислительных систем при поддержке ООО "Сбер"'
                    'и его подразделения "Школа-21".'
                    '\n'
                    'Автор и разработчик продукта: '
                    'jleslee@student.21-school.ru\n'
                    'Никакие права не защищены.\n'
                    'Copyright © 2023 Jimmie Leslee')

    def run(self):
        "Метод запуска основного окна"
        func = num_buttons_functions.NumButtonsActions(self)
        self.open_wigets()
        func.print_last()
        self.open_buttons()
        self.clear_logs_file()
        self.key_catch()
        self.win.mainloop()
