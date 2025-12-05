import numpy as np


def parab_func(a, b, N):
    x = np.linspace(a, b, N)
    out = np.zeros((N, 2))
    out[:, 0] = x
    out[:, 1] = x**2
    return out

    
y = parab_func(-1, 1, 10)
print(y)
