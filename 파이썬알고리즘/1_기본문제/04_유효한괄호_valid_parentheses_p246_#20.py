# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

import collections
from typing import *


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        table = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        for char in s:
            if char not in table:
                stack.append(char)

            else:
                if not stack or table[char] != stack.pop():
                    return False

        return not stack

s = "()[]{}"
print(Solution().isValid(s))
# True