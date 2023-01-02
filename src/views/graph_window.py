from tkinter import *
from model.debug import check_debug

debug = check_debug()

class GraphWindow:
    "Класс окна графиков"
    def __init__(self, parent, width, height, title="SmartCalc_v3", resizable=(0, 0), icon=None):
        super().__init__()
        if debug:
            print("Инициализация окна графиков")
        self.gwin = Toplevel(parent)
        self.gwin.title(title)
        self.gwin.geometry(f"{width}x{height}+200+200")
        self.gwin.resizable(resizable[0], resizable[1])
        self.gwin.configure(bg='gray')
