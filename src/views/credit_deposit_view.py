from views.buttons_views import CalcButton
from presenter.credit_deposit_windows import *

def credit_deposit_buttons():
    "Кнопки открытия кредитного и депозитного калькулятора"
    CalcButton("win", "Credit Calc", "#272727", 3, 1,
               open_credit_calc_button_press).place(width=140, height=42, x=95, y=365)
    CalcButton("win", "Deposit Calc", "#272727", 3, 1,
               open_deposit_calc_button_press).place(width=140, height=42, x=320, y=365)