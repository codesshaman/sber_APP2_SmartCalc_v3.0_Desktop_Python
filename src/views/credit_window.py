import tkinter as tk


class CreditWindow():
    def __init__(self):
        self.cred = tk.Tk()
        self.cred.title("Credit Calc")
        self.cred.geometry("577x200")
        # Обозначения полей ввода
        input_rate = tk.Label(self.cred, text="Годовая процентная ставка")
        input_rate.grid(row=1, column=1, sticky=tk.W)
        input_years = tk.Label(self.cred, text="Количество лет")
        input_years.grid(row=2, column=1, sticky=tk.W)
        input_sum = tk.Label(self.cred, text="Сумма кредита")
        input_sum.grid(row=3, column=1, sticky=tk.W)
        input_month = tk.Label(self.cred, text="Ежемесячный платёж")
        input_month.grid(row=4, column=1, sticky=tk.W)
        input_total = tk.Label(self.cred, text="Общая сумма платежа")
        input_total.grid(row=5, column=1, sticky=tk.W)
        # Поля для ввода
        self.annualInterestRate = tk.StringVar()
        ent_rate_entry = tk.Entry(self.cred,
                                  textvariable=self.annualInterestRate,
                                  justify=tk.LEFT)
        ent_rate_entry.grid(row=1, column=2)
        self.numberOfYears = tk.StringVar()
        ent_num_of_years = tk.Entry(self.cred,
                                    textvariable=self.numberOfYears,
                                    justify=tk.LEFT)
        ent_num_of_years.grid(row=2, column=2)
        self.loanAmountVar = tk.StringVar()
        ent_rate_entry = tk.Entry(self.cred,
                                  textvariable=self.loanAmountVar,
                                  justify=tk.LEFT)
        ent_rate_entry.grid(row=3, column=2)
        # Выходные значения:
        self.montlyPaymentVar = tk.StringVar()
        ent_monthly_entry = tk.Label(self.cred,
                                     textvariable=self.montlyPaymentVar,
                                     justify=tk.LEFT)
        ent_monthly_entry.grid(row=4, column=2, sticky=tk.E)
        self.totalPaymentVar = tk.StringVar()
        ent_total_entry = tk.Label(self.cred,
                                   textvariable=self.totalPaymentVar,
                                   justify=tk.LEFT)
        ent_total_entry.grid(row=5, column=2, sticky=tk.E)
        btnCalcPayment = tk.Button(self.cred,
                                   text="Рассчитать",
                                   command=self.calcPayment)
        btnCalcPayment.grid(row=6, column=2, sticky=tk.E)

    def calcPayment(self):
        print("calcPayment")

    def payment(self, loanAmount, monthlyInterestRate, numberOfYears):
        monthlyPayment = loanAmount * monthlyInterestRate / \
                         (1 - 1 / (1 + monthlyInterestRate) ** \
                         (numberOfYears * 12))
        return monthlyPayment
    def run(self):
        window = self.cred
        window.mainloop()

window = CreditWindow()
window.run()

#https://github.com/BekBrace/loan-calculator/blob/master/loan_calculator.py
