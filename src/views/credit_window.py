import tkinter as tk
from presenter import config_functions


class CreditWindow():
    def __init__(self, parent):
        self.cred = tk.Toplevel(parent)
        self.cred.title("Credit Calc")
        self.cred.geometry("555x200+200+644")
        self.cred.resizable(0, 0)
        self.cred.configure(bg='gray', pady=10)
        # Обозначения полей ввода
        input_rate = tk.Label(self.cred, text="Годовая процентная ставка", bg='gray', padx=10, pady=2)
        input_rate.grid(row=1, column=1, sticky=tk.W, padx=10, pady=2)
        input_years = tk.Label(self.cred, text="Количество лет", bg='gray', padx=10, pady=2)
        input_years.grid(row=2, column=1, sticky=tk.W, padx=10, pady=2)
        input_sum = tk.Label(self.cred, text="Сумма кредита", bg='gray', padx=10, pady=2)
        input_sum.grid(row=3, column=1, sticky=tk.W, padx=10, pady=2)
        input_month = tk.Label(self.cred, text="Ежемесячный платёж", bg='gray', padx=10, pady=2)
        input_month.grid(row=4, column=1, sticky=tk.W, padx=10, pady=2)
        input_total = tk.Label(self.cred, text="Общая сумма платежа", bg='gray', padx=10, pady=2)
        input_total.grid(row=5, column=1, sticky=tk.W, padx=10, pady=2)
        # Поля для ввода
        self.annualInterestRate = tk.StringVar()
        ent_rate_entry = tk.Entry(self.cred,
                                  textvariable=self.annualInterestRate,
                                  bg="#b0b0b0", justify=tk.LEFT)
        ent_rate_entry.grid(row=1, column=2)
        self.numberOfYears = tk.StringVar()
        ent_num_of_years = tk.Entry(self.cred,
                                    textvariable=self.numberOfYears,
                                    bg="#b0b0b0", justify=tk.LEFT)
        ent_num_of_years.grid(row=2, column=2)
        self.loanAmountVar = tk.StringVar()
        ent_rate_entry = tk.Entry(self.cred,
                                  textvariable=self.loanAmountVar,
                                  bg="#b0b0b0", justify=tk.LEFT)
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
        # Изображение
        canvas = tk.Label(self.cred, width=90, height=90)
        canvas.place(relx=0.73, rely=0.07, relheight=0.72, relwidth=0.25)
        img = tk.PhotoImage(file="views/img/credit.png")
        img = img.subsample(4, 4)
        canvas.image = img
        canvas['image'] = canvas.image

    def destroy(self):
        self.cred.destroy()

    def calcPayment(self):
        monthlyPayment = self.getMonthlyPayment(
            float(self.loanAmountVar.get()),
            float(self.annualInterestRate.get()) / 1200,
            int(self.numberOfYears.get()))

        self.montlyPaymentVar.set(format(monthlyPayment, '10.2f'))
        totalPayment = float(self.montlyPaymentVar.get()) * 12 \
            * int(self.numberOfYears.get())

        self.totalPaymentVar.set(format(totalPayment, '10.2f'))

    # Вычисление ежемесячного платежа
    def getMonthlyPayment(self, loanAmount, monthlyInterestRate, numberOfYears):
        monthlyPayment = loanAmount * monthlyInterestRate / \
            (1 - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
        return monthlyPayment
    def run(self):
        window = self.cred
        window.mainloop()
