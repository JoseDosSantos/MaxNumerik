import math
import matplotlib.pyplot as plt

start = 10**6
step = 10**4
stop = 10**8

def func(b):
    return (-b + math.sqrt(b**2 - 1)) * (-b - math.sqrt(b**2 - 1))

x = range(start, stop, step)
vals = [func(b) for b in x]

plt.plot(x, vals)
plt.xscale('log')
plt.show()
