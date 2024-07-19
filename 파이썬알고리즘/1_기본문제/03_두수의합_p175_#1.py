# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

import collections
from typing import *

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = dict()  # key: num, value: index

        for index, num in enumerate(nums):
            if target - num in table:
                return [table[target - num], index]

            else:
                table[num] = index

        return []

nums =[2,7,11,15]
target = 9
print(Solution().twoSum(nums, target))
# [0, 1]