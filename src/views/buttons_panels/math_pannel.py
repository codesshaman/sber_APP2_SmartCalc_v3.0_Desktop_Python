from presenter import config_functions
from views.buttons_panels.buttons_views import CalcButton
from presenter.buttons_functions.math_buttons_functions \
    import MathButtonsActions


def math_pannel(parent, x, y):
    "Панель сложных математических операций"
    conf = config_functions.CalcConfig()
    func = MathButtonsActions(parent)
    fg = conf.get_fontcolor()
    CalcButton("win", "С", "#ABA9A9", fg, 3, 1, func.press_clean_history)\
        .place(width=65, height=42, x=x + 20, y=y + 110)
    CalcButton("win", "<=", "#ABA9A9", fg, 3, 1, func.clean_last)\
        .place(width=65, height=42, x=x + 95, y=y + 110)
    CalcButton("win", "π", "#ABA9A9", fg, 3, 1, func.press_pi)\
        .place(width=65, height=42, x=x + 170, y=y + 110)
    CalcButton("win", "sin", "#ABA9A9", fg, 3, 1, func.press_sin)\
        .place(width=65, height=42, x=x + 20, y=y + 160)
    CalcButton("win", "asin", "#ABA9A9", fg, 3, 1, func.press_asin)\
        .place(width=65, height=42, x=x + 95, y=y + 160)
    CalcButton("win", "ln", "#ABA9A9", fg, 3, 1, func.press_ln)\
        .place(width=65, height=42, x=x + 170, y=y + 160)
    CalcButton("win", "cos", "#ABA9A9", fg, 3, 1, func.press_cos)\
        .place(width=65, height=42, x=x + 20, y=y + 210)
    CalcButton("win", "acos", "#ABA9A9", fg, 3, 1, func.press_acos)\
        .place(width=65, height=42, x=x + 95, y=y + 210)
    CalcButton("win", "log", "#ABA9A9", fg, 3, 1, func.press_log)\
        .place(width=65, height=42, x=x + 170, y=y + 210)
    CalcButton("win", "tan", "#ABA9A9", fg, 3, 1, func.press_tan)\
        .place(width=65, height=42, x=x + 20, y=y + 260)
    CalcButton("win", "atan", "#ABA9A9", fg, 3, 1, func.press_atan)\
        .place(width=65, height=42, x=x + 95, y=y + 260)
    CalcButton("win", "sqrt", "#ABA9A9", fg, 3, 1, func.press_sqrt)\
        .place(width=65, height=42, x=x + 170, y=y + 260)
    CalcButton("win", "X", "#ABA9A9", fg, 3, 1, func.x_func)\
        .place(width=65, height=42, x=x + 20, y=y + 310)
    CalcButton("win", "graph", "#ABA9A9", fg, 3, 1, func.open_graph)\
        .place(width=140, height=42, x=x + 95, y=y + 310)
