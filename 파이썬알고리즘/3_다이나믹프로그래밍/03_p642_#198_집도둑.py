# Example 1:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.

# Example 2:
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.

from typing import *

# 반복문 loop

class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_loop(nums: List[int]):
            if len(nums) <= 2:
                return max(nums)

            output = 0
            max_left_left = nums[0]
            max_left = max(nums[0], nums[1])

            for i in range(2, len(nums)):
                output = max(max_left_left + nums[i], max_left)
                max_left_left, max_left = max_left, output

            return output
        return rob_loop(nums)

nums = [2,7,9,3,1]
print(Solution().rob(nums))
# 5


# 재귀 구조 브루트 포스

class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_recur(nums: List[int]):
            if len(nums) <= 2:
                return max(nums)

            return max(rob_recur(nums[:-2]) + nums[-1], rob_recur(nums[:-1]))

        return rob_recur(nums)

nums = [2,7,9,3,1]
print(Solution().rob(nums))
# 5


# 바텀-업 다이나믹 프로그래밍
# 테뷸레이션

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        table = dict()

        def rob_tabu(nums):
            table[0] = nums[0]
            table[1] = max(nums[0], nums[1])

            for i in range(2, len(nums)):
                table[i] = max(table[i-2] + nums[i], table[i-1])

            return table[len(nums)-1]

        return rob_tabu(nums)

nums = [2,7,9,3,1]
print(Solution().rob(nums))
# 5


# 탑-다운 다이나믹 프로그래밍
# 메모이제이션

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        table = dict()
        table[0] = nums[0]
        table[1] = max(nums[0], nums[1])

        def rob_memo(index):
            if index in table:
                return table[index]

            else:
                table[index] = max(rob_memo(index-2) + nums[index], rob_memo(index-1))
                return table[index]

        return rob_memo(len(nums) - 1)

nums = [2,7,9,3,1]
print(Solution().rob(nums))
# 5
