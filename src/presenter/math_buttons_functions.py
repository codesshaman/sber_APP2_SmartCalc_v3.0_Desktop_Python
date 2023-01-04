class MathButtonsActions():
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        # self.num = num

    def press_clean(self):
        self.parent.clear()

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


def open_graph_button_press():
    print("Open Graph")

def clean():
    print("clean")

def third():
    print("0,3")

def x_func():
    print("= X")

def sinus():
    print("sinus")

def arcsin():
    print("arcsinus")

def ln():
    print("natural logariphm")

def cosinus():
    print("cosinus")

def arccos():
    print("arccos")

def log():
    print("logariphm")

def tangens():
    print("tangens")

def arctan():
    print("arctangens")

def sqrt():
    print("sqrt")

def exponentiation():
    print("exponentiation")