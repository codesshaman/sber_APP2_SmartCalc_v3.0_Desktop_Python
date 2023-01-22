import sys
import tkinter as tk
from PIL import Image, ImageTk
from views import canvas_creator as plu
from presenter import config_functions

# Глобальная переменная для проверки,
# Существует ли построенный график
plotted = False


def Plot(fx, xpoints, canvas, line_style, file_path):
    "Функция отрисовки графика"
    print("Start Plot")
    cf = config_functions.CalcConfig()
    if cf.get_graph_window() == "0":
        gui = True
    elif cf.get_graph_window() == "1":
        gui = False
    global plotted
    if fx:
        plu.plot(fx, xpoints, 'X-axis', 'Y-axis', gui, line_style, file_path)
        image = Image.open(".temp/generated_plot.png").resize(
            (canvas.winfo_width(), canvas.winfo_height()))
        gif1 = ImageTk.PhotoImage(image, Image.ANTIALIAS)
        canvas.create_image(0, 0, image=gif1, anchor=tk.NW)
        canvas.gif1 = gif1
        plotted = True
        print("-----Stop Plot")
    else:
        canvas.delete(tk.ALL)

    sys.stdout.flush()
