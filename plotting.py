"""Module for plotting data from a file"""

import numpy
import matplotlib.pyplot as plt

def load_data(filename):
    """Read in multiple column data from file"""
    return numpy.loadtxt(filename, unpack=True)


def plot_file_contents(filename):
    x, y = load_data(filename)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title('Results')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    fig.show()

