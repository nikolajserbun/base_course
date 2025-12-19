import matplotlib.pyplot as plt
import numpy as np
x1 = int(input())
x2 = int(input())
k = int(input())
S = int(input())
def grafic_plotter(x1, x2):
    x = np.arange(x1, x2, S)
    y = k / x
    plt.plot(x, y, label = 'my giperbola')
    plt.xlabel('coord - x')
    plt.xlabel('coord - y')

    plt.savefig('fig_2.png')
if __name__ == '__main__':
    grafic_plotter()