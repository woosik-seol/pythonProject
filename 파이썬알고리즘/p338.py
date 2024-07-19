from typing import *

# def letterCombinations(digits: str) -> List[str]:
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

output  = []
digits = "23"

def dfs(depth, path):
    if len(path) == len(digits):
        output.append(path)
        return
    for char in table[digits[depth]]:
        dfs(depth + 1, path + char)

dfs(0, "")
print(output)



