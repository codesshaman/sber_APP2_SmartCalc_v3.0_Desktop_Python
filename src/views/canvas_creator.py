import os
import matplotlib.pyplot as plt
import matplotlib.style as mplstyle


def create_y_values(func, xvals):
    yvals = []
    for x in xvals:
        yval = eval(func)
        yvals.append(yval)
    return yvals


def plot(func, xpoints, xlabel, ylabel, gui, line_style, file_path):
    # print("Plotting")
    mplstyle.use('default')
    xvals = xpoints
    yvals = create_y_values(func, xvals)
    plt.plot(xvals, yvals, linestyle=line_style)
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
