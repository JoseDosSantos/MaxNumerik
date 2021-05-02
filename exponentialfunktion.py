import numpy as np

def exp(x):
    fak = 1
    exponential = 1
    k = 1
    last_val = 1
    while True:
        exponential = exponential * x
        fak = fak * k
        new_val = last_val + exponential / fak
        if new_val == last_val:
            break
        else:
            last_val = new_val
            k += 1
    return new_val

for x in range(-19, 20, 2):
    e = exp(x)
    print(f"x={x} \t{abs(np.exp(x) - e ) / abs(np.exp(x))}")
