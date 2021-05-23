import numpy as np
import matplotlib.pyplot as plt


def func(x):
    return ((((4*x - 59) * x + 324) * x - 751) * x + 622) / ((((x - 14) * x + 72) * x - 151) * x + 112)

def func2(x):
    return 4 - (3 * (x**3 - 12 * x**2 + 49 * x - 58)) / (x**4 - 14 * x**3 + 72 * x**2 - 151 * x + 112)


x = [1.606]

for i in range(150):
    x.append(np.nextafter(x[-1], 2))
    x = [np.nextafter(x[0], 1)] + x

y1 = [func(val) for val in x]

y2 = [func2(val) for val in x]

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=[6, 6], dpi=300)
ax.axhline(y=np.mean(y1), color='gray', linestyle='-')
ax.scatter(range(len(x)), y1, facecolors='none', edgecolors='gray')
ax.set_ylim([8.7523765807784, 8.7523765807786])

plt.show()

