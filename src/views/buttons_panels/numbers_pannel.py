from views.buttons_panels.buttons_views import CalcButton
# from main import window
# from views.main_window import CalcWindow
from presenter.buttons_functions.num_buttons_functions import *

def nums_pannel(parent, x, y):
    "Панель простых чисел"
    func = NumButtonsActions(parent)
    CalcButton("win", "1", "#3b3e41", 3, 1, func.press_one).place(width=65, height=42, x=x + 20, y=y + 260)
    CalcButton("win", "2", "#3b3e41", 3, 1, func.press_two).place(width=65, height=42, x=x + 95, y=y + 260)
    CalcButton("win", "3", "#3b3e41", 3, 1, func.press_three).place(width=65, height=42, x=x + 170, y=y + 260)
    CalcButton("win", "4", "#3b3e41", 3, 1, func.press_four).place(width=65, height=42, x=x + 20, y=y + 210)
    CalcButton("win", "5", "#3b3e41", 3, 1, func.press_five).place(width=65, height=42, x=x + 95, y=y + 210)
    CalcButton("win", "6", "#3b3e41", 3, 1, func.press_six).place(width=65, height=42, x=x + 170, y=y + 210)
    CalcButton("win", "7", "#3b3e41", 3, 1, func.press_seven).place(width=65, height=42, x=x + 20, y=y + 160)
    CalcButton("win", "8", "#3b3e41", 3, 1, func.press_eight).place(width=65, height=42, x=x + 95, y=y + 160)
    CalcButton("win", "9", "#3b3e41", 3, 1, func.press_nine).place(width=65, height=42, x=x + 170, y=y + 160)
    CalcButton("win", "0", "#3b3e41", 3, 1, func.press_null).place(width=65, height=42, x=x + 20, y=y + 310)
    CalcButton("win", "=", "#94b5f2", 3, 1, func.calculate).place(width=140, height=42, x=x + 95, y=y + 310)