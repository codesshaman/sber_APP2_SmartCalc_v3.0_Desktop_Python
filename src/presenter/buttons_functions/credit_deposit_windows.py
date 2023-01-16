class CreditDepositActions():
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

    def open_credit_calc_button_press(self):
        self.parent.open_credit()

    def open_deposit_calc_button_press(self):
        self.parent.open_depos()
