# Example 1:
# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3

# Example 2:
# Input: jewels = "z", stones = "ZZ"
# Output: 0

import collections
from typing import *


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        table = collections.defaultdict(int)

        for stone in stones:
            table[stone] += 1

        counter = 0
        for jewel in jewels:
            counter += table[jewel]

        return counter

jewels = "aA"
stones = "aAAbbbb"
print(Solution().numJewelsInStones(jewels, stones))
# 3


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = collections.Counter(stones)

        counter = 0
        for jewel in jewels:
            counter += freqs[jewel]

        return counter

jewels = "aA"
stones = "aAAbbbb"
print(Solution().numJewelsInStones(jewels, stones))
# 3
