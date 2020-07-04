import matplotlib.pyplot as plt
import numpy as np


def lap(x, b):
    x = np.fabs(x)
    return 1 / (2 * b) * np.e**(-x/b)


def draw_scatter():
    x_list = np.linspace(-30, 30, 1000)
    y_list_1 = [lap(x, 9) for x in x_list]
    y_list_2 = [lap(x, 99) for x in x_list]
    plt.plot(x_list, y_list_1, label="a")
    plt.plot(x_list, y_list_2, label="b")
    plt.legend(['n=10', "n=100"])
    plt.show()


epsilon=1
k = 100
p1 = np.e / (np.e**epsilon + k - 1)
p2 = 1 / (np.e**epsilon + k - 1)
print(p1, p2)