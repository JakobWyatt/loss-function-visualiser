import sys
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def multidimensional_plot(plot_data):
    fig = plt.figure()
    ax = Axes3D(fig)
    plt.show()

def plot_from_file(file_path):
    """
    Get data from a .npy file and plot the data using multidimensional_plot.
    """
    file_data = np.load(file_path)
    multidimensional_plot(file_data)

if __package__ == '__main__':
    if sys.argv.len() < 2:
        print("Please provide the file name of the data to be visualised.")
    else:
        plot_from_file(sys.argv[1])
