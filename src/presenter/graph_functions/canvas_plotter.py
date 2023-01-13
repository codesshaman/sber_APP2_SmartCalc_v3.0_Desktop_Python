import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

from PIL import Image, ImageTk
from model import plotutil as plu

# Глобальная переменная для проверки,
# Существует ли построенный график
plotted = False


def Plot(fx, xpoints, canvas, line_style, file_path):

    global plotted
    if fx:
        plu.plot(fx, xpoints, 'X-axis', 'Y-axis', True, line_style, file_path)
        image = Image.open(".temp/generated_plot.png").resize(
            (canvas.winfo_width(), canvas.winfo_height()))
        gif1 = ImageTk.PhotoImage(image, Image.ANTIALIAS)
        canvas.create_image(0, 0, image=gif1, anchor=NW)
        canvas.gif1 = gif1
        plotted = True
    else:
        canvas.delete(ALL)

    sys.stdout.flush()
