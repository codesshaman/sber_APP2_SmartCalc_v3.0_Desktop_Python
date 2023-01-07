from views.buttons_panels.buttons_views import CalcButton
from presenter.buttons_functions.operations_functions import *
def operations_panel(parent, x, y):
    "Панель математических операций"
    func = OpButtonsActions(parent)
    CalcButton("win", "(", "#ABA9A9", 3, 1, func.press_left_bracket).place(width=65, height=42, x=x + 20, y=y + 110)
    CalcButton("win", ")", "#ABA9A9", 3, 1, func.press_right_bracket).place(width=65, height=42, x=x + 95, y=y + 110)
    CalcButton("win", "%", "#ABA9A9", 3, 1, func.press_percent).place(width=65, height=42, x=x + 170, y=y + 110)
    CalcButton("win", "/", "#ABA9A9", 3, 1, func.press_division).place(width=65, height=42, x=x + 245, y=y + 110)
    CalcButton("win", "*", "#ABA9A9", 3, 1, func.press_multiplication).place(width=65, height=42, x=x + 245, y=y + 160)
    CalcButton("win", "-", "#ABA9A9", 3, 1, func.press_subtraction).place(width=65, height=42, x=x + 245, y=y + 210)
    CalcButton("win", "+", "#ABA9A9", 3, 1, func.press_addition).place(width=65, height=42, x=x + 245, y=y + 260)
    CalcButton("win", ".", "#ABA9A9", 3, 1, func.press_dot).place(width=65, height=42, x=x + 245, y=y + 310)