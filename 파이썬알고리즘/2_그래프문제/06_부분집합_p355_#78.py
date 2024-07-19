# Example 1:
#
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:
#
# Input: nums = [0]
# Output: [[],[0]]

from typing import *


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []

        def dfs(depth, path=[]):
            if depth == len(nums):  # stop 조건
                output.append(path[:])
                return

            dfs(depth + 1, path)

            path.append(nums[depth])
            dfs(depth + 1, path)
            path.pop()

        dfs(0, [])
        return output

nums = [1,2,3]
print(Solution().subsets(nums))
# [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]
