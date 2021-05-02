import math

# b)
i = 0
s = 0
while True:
    s += (-1)**i / (2 * i + 1)
    if abs(math.pi - 4 * s) <= 10**-5:
        break
    i += 1

# print(i)

# c)

def get_arctan(x, M, N):
    s = 0
    for n in range(N+1):
        s += (-1) ** n * math.floor(M / (x ** (2 * n + 1) * (2 * n + 1)))
    return s / M

M = 10**20
N = 10

print(math.pi)
print(4 * (4 * get_arctan(5, M, N) - get_arctan(239, M, N)))