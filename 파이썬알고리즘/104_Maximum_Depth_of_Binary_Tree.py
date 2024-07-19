from typing import *
from __future__ import annotations

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        output = 0

        def dfs(node, depth):
            if not node:
                nonlocal output
                output = max(output, depth)
                return
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)

        dfs(root, 0)
        return output

root = [3,9,20,None,None,15,7]