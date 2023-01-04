class NumButtonsActions():
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        # self.num = num

    def press_null(self):
        self.parent.display(0)

    def press_one(self):
        self.parent.display(1)

    def press_two(self):
        self.parent.display(2)

    def press_three(self):
        self.parent.display(3)

    def press_four(self):
        self.parent.display(4)

    def press_five(self):
        self.parent.display(5)

    def press_six(self):
        self.parent.display(6)

    def press_seven(self):
        self.parent.display(7)

    def press_eight(self):
        self.parent.display(8)

    def press_nine(self):
        self.parent.display(9)

    def calculate(self):
        value = self.parent.get()
        self.parent.clear()
        self.parent.display(eval(value))
