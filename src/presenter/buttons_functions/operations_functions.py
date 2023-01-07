class OpButtonsActions():
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

    def press_left_bracket(self):
        self.parent.display("(")

    def press_right_bracket(self):
        self.parent.display(")")

    def press_percent(self):
        self.parent.display("%")

    def press_division(self):
        self.parent.display("/")

    def press_multiplication(self):
        self.parent.display("*")

    def press_subtraction(self):
        self.parent.display("-")

    def press_addition(self):
        self.parent.display("+")

    def press_dot(self):
        self.parent.display(".")
