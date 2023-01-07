from model.calculate import *
from views.graph_window import graph_show

class MathButtonsActions():
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

    def press_clean(self):
        self.parent.clean()

    def clean_last(self):
        self.parent.clean_last()

    def press_pi(self):
        self.parent.display(math_pi())

    def press_e(self):
        self.parent.display(math_e())

    def press_sin(self):
        value = self.parent.get()
        self.parent.clean()
        self.parent.display(math_sin(value))

    def press_cos(self):
        value = self.parent.get()
        self.parent.clean()
        self.parent.display(math_cos(value))

    def press_asin(self):
        value = self.parent.get()
        self.parent.clean()
        self.parent.display(math_asin(value))

    def press_acos(self):
        value = self.parent.get()
        self.parent.clean()
        self.parent.display(math_acos(value))

    def press_tan(self):
        value = self.parent.get()
        self.parent.clean()
        self.parent.display(math_tan(value))

    def press_atan(self):
        value = self.parent.get()
        self.parent.clean()
        self.parent.display(math_atan(value))

    def press_ln(self):
        value = self.parent.get()
        self.parent.clean()
        self.parent.display(math_ln(value))

    def press_sqrt(self):
        value = self.parent.get()
        self.parent.clean()
        self.parent.display(math_sqrt(value))

    def press_power(self):
        value = self.parent.get()
        self.parent.clean()
        self.parent.display(math_power(value))

    def open_graph(self):
        print("Open Graph")
        self.parent.open_graph(425, 500)
