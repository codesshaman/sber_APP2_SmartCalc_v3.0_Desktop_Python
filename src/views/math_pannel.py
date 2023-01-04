from views.buttons_views import CalcButton
from presenter.math_buttons_functions import *
def math_pannel(parent, x, y):
    "Панель сложных математических операций"
    func = MathButtonsActions(parent)
    CalcButton("win", "С", "#ABA9A9", 3, 1, func.press_clean).place(width=65, height=42, x=x + 20, y=y + 110)
    CalcButton("win", "0.3", "#ABA9A9", 3, 1, third).place(width=65, height=42, x=x + 95, y=y + 110)
    CalcButton("win", "= X", "#ABA9A9", 3, 1, x_func).place(width=65, height=42, x=x + 170, y=y + 110)
    CalcButton("win", "sin", "#ABA9A9", 3, 1, sinus).place(width=65, height=42, x=x + 20, y=y + 160)
    CalcButton("win", "asin", "#ABA9A9", 3, 1, arcsin).place(width=65, height=42, x=x + 95, y=y + 160)
    CalcButton("win", "ln", "#ABA9A9", 3, 1, ln).place(width=65, height=42, x=x + 170, y=y + 160)
    CalcButton("win", "cos", "#ABA9A9", 3, 1, cosinus).place(width=65, height=42, x=x + 20, y=y + 210)
    CalcButton("win", "acos", "#ABA9A9", 3, 1, arccos).place(width=65, height=42, x=x + 95, y=y + 210)
    CalcButton("win", "log", "#ABA9A9", 3, 1, log).place(width=65, height=42, x=x + 170, y=y + 210)
    CalcButton("win", "tan", "#ABA9A9", 3, 1, tangens).place(width=65, height=42, x=x + 20, y=y + 260)
    CalcButton("win", "atan", "#ABA9A9", 3, 1, arctan).place(width=65, height=42, x=x + 95, y=y + 260)
    CalcButton("win", "sqrt", "#ABA9A9", 3, 1, sqrt).place(width=65, height=42, x=x + 170, y=y + 260)
    CalcButton("win", "x^y", "#ABA9A9", 3, 1, exponentiation).place(width=65, height=42, x=x + 20, y=y + 310)
    CalcButton("win", "graph", "#ABA9A9", 3, 1, open_graph_button_press).place(width=140, height=42, x=x + 95, y=y + 310)