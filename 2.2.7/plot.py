from matplotlib import pyplot as plt
import approximate
import numpy as np


class Plot:

    def __init__(self, title='My plot', number=1, figsize=(5.5, 4)):
        """
        :param title: Title of plot
        :param number: Count of figures on plot
        :param figsize: Size of figure (screen ratio)
        """

        self.title = title
        self.fig = plt.figure(number, figsize=figsize)

    @staticmethod
    def dots(x, y, x_err=0, y_err=0, label=''):
        plt.errorbar(x, y, fmt=".r", xerr=x_err, yerr=y_err, label=label)

    @staticmethod
    def plot(x, y, label=''):
        k, b = approximate.lessSquaresMethod(x, y)

        plt.plot(x, k * x + np.array(b), label=label)

    def complete(self, x, y, x_err=0, y_err=0, label=''):
        self.plot(x, y)
        self.dots(x, y, x_err=x_err, y_err=y_err)

    def show(self, xlabel='', ylable='', ylog=False, xlog=False):
        plt.grid(linestyle='--', which='major')
        plt.grid(linestyle=':', which='minor')
        plt.title(self.title)
        plt.xlabel(xlabel)
        plt.ylabel(ylable)

        if ylog:
            plt.yscale("log")
        if xlog:
            plt.xscale("log")

        # plt.savefig(self.title)
        plt.show()

    def save(self, path=''):
        plt.savefig(path + self.title)
