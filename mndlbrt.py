import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
from  matplotlib.animation import FuncAnimation

def is_mandel(x, y):
    c = complex(x, y)
    z = complex(0, 0)
    for i in range(10):
        z = z ** 2 + c
        if abs(z) >= 2:
            return i
    return 0

xmin, xmax, xn = -2, 0, 1000
ymin, ymax, yn = -1, 1, 1000

z = np.zeros(xn * yn)
for i in range(xn * yn):
    iy, ix = divmod(i, xn)
    x = xmin + ix * (xmax - xmin) / xn
    y = ymin + iy * (ymax - ymin) / yn
    z[i] = is_mandel(x, y)

z = z.reshape((xn, yn))

plt.matshow(z)

plt.show()



