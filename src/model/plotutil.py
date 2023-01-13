import os
import re
import matplotlib.pyplot as plt
import matplotlib.style as mplstyle
from matplotlib import colors as mcolors


def create_y_values(func, xvals):

    # Create function ordinate values
    yvals = []
    for x in xvals:
        # try:
        yval = eval(func)
        yvals.append(yval)
        # except Exception:
        #     raise InvalidFunctionException('Function is improper, unbale to evaluate function at x = ' + str(x))

    return yvals

def plot(func, xpoints, xlabel, ylabel, gui, line_style, file_path):
    mplstyle.use('default')
    xvals = xpoints
    yvals = create_y_values(func, xvals)
    plt.plot(xvals, yvals, color='red', linewidth=2.0, linestyle=line_style)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(r'$ ' + func + ' $')
    if file_path != "":
        plt.savefig(file_path)
    plt.grid(True)
    if not gui:
        plt.show()
    else:
        if not os.path.exists('.temp/'):
            os.mkdir('.temp/')
        plt.savefig(".temp/generated_plot.png")
    plt.cla()
    plt.clf()