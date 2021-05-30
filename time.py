import timeit

setup = """
import numpy as np
n = 1000
A = np.random.rand(n, n)
B = np.zeros_like(A)
b = np.random.rand(n)
"""

def time(setup, stmt, text):
    print(f"Time elapsed for "
          f"{text}: {timeit.timeit(setup=setup, stmt=stmt, number=1):.4f}")


# Aufgabe 1)
stmt = "A@b"
time(setup, stmt, stmt)

stmt = "A@A"
time(setup, stmt, stmt)

stmt = "np.linalg.inv(A) @ b"
time(setup, stmt, stmt)

stmt = "np.linalg.solve(A, b)"
time(setup, stmt, stmt)


# Aufgabe 2a)
stmt = """
for row in range(n):
    for col in range(n):
        val = A[row, col]
        if val >= 0.5:
            B[row, col] = 4 * (val - 0.5) ** 2
"""
time(setup, stmt, 'For Loop')


# Aufgabe 2b)
stmt = """
def B_func(psi):
    if psi >= 0.5:
        return 4 * (psi - 0.5) ** 2
    return 0
B_vectorized = np.vectorize(B_func)
B_vectorized(A)
"""
time(setup, stmt, 'B with np.vectorize')


# Aufgabe 2c)
stmt = """
4 * (A - 0.5)**2 * (A >= 0.5)
"""
time(setup, stmt, 'B with custom vectorization')


# Aufgabe 3)
stmt = """
for row in range(n):
    for col in range(n):
        B[row, col] = np.sum(A[row, :] * A[:, col])
"""
time(setup, stmt, 'Custom matrix multiplication')

