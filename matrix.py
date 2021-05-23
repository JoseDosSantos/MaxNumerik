import numpy as np
import matplotlib.pyplot as plt

n = 10
arr = np.zeros((n, n))
np.fill_diagonal(arr, 0.5)
np.fill_diagonal(arr[1:], 1)

def func(arr):
    arr_mult = arr.T @ arr
    max_eig = max(np.linalg.eig(arr_mult)[0])
    return np.sqrt(max_eig)

print(func(arr))

arr2 = np.linalg.matrix_power(arr, 50)
print(func(arr2))

print(np.power(func(arr), 50))


f_k = [np.power(func(arr), k) for k in range(0, 51)]
f_k2 = [func(np.linalg.matrix_power(arr, k)) for k in range(0, 51)]

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=[8, 4], dpi=300)


ax[0].plot(f_k)
ax[0].set_yscale('log')
ax[0].set_title('Approximiert')

ax[1].plot(f_k2)
ax[1].set_yscale('log')
ax[1].set_title('linalg matrix power')

plt.show()





