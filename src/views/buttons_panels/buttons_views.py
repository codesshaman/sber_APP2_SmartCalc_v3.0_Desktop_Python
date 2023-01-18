import tkinter as tk


class CalcButton(tk.Button):
    "Класс кнопки"
    def __init__(self, parent, text, bg, fg, width, height, func):
        super().__init__(text=text, bg=bg, fg=fg, width=width,
                         height=height, command=func,
                         justify=tk.RIGHT)
        self.parent = parent
        self._text = text
        self._bg = bg
        self._width = width
        self._height = height
        self._command = func
