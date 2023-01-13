from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

from views.graphic_window import gui_support

darktext = '#808080'
_bgcolorlight = '#b0b0b0'
_fgcolorlight = '#000000'
_lightwindowbackground = '#7e7e7e'

w = None

def destroy_app():
    global root
    root.destroy()
    exit(0)

class new_graph:
    def __init__(self, parent, top=None):
        "Графическое отображение"
        self.top = Toplevel(parent)
        top.geometry("600x460+408+120")
        top.resizable(0, 0)
        top.title("График функции")

        self.theme = 'light'
        self.line_style = '-'
        self.file_path = ''
        root.configure(background=_lightwindowbackground)
        self.pvalue1=''
        self.pvaluetemp=''
        # Минимальный X
        self.x_lower = 0
        # Maкстмальный X
        self.x_upper = 100
        # Длинна шага
        self.stepsize = 1
        # Цвет графика
        self.color_input = '#FF0000'
        # *****************************
        # *****************************
        # *****************************
        self.graph_canvas = Canvas(top)
        self.graph_canvas.place(relx=0.04, rely=0.05, relheight=0.70, relwidth=0.69)
        self.graph_canvas.configure(background=_bgcolorlight)
        self.graph_canvas.configure(borderwidth="2")
        self.graph_canvas.configure(relief=RIDGE)
        self.graph_canvas.configure(selectbackground="#c4c4c4")
        self.graph_canvas.configure(width=394)
        # self.graph_canvas.bind('<Configure>', self.resize_plot)
        # *****************************
        # *****************************
        # *****************************

        self.fx = Entry(top)
        self.fx.place(relx=0.11, rely=0.82, relheight=0.05, relwidth=0.53)
        self.fx.configure(background=_bgcolorlight)
        self.fx.configure(font="TkFixedFont")
        self.fx.configure(width=296)
        # self.fx.bind('<Return>', lambda x : self.toPlot(self.radiovar.get()))
        self.fx.configure(fg=_fgcolorlight)
        self.fx.configure(insertbackground=_fgcolorlight)
        self.Label3 = Label(top)
        self.Label3.place(relx=0.04, rely=0.82, height=18, width=35)
        self.Label3.configure(text='''f(x)=''')
        self.Label3.configure(fg=_fgcolorlight)
        self.Label3.configure(background=_lightwindowbackground)
        self.bt_plot = Button(top)
        self.bt_plot.place(relx=0.67, rely=0.85, height=26, width=47)
        self.bt_plot.configure(activebackground=darktext)    
        self.bt_plot.configure(cursor="left_ptr")
        self.bt_plot.configure(text='''Plot''')
        self.bt_plot.configure(width=47, background=_bgcolorlight, fg=_fgcolorlight)
        self.bt_plot.configure(command=lambda : (self.toPlot()))
    
    def toPlot(self):
        "Метод отрисовки графика"
        gui_support.Plot(self.fx.get(), range(1, 100, 1), '#FF0000',
                         self.graph_canvas, self.line_style, self.file_path)

def vp_start_gui(parent):
    "Функция запуска интерфейса"
    global val, w, root
    root = parent
    new_graph(root)
    root.protocol('WM_DELETE_WINDOW', destroy_app)
    root.mainloop()

if __name__ == "__main__":
    vp_start_gui()
