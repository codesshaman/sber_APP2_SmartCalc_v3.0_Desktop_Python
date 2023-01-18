from presenter import config_functions
from views.buttons_panels.buttons_views import CalcButton
from presenter.buttons_functions.credit_deposit_windows \
    import CreditDepositActions


def credit_deposit_buttons(parent):
    "Кнопки открытия кредитного и депозитного калькулятора"
    conf = config_functions.CalcConfig()
    func = CreditDepositActions(parent)
    fg = conf.get_fontcolor()
    CalcButton("win", "Credit Calc", "#272727", fg, 3,
               1, func.open_credit_calc_button_press)\
        .place(width=140, height=42, x=95, y=365)
    CalcButton("win", "Deposit Calc", "#272727", fg, 3,
               1, func.open_deposit_calc_button_press)\
        .place(width=140, height=42, x=320, y=365)
