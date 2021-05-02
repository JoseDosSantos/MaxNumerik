import numpy as np
import matplotlib.pyplot as plt

def partial_sum(t):
    n = 10**6
    result = 0
    for i in range(1, n+1):
        result += float(format(1 / i, f".{t}g"))
    return result

for t in [3, 4, 5, 6]:
    print(f"t={t}:\t {partial_sum(t)}")
print(f"t=64:\t {partial_sum(64)}")

