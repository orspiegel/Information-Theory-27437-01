import matplotlib.pyplot as plt
import numpy
import numpy as np
import random
import pandas as pd

# Generate data on commute times.
import pylab as pl
def hist():
    histogram = []

    for i in range(10000):
        # Gaussian distribution array:
        #   1st argument = mean -> 0,
        #   2nd arg = standard deviation -> 1,
        #   3rd arg = length of the random array -> 50.
        random_array = np.random.normal(0.0, 1.0, 50)
        # multiplying all the values of the array
        mult_vector = np.prod(random_array)
        # adding to the histogram vector
        histogram.append(mult_vector)

    # --------------NOT SEMILOG--------------------#
    # plt.hist(histogram, bins=[-0.003,-0.002,-0.001,0,0.001,0.002,0.003,0.004])
    # plt.title("histogram")
    # plt.show()

    #--------------WHY NOT SEMILOG--------------------#
    pl.hist(histogram, bins=np.logspace(np.log10(0.1), np.log10(1.0), 10))
    pl.gca().set_xscale("log")
    pl.show()

if __name__ == '__main__':
    hist()

