# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
#
# Example 2:
# Input: strs = [""]
# Output: [[""]]
#
# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]

import collections
from typing import *

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = collections.defaultdict(list)
        output = []

        for word in strs:
            table[''.join(sorted(word))].append(word)

        for value in table.values():
            output.append(value)

        return output

strs = ["eat","tea","tan","ate","nat","bat"]
print(Solution().groupAnagrams(strs))
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]