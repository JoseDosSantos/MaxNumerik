import math
import matplotlib.pyplot as plt


def fibs(n):
    fibonacci = [1, 1]
    for i in range(n-2):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci[:n]

k = 51
fibonacci_numbers = fibs(k)

result = []
for i in range(k-1):
    result.append(abs(fibonacci_numbers[i + 1] / fibonacci_numbers[i] - (math.sqrt(5) + 1) / 2))

plt.plot(result)
plt.yscale('log')
plt.show()

