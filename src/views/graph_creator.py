import sys
import tkinter as tk
from PIL import Image, ImageTk
from views import canvas_creator as plu

plotted = False


def Plot(fx, xpoints, color_name, canvas, line_style, file_path):
    "Построение графика по осям координат"
    global plotted
    if fx:
        plu.plot(fx, xpoints, color_name,
                 'ось X', 'ось Y', True, line_style, file_path)
        image = Image.open(".temp/generated_plot.png").resize(
            (canvas.winfo_width(), canvas.winfo_height()))
        gif1 = ImageTk.PhotoImage(image, Image.ANTIALIAS)
        canvas.create_image(0, 0, image=gif1, anchor=tk.NW)
        canvas.gif1 = gif1
        plotted = True
    else:
        canvas.delete(tk.ALL)

    sys.stdout.flush()


def Plot_line(arrays, color_name, canvas, line_style, file_path):
    "Рисование линии по осям координат"
    global plotted
    if arrays:
        plu.plot_line(arrays, color_name,
                      'ось X', 'ось Y', True, line_style, file_path)
        image = Image.open(".temp/generated_plot.png").resize(
            (canvas.winfo_width(), canvas.winfo_height()))
        gif1 = ImageTk.PhotoImage(image, Image.ANTIALIAS)
        canvas.create_image(0, 0, image=gif1, anchor=tk.NW)
        canvas.gif1 = gif1
        plotted = True
    else:
        canvas.delete(tk.ALL)
    sys.stdout.flush()
