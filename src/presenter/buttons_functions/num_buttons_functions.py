from model.calculate import *
from presenter.buttons_functions.history import *

class NumButtonsActions():
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.history = CalcHistory()
        self.counter = self.parent.counter
        self.prew_actions = self.history.read_file()

    def history_clean(self):
        self.parent.counter = 0


    def print_last(self):
        prew_len = len(self.prew_actions)
        if prew_len > 0:
            self.parent.display(self.prew_actions[self.parent.counter])
        else:
            self.parent.flag = True
            self.parent.display(0)


    def history_back(self):
        prew_len = len(self.prew_actions)
        if prew_len > 0:
            self.parent.clean()
            self.parent.counter += 1
            if int(self.parent.counter) >= len(self.prew_actions):
                self.history_clean()
            self.parent.display(self.prew_actions[self.parent.counter])
        else:
            self.parent.clean()
            self.parent.display(0)

    def history_for(self):
        prew_len = len(self.prew_actions)
        if prew_len > 0:
            self.parent.clean()
            self.parent.counter -= 1
            if int(self.parent.counter) < 0:
                self.parent.counter = (len(self.prew_actions) - 1)
            self.parent.display(self.prew_actions[self.parent.counter])
        else:
            self.parent.clean()
            self.parent.display(0)

    def add_to_history(self, value):
        self.history.write_file(value)

    def history_read(self):
        self.prew_actions = self.history.read_file()

    def press_null(self):
        if self.parent.flag:
            self.parent.flag = False
            self.parent.clean()
        self.parent.display(0)

    def press_one(self):
        if self.parent.flag == True:
            print("Successfully")
            self.parent.clean()
            self.parent.flag = False
        self.parent.display(1)

    def press_two(self):
        if self.parent.flag:
            self.parent.flag = False
            self.parent.clean()
        self.parent.display(2)

    def press_three(self):
        if self.parent.flag:
            self.parent.flag = False
            self.parent.clean()
        self.parent.display(3)

    def press_four(self):
        if self.parent.flag:
            self.parent.flag = False
            self.parent.clean()
        self.parent.display(4)

    def press_five(self):
        if self.parent.flag:
            self.parent.flag = False
            self.parent.clean()
        self.parent.display(5)

    def press_six(self):
        if self.parent.flag:
            self.parent.flag = False
            self.parent.clean()
        self.parent.display(6)

    def press_seven(self):
        if self.parent.flag:
            self.parent.flag = False
            self.parent.clean()
        self.parent.display(7)

    def press_eight(self):
        if self.parent.flag:
            self.parent.flag = False
            self.parent.clean()
        self.parent.display(8)

    def press_nine(self):
        if self.parent.flag:
            self.parent.flag = False
            self.parent.clean()
        self.parent.display(9)

    def calculate(self):
        value = self.parent.get()
        self.parent.flag = False
        self.parent.clean()
        self.add_to_history(value)
        self.history_clean()
        self.parent.display(math_eval(value))
