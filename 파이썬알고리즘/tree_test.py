# https://github.com/onlybooks/python-algorithm-interview

from typing import *
from dataclasses import dataclass
from __future__ import annotations

@dataclass
class Node:
    value: int = 0
    left: Optional[Node] = None
    right: Optional[Node] = None

root = Node()


# tree_node = TreeNode()