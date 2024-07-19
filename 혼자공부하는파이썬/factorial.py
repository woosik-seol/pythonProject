from typing import *


def factorial(n: int) -> int:
    outout = 1
    for i in range(n, 0, -1):
        outout *= i
    return outout
print(factorial(5))
# 120


def factorial_recur(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n-1)
print(factorial_recur(5))
# 120