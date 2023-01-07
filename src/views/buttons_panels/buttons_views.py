from tkinter import *

class CalcButton(Button):
    "Класс кнопки"
    def __init__(self, parent, text, bg, width, height, func):
        super().__init__(text=text, bg=bg, width=width, height=height, command=func, justify=RIGHT)
        self.parent = parent
        self._text = text
        self._bg = bg
        self._width = width
        self._height = height
        self._command = func

    def text(self, _text):
        text = _text

    def width(self, _width):
        width = _width

    def height(self, _height):
        height = _height
