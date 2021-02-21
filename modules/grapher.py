import matplotlib.pyplot as plt
import numpy
import os
import shutil


class Grapher:
    def __init__(self):
        self._clean_directory()

    def _clean_directory(self):
        try:
            shutil.rmtree("figure")
        except FileNotFoundError:
            pass
        os.mkdir("figure")

    def scatter_plot(self, x, x_label, y, y_label):
        fig = plt.figure()
        plt.scatter(x, y)
        plt.ylabel(f"{y_label}")
        plt.xlabel(f"{x_label}")
        fig.savefig(
            f"./figure/{x_label}-{y_label}.png")
        print(f"{x_label}-{y_label}.png create")

    def scatter_plot_with_corrcoef(self, x, x_label, y, y_label):
        if abs(numpy.corrcoef(x, y)[0][1]) > 0.5:
            self.scatter_plot(x, x_label, y, y_label)
        else:
            print(f"{x_label}-{y_label}low level corrcoef !! ")

    def line_graph(self, x, x_label, y, y_label):
        fig = plt.figure()
        plt.plot(x, y)
        plt.ylabel(f"{y_label}")
        plt.xlabel(f"{x_label}")
        fig.savefig(
            f"./figure/{x_label}-{y_label}.png")
        print(f"{x_label}-{y_label}.png create")
