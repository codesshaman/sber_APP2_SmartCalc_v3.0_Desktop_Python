import tkinter as tk
from PIL import Image, ImageTk

class DeposWindow():
    def __init__(self, parent):
        self.dep = tk.Toplevel(parent)
        self.dep.title("Deposit Calc")
        self.dep.geometry("555x200+200+644")
        self.dep.resizable(0, 0)
        self.dep.configure(bg='gray', pady=10)
        # Обозначения полей ввода
        input_one = tk.Label(self.dep, text="Годовая процентная ставка", bg='gray', padx=10, pady=2)
        input_one.grid(row=1, column=1, sticky=tk.W, padx=10, pady=2)
        input_two = tk.Label(self.dep, text="Количество лет", bg='gray', padx=10, pady=2)
        input_two.grid(row=2, column=1, sticky=tk.W, padx=10, pady=2)
        input_three = tk.Label(self.dep, text="Сумма вклада", bg='gray', padx=10, pady=2)
        input_three.grid(row=3, column=1, sticky=tk.W, padx=10, pady=2)
        input_four = tk.Label(self.dep, text="Профит", bg='gray', padx=10, pady=2)
        input_four.grid(row=4, column=1, sticky=tk.W, padx=10, pady=2)
        input_five = tk.Label(self.dep, text="Общая сумма", bg='gray', padx=10, pady=2)
        input_five.grid(row=5, column=1, sticky=tk.W, padx=10, pady=2)
        # Поля для ввода
        self.varOne = tk.StringVar()
        one_entry = tk.Entry(self.dep,
                                  textvariable=self.varOne,
                                  bg="#b0b0b0", justify=tk.LEFT)
        one_entry.grid(row=1, column=2)
        self.varTwo = tk.StringVar()
        two_entry = tk.Entry(self.dep,
                                    textvariable=self.varTwo,
                                    bg="#b0b0b0", justify=tk.LEFT)
        two_entry.grid(row=2, column=2)
        self.varThree = tk.StringVar()
        three_entry = tk.Entry(self.dep,
                                  textvariable=self.varThree,
                                  bg="#b0b0b0", justify=tk.LEFT)
        three_entry.grid(row=3, column=2)
        # Выходные значения:
        self.varFour = tk.StringVar()
        four_entry = tk.Label(self.dep,
                                     textvariable=self.varFour,
                                     justify=tk.LEFT)
        four_entry.grid(row=4, column=2, sticky=tk.E)
        self.varTotal = tk.StringVar()
        five_entry = tk.Label(self.dep,
                                   textvariable=self.varTotal,
                                   justify=tk.LEFT)
        five_entry.grid(row=5, column=2, sticky=tk.E)
        btnCalcPayment = tk.Button(self.dep,
                                   text="Рассчитать",
                                   command=self.calcPayment)
        btnCalcPayment.grid(row=6, column=2, sticky=tk.E)
        # Изображение
        canvas = tk.Label(self.dep, width=90, height=90)
        canvas.place(relx=0.73, rely=0.07, relheight=0.72, relwidth=0.25)
        img = tk.PhotoImage(file="views/img/depos.png")
        img = img.subsample(4, 4)
        canvas.image = img
        canvas['image'] = canvas.image

    def destroy(self):
        self.dep.destroy()

    def calcPayment(self):
        ProfitCalc = self.TotalProfit(
            float(self.varThree.get()),
            float(self.varOne.get()),
            int(self.varTwo.get()))

        self.varFour.set(format(ProfitCalc, '10.2f'))
        totalPayment = float(self.varFour.get()) * int(self.varTwo.get()) + float(self.varThree.get())

        self.varTotal.set(format(totalPayment, '10.2f'))

    # Вычисление ежемесячного платежа
    def TotalProfit(self, varThree, varOne, varTwo):
        profit = ((varThree * varOne * varTwo)/100)
        return profit
    def run(self):
        window = self.dep
        window.mainloop()
