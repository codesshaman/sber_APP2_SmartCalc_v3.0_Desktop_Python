from tkinter import *

class CalcButton(Button):
    "Класс кнопки"
    def __init__(self, parent, text, width, height):
        super().__init__(text=text, width=width, height=height, justify=LEFT)
        self.parent = parent
        self._text = text
        self._width = width
        self._height = height

    def text(self, _text):
        text = _text

    def width(self, _width):
        width = _width

    def height(self, _height):
        height = _height
