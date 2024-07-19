# 1 1 2 3 5 8 13

def fibonacci_loop(n: int):
    if n <= 2:
        return 1

    outout = 0
    first_value = 1
    second_value = 1

    for i in range(3, n+1):
        outout = first_value + second_value
        first_value, second_value = second_value, outout

    return outout
print(fibonacci_loop(8))
# 21




def fibonacci_recur(n: int):
    if n <= 2:
        return 1
    return fibonacci_recur(n-1) + fibonacci_recur(n-2)
print(fibonacci_recur(8))
# 21


table = dict()

def fibonacci(n: int):
    if n <= 2:
        return 1
    elif n in table:
        return table[n]
    else:
        outout = fibonacci(n-1) + fibonacci(n-2)
        table[n] = outout
        return outout

print(fibonacci(8))
# 21

print(table)
# {3: 2, 4: 3, 5: 5, 6: 8, 7: 13, 8: 21}