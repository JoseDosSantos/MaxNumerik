import numpy as np
import matplotlib.pyplot as plt


def p_norm(x, p):
    y = np.abs(x)
    y = np.power(y, p)
    y = np.sum(y, axis=1)
    y = np.power(y, 1.0/p)
    return y[:, np.newaxis]


p = 3

alpha = np.linspace(0, 2 * np.pi, 999)
x = np.array([np.cos(alpha), np.sin(alpha)]).T
y = x / p_norm(x, p)


fig, ax = plt.subplots(nrows=1, ncols=1, figsize=[6, 6], dpi=300)
ax.plot(x[:, 0], x[:, 1])
ax.plot(y[:, 0], y[:, 1])
plt.show()