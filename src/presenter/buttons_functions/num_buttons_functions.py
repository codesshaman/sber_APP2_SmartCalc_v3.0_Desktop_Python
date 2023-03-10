from model import calculate as calc
from presenter.buttons_functions import logs
from presenter.buttons_functions import history


class NumButtonsActions():
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.logs = logs.CalcLogs()
        self.counter = self.parent.counter
        self.history = history.CalcHistory()
        self.prew_actions = self.history.read_file()

    def counter_clean(self):
        self.parent.counter = 0

    def history_clean(self):
        self.parent.counter = 0
        self.history.del_history()

    def print_last(self):
        prew_len = len(self.prew_actions)
        if prew_len > 0:
            self.parent.display(self.prew_actions[self.parent.counter])
        else:
            self.parent.flag = True
            self.parent.display(0)

    def history_back(self):
        prew_len = len(self.prew_actions)
        self.parent.flag = True
        if prew_len > 0:
            self.parent.clean()
            self.parent.counter += 1
            if int(self.parent.counter) >= len(self.prew_actions):
                self.counter_clean()
            self.parent.display(self.prew_actions[self.parent.counter])
        else:
            self.parent.clean()
            self.parent.display(0)

    def history_for(self):
        self.parent.flag = True
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
        if len(str(value)) > 0:
            self.history.write_file(value)

    def add_to_logs(self, value):
        if len(str(value)) > 0:
            self.logs.write_file(value)

    def history_read(self):
        self.prew_actions = self.history.read_file()

    def press_null(self):
        if self.parent.flag:
            self.parent.flag = False
            self.parent.clean()
        self.parent.display(0)

    def press_one(self):
        if self.parent.flag:
            self.parent.flag = False
            self.parent.clean()
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

    def dot_null_check(self, value):
        if type(value) == float:
            if str(value).find(".") != -1:
                res = str(value).split('.')
                if res[1] == "0":
                    return int(res[0])
                else:
                    return value
        else:
            return value

    def calculate(self):
        value = self.parent.get()
        self.parent.flag = False
        self.parent.clean()
        self.counter_clean()
        result = calc.math_eval(value)
        # print(type(result))
        result = self.dot_null_check(result)
        # print(type(result))
        self.parent.display(result)
        self.add_to_logs(value)
        self.add_to_history(result)
