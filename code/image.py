import matplotlib.pyplot as plt
import numpy as np

def draw_function(coe):
    x = np.arange(-10, 10, 0.1)
    coe = [float(c) for c in coe]
    y = x*0
    degree = len(coe) - 1
    for i in range(degree):
        y += coe[i] * x ** (degree - i)
    plt.axhline(0)
    plt.axvline(0)
    plt.plot(x, y)
    plt.grid(True)
    plt.show()