# 정렬

s = ['2 A', '1 B', '4 C', '1 A']

def func(x):
    return x.split()[1], x.split()[0]

s.sort(key=func)
print(s)
# ['1 A', '2 A', '1 B', '4 C']

s.sort(key=lambda x: (x.split()[0], x.split()[1]))
print(s)
# ['1 A', '1 B', '2 A', '4 C']

a = [2, 5, 1, 9, 7]
print(sorted(a))
# [1, 2, 5, 7, 9]
print(a)
# [2, 5, 1, 9, 7]

b = 'zbdaf'
print(sorted(b))
['a', 'b', 'd', 'f', 'z']

print(''.join(sorted(b)))
# abdfz

a = ['cde', 'zfc', 'abc']
print(sorted(a, key=lambda s: (s[-1], s[0])))
# ['abc', 'zfc', 'cde']


# 최댓값과 최솟값

import sys
max_int = sys.maxsize
min_int = -sys.maxsize

max_float = float("inf")
min_float = float("-inf")