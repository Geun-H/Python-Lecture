def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


def fib2(n, l):
    for i in range(n - 1):
        l.append(l[-2] + l[-1])

    return l


l = fib2(5, [0, 1])
print(l)
