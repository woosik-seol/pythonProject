# 숫자가 주어졌을 때
# 전화번호로 조합 가능한
# 모든 문자를 출력하라

# Example 1:
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

# Example 2:
# Input: digits = ""
# Output: []

# Example 3:
# Input: digits = "2"
# Output: ["a","b","c"]

from typing import *

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        table = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        output = []

        def dfs(depth, path):
            if len(path) == len(digits):    # stop 조건
                output.append(path)
                return None

            for char in table[digits[depth]]:   # 이 부분 때문에 depth 가 유용.
                dfs(depth + 1, path + char)     # 다른 소스코드들은 depth 가 필요치 않을 수 있음.

        dfs(0, "")
        return output

digits = "23"
print(Solution().letterCombinations(digits))
# ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
