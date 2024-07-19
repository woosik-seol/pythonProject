# 1 2 3 5 8 13 21

# Example 1:
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
#
# Example 2:
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
#
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

# 반복문 loop

class Solution:
    def climbStairs(self, n: int) -> int:
        def climb_loop(n: int):
            if n <= 2:
                return n

            output = 0
            first_step = 1
            second_step = 2

            for i in range(3, n + 1):
                output = first_step + second_step
                first_step, second_step = second_step, output

            return output

        return climb_loop(n)

n = 4
print(Solution().climbStairs(n))
# 5


# 재귀 구조 브루트 포스

class Solution:
    def climbStairs(self, n: int) -> int:
        def climb_recur(n: int):
            if n <= 2:
                return n

            return climb_recur(n-2) + climb_recur(n-1)

        return climb_recur(n)

n = 4
print(Solution().climbStairs(n))
# 5


# 바텀-업 다이나믹 프로그래밍
# 테뷸레이션

class Solution:
    def climbStairs(self, n: int) -> int:
        table = dict()

        def climb_tabu(n: int):

            table[1] = 1
            table[2] = 2

            for i in range(3, n + 1):
                table[i] = table[i-2] + table[i-1]

            return table[n]

        return climb_tabu(n)

n = 4
print(Solution().climbStairs(n))
# 5


# 탑-다운 다이나믹 프로그래밍
# 메모이제이션

class Solution:
    def climbStairs(self, n: int) -> int:
        table = dict()

        table[1] = 1
        table[2] = 2

        def climb_memo(n: int):
            if n in table:
                return table[n]

            else:
                table[n] = climb_memo(n-2) + climb_memo(n-1)
                return table[n]

        return climb_memo(n)

n = 4
print(Solution().climbStairs(n))
# 5
