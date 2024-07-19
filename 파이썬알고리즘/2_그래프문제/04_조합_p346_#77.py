# Example 1:
# Input: n = 4, k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
# Explanation: There are 4 choose 2 = 6 total combinations.
# Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

# Example 2:
# Input: n = 1, k = 1
# Output: [[1]]
# Explanation: There is 1 choose 1 = 1 total combination.

from typing import *

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [num for num in range(1, n + 1)]
        output = []

        def dfs(depth, start, path=[]):
            if len(path) == k:
                output.append(path[:])
                return

            for i in range(start, depth + n - k + 1):
                path.append(nums[i])
                dfs(depth + 1, i + 1, path)
                path.pop()

        dfs(0, 0, [])
        return output

n = 4
k = 2
print(Solution().combine(n, k))
# [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
