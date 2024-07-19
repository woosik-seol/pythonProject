# Example 1:
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.

# Example 2:
# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]

# Example 3:
# Input: candidates = [2], target = 1
# Output: []

from typing import *

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []

        def dfs(start, path=[]):
            if sum(path) == target:     # stop 조건
                output.append(path[:])
                return

            elif sum(path) > target:    # stop 조건
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                dfs(i, path)
                path.pop()

        dfs(0, [])
        return output

candidates = [2,3,5]
target = 8
print(Solution().combinationSum(candidates, target))
# [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
