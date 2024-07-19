# https://github.com/onlybooks/python-algorithm-interview

import copy
from typing import *

print(divmod(5,3))
print(isinstance(235, Sequence))

a = 10
b = a
a += 1
print(a)
# 11
print(b)
# 10


a = [1,2,3]
b = copy.deepcopy(a)
print(b == a)

idx = 1
fruit = "Apple"
output = f"{idx}: {fruit}"
print(output)
print(type(output))

import sys

print(sys.maxsize)
print(-sys.maxsize)

a = [1,2,3,4,5,5,5,6,6]

import collections
b = collections.Counter(a)

print(b.most_common(2))
print(type(b.most_common(2)))
print(*b.most_common(2))
# print(type(*b.most_common(2)))

print(list(zip(*b.most_common(2))))

# a = [1,2,3,4,5,5,5,6,6]
# type(*a)


date_info = {'year':2020, "month":1, "day":7}
b = {**date_info, "day":None}
print(b)

a = "12345"

# print(a[2])