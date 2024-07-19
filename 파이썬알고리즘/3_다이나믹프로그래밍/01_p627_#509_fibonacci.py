# 1 1 2 3 5 8 13

# Example 1:
# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

# Example 2:
# Input: n = 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

# Example 3:
# Input: n = 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

# 반복문 loop

class Solution:
    def fib(self, n: int) -> int:
        def fibonacci_loop(n: int):
            if n <= 1:
                return n

            outout = 0
            first_value = 0
            second_value = 1

            for i in range(2, n + 1):
                outout = first_value + second_value
                first_value, second_value = second_value, outout

            return outout

        return fibonacci_loop(n)

n = 4
print(Solution().fib(n))
# 3


# 재귀 구조 브루트 포스

class Solution:
    def fib(self, n: int) -> int:
        def fibonacci_recur(n: int):
            if n <= 1:
                return n

            return fibonacci_recur(n-2) + fibonacci_recur(n-1)

        return fibonacci_recur(n)

n = 4
print(Solution().fib(n))
# 3


# 바텀-업
# 테뷸레이션

class Solution:
    def fib(self, n: int) -> int:
        table = dict()

        def fibonacci_tabu(n: int):

            table[0] = 0
            table[1] = 1

            for i in range(2, n + 1):
                table[i] = table[i-2] + table[i-1]

            return table[n]

        return fibonacci_tabu(n)

n = 4
print(Solution().fib(n))
# 3


# 탑-다운
# 메모이제이션

class Solution:
    def fib(self, n: int) -> int:
        table = dict()

        def fibonacci_memo(n: int):
            if n <= 1:
                return n

            elif n in table:
                return table[n]

            else:
                table[n] = fibonacci_memo(n-2) + fibonacci_memo(n-1)
                return table[n]

        return fibonacci_memo(n)

n = 4
print(Solution().fib(n))
# 3
