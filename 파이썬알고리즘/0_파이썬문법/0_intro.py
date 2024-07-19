# https://github.com/onlybooks/algorithm-interview

# p34
# 언어 차원에서 제공하는 라이브러리
# 리트코드에서 별도로 import 하지 않아도 바로 사용 가능

import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

d: Deque = collections.deque()

import pprint # pretty printer
pprint.pprint(locals())


# p64
from dataclasses import dataclass
@dataclass
class Rectangle:
    width: int
    height: int

    def area(self):
        return self.width * self.height

rect = Rectangle(3,4)
print(rect.area())
# 12
