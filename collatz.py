def collatz(a0):
    an = a0
    n = 0

    while (an > 1):
        if an % 2 == 0:
            an = an // 2
        else:
            an = 3 * an + 1
        n = n + 1
        # print(an)
    # print(n)
    return n

highest_n = 0
highest_value = 0

for i in range(401):
    n = collatz(i)
    if n > highest_n:
        highest_n = n
        highest_value = i

print(f"Value: {highest_value} took {highest_n} iterations.")