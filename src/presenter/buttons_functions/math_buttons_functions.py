from model import calculate as calc
from presenter.buttons_functions import history


class MathButtonsActions():
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.history = history.CalcHistory()

    def press_clean(self):
        self.parent.clean()

    def press_clean_history(self):
        self.parent.clean()
        self.parent.flag = True
        self.history.del_history()

    def clean_last(self):
        self.parent.clean_last()

    def press_pi(self):
        self.parent.display(calc.math_pi())

    def press_e(self):
        self.parent.display(calc.math_e())

    def press_log(self):
        value = self.parent.get()
        self.parent.clean()
        self.parent.display(calc.math_log(value))

    def press_sin(self):
        value = self.parent.get()
        self.parent.clean()
        self.parent.display(calc.math_sin(value))

    def press_cos(self):
        value = self.parent.get()
        self.parent.clean()
        self.parent.display(calc.math_cos(value))

    def press_asin(self):
        value = self.parent.get()
        self.parent.clean()
        self.parent.display(calc.math_asin(value))

    def press_acos(self):
        value = self.parent.get()
        self.parent.clean()
        self.parent.display(calc.math_acos(value))

    def press_tan(self):
        value = self.parent.get()
        self.parent.clean()
        self.parent.display(calc.math_tan(value))

    def press_atan(self):
        value = self.parent.get()
        self.parent.clean()
        self.parent.display(calc.math_atan(value))

    def press_ln(self):
        value = self.parent.get()
        self.parent.clean()
        self.parent.display(calc.math_ln(value))

    def press_sqrt(self):
        value = self.parent.get()
        self.parent.clean()
        self.parent.display(calc.math_sqrt(value))

    def press_power(self):
        value = self.parent.get()
        self.parent.clean()
        self.parent.display(calc.math_power(value))

    def input_x(self):
        value = self.parent.get()
        if len(value) > 0:
            if value != "0":
                self.parent.x_variable = value
                self.parent.x_flag = True

    def print_x(self):
        self.parent.display(self.parent.x_variable)

    def x_func(self):
        if self.parent.x_flag:
            self.print_x()
            self.parent.x_flag = False
        else:
            self.input_x()

    def open_graph(self):
        # print("Open Graph")
        self.parent.open_graph(425, 444)
