def fibs_max(max_value):
    fibonacci = [1, 1]
    while fibonacci[-1] < max_value:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci[:-1]

def get_zeckendorf(n):
    fib_nums = fibs_max(n)
    fib_sum = 0
    zeck_nums = []
    while fib_sum != n:
        if fib_nums[-1] + fib_sum <= n:
            fib_sum += fib_nums[-1]
            zeck_nums.append(fib_nums[-1])
            fib_nums = fib_nums[:-2]
        else:
            fib_nums = fib_nums[:-1]
    return zeck_nums

n = 143
print(n, get_zeckendorf(n))

n = 10**10
print(n, get_zeckendorf(n))
