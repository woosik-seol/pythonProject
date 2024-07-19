# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5

# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4

from typing import *
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = []
        output = 0

        for num in nums:
            heapq.heappush(q, -num)

        for _ in range(k):
            output = -heapq.heappop(q)

        return output


nums = [3,2,1,5,6,4]
k = 2
print(Solution().findKthLargest(nums, k))
# 5