import numpy as np


def func(A, n):
    if n == 0:
        return np.identity(arr.shape[0], dtype=int)
    return func(A, n//2) @ func(A, n//2) @ ((n % 2) * arr + (1 - n % 2) * np.identity(arr.shape[0], dtype=arr.dtype))


arr = np.array([[1, 1], [1, 0]], dtype=np.object)
n = 100


# print(np.linalg.matrix_power(arr, n))
print(func(arr, n))

