import sys
import tkinter as tk
from PIL import Image, ImageTk
from views import canvas_creator as plu

# Глобальная переменная для проверки,
# Существует ли построенный график
plotted = False


def Plot(fx, xpoints, canvas, line_style, file_path):
    "Функция отрисовки графика"
    global plotted
    if fx:
        plu.plot(fx, xpoints, 'X-axis', 'Y-axis', True, line_style, file_path)
        image = Image.open(".temp/generated_plot.png").resize(
            (canvas.winfo_width(), canvas.winfo_height()))
        gif1 = ImageTk.PhotoImage(image, Image.ANTIALIAS)
        canvas.create_image(0, 0, image=gif1, anchor=tk.NW)
        canvas.gif1 = gif1
        plotted = True
    else:
        canvas.delete(tk.ALL)

    sys.stdout.flush()
