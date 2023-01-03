from views.buttons_views import CalcButton
from presenter.num_buttons_functions import *
def nums_pannel(x, y):
    "Панель простых чисел"
    CalcButton("win", "1", "#3b3e41", 3, 1, press_button_1).place(width=65, height=42, x=x + 20, y=y + 260)
    CalcButton("win", "2", "#3b3e41", 3, 1, press_button_2).place(width=65, height=42, x=x + 95, y=y + 260)
    CalcButton("win", "3", "#3b3e41", 3, 1, press_button_3).place(width=65, height=42, x=x + 170, y=y + 260)
    CalcButton("win", "4", "#3b3e41", 3, 1, press_button_4).place(width=65, height=42, x=x + 20, y=y + 210)
    CalcButton("win", "5", "#3b3e41", 3, 1, press_button_5).place(width=65, height=42, x=x + 95, y=y + 210)
    CalcButton("win", "6", "#3b3e41", 3, 1, press_button_6).place(width=65, height=42, x=x + 170, y=y + 210)
    CalcButton("win", "7", "#3b3e41", 3, 1, press_button_7).place(width=65, height=42, x=x + 20, y=y + 160)
    CalcButton("win", "8", "#3b3e41", 3, 1, press_button_8).place(width=65, height=42, x=x + 95, y=y + 160)
    CalcButton("win", "9", "#3b3e41", 3, 1, press_button_9).place(width=65, height=42, x=x + 170, y=y + 160)
    CalcButton("win", "0", "#3b3e41", 3, 1, press_button_0).place(width=65, height=42, x=x + 20, y=y + 310)
    CalcButton("win", "=", "#94b5f2", 3, 1, press_button_equal).place(width=140, height=42, x=x + 95, y=y + 310)