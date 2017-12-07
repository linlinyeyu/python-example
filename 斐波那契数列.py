#!/usr/bin/python3


def fib(n):
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a


def fiblist(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(n - 1):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs


print(fib(10))
print(fiblist(10))
