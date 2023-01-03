from views.buttons_views import CalcButton
from presenter.operations_functions import *
def operations_panel(x, y):
    "Панель математических операций"
    CalcButton("win", "(", "#ABA9A9", 3, 1, left_bracket).place(width=65, height=42, x=x + 20, y=y + 110)
    CalcButton("win", ")", "#ABA9A9", 3, 1, right_bracket).place(width=65, height=42, x=x + 95, y=y + 110)
    CalcButton("win", "%", "#ABA9A9", 3, 1, percent).place(width=65, height=42, x=x + 170, y=y + 110)
    CalcButton("win", "/", "#ABA9A9", 3, 1, division).place(width=65, height=42, x=x + 245, y=y + 110)
    CalcButton("win", "*", "#ABA9A9", 3, 1, multiplication).place(width=65, height=42, x=x + 245, y=y + 160)
    CalcButton("win", "-", "#ABA9A9", 3, 1, subtraction).place(width=65, height=42, x=x + 245, y=y + 210)
    CalcButton("win", "+", "#ABA9A9", 3, 1, addition).place(width=65, height=42, x=x + 245, y=y + 260)
    CalcButton("win", ".", "#ABA9A9", 3, 1, dot).place(width=65, height=42, x=x + 245, y=y + 310)