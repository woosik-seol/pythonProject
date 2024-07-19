# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]

# Example 3:
# Input: nums = [1]
# Output: [[1]]

from typing import *

# 가장 심플한 버전
# 실제로는 제일 빠름
# 37 ms

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []

        def dfs(path = []):
            if len(path) == len(nums):  # stop 조건
                output.append(path[:])
                return
            for num in nums:
                if num not in path:
                    dfs(path + [num])

        dfs([])
        return output

nums = [1,2,3]
print(Solution().permute(nums))
# [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

# 공간 복잡도 개선
# 40ms

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []

        def dfs(path = []):
            if len(path) == len(nums):  # stop 조건
                output.append(path[:])
                return
            for num in nums:
                if num not in path:
                    path.append(num)
                    dfs(path)
                    path.pop()

        dfs([])
        return output

nums = [1,2,3]
print(Solution().permute(nums))
# [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

# 시간 복잡도 개선 (조건문 없앰)
# 46 ms
# 실제로는 제일 느림

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        candidates = nums[:]

        def dfs(path=[]):
            if len(path) == len(nums):  # stop 조건
                output.append(path[:])
                return

            for i, num in enumerate(candidates):
                candidates.pop(i)
                path.append(num)
                dfs(path)
                path.pop()
                candidates.insert(i, num)

        dfs([])
        return output

nums = [1,2,3]
print(Solution().permute(nums))
# [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
