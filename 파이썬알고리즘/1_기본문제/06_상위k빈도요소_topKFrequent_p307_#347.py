# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

import collections
import heapq
from typing import *

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        q = []
        output = []

        freqs = collections.Counter(nums)

        for key, value in freqs.items():
            heapq.heappush(q, (-value, key))

        for _ in range(k):
            output.append(heapq.heappop(q)[1])

        return output

nums = [1,1,1,2,2,3]
k = 2
print(Solution().topKFrequent(nums, k))
# [1, 2]



class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(zip(*collections.Counter(nums).most_common(k)))[0]

nums = [1, 1, 1, 2, 2, 3]
k = 2
print(Solution().topKFrequent(nums, k))
# (1, 2)
