from __future__ import annotations

from typing import *
from dataclasses import dataclass, field


def digging(camel_source: str):
    keys = []

    i = 0
    while i < len(camel_source):
        if camel_source[i].islower():
            i += 1

        else:
            if i + 1 < len(camel_source) and camel_source[i + 1].islower():
                keys.append(camel_source[i:i+2])
                i += 2
            else:
                keys.append(camel_source[i])
                i += 1

    keys.append(camel_source)

    return keys


# ['Fo', 'Fe', 'Ba', 'A', 'ForceFeedBackA']

def init_keys_values(list_source: List[str]):
    output = []

    for camel in list_source:
        keys = digging(camel)
        output.append(keys)
    return output

@dataclass
class Node:
    key: str
    values: List[str] = field(default_factory=list)
    children: List[Node] = field(default_factory=list)

def insert(node: Node):
    pass


# def insert_key_value(node, key_value: List[str]):
#     if len(key_value) > 1:
#         index = 0
#         for child in node.children:
#             if child.key == key_value[0]:
#                 break
#             index += 1
#         if index == len(node.children):
#             node.children.append(Node(key_value[0]))
#         insert_key_value(node.children[index], key_value[1:])
#     else:
#         node.values.append(key_value[0])

def insert_key_value(node, key_value: List[str]):
    if not key_value:
        return

    # node.values.append(key_value[-1])

    if len(key_value) > 1:
        for child in node.children:
            if child.key == key_value[0]:
                insert_key_value(child, key_value[1:])
                return
            # else:
        new_node = Node(key_value[0])
        node.children.append(new_node)
        insert_key_value(new_node, key_value[1:])
    else:
        node.values.append(key_value[0])

# @dataclass
# class Node:
#     key: str
#     children: List[Node] = field(default_factory=list)

def insert(node: Node):
    pass

# def insert_key_value(node, key_value: List[str]):
#     if len(key_value) > 1:
#         index = 0
#         for child in node.children:
#             if child.key == key_value[0]:
#                 break
#             index += 1
#         if index == len(node.children):
#             node.children.append(Node(key_value[0]))
#         insert_key_value(node.children[index], key_value[1:])
#     else:
#         node.key = key_value[0]
def init_tree(root: Node, keys_values: List[List[str]]):
    for key_value in keys_values:
        insert_key_value(root, key_value[:])


        # print(key_value)


keys_values = init_keys_values(["Apple", "FooBarTest", "FrameBuffer", "FrameBufferA",
                     "FrameBufferB", "ForceFeedBack", "ForceFeedBackA", "ForceFeedBackAb", "G"])

# print(keys_values)

root = Node("")

init_tree(root, keys_values)
print(root)

# output = []

def searchNode(source: str, node: Node) -> List[Node]:
    path: Node = []

    def dfs(source: str, node: Node):

        if not source:
            if node:
                path.append(node)
            return

        if len(source) >= 2 and source[1].islower():
            key = source[:2]

            for child in node.children:
                if child.key == key:
                    dfs(source[2:], child)
        else:
            key = source[0]

            for child in node.children:
                if child.key[0] == key:
                    dfs(source[1:], child)

    dfs(source, node)
    return path


def traverseNode(node: Node) -> List[str]:
    path = []

    def dfs(node: Node):
        if not node:
            return
        if node.values:
            path.extend(node.values[:])
        for child in node.children:
            dfs(child)
    dfs(node)
    return path

def traverse(nodes) -> List[str]:
    path = []

    for node in nodes:
        path_for_node = traverseNode(node)
        if path_for_node:
            path.extend(path_for_node)
    return path

outout_search = traverse(searchNode("G", root))
print(outout_search)


outout_search = traverse(searchNode("FrBA", root))
print(outout_search)

outout_search = traverse(searchNode("FoFeBaAb", root))
print(outout_search)

outout_search = traverse(searchNode("FoFBAb", root))
print(outout_search)


outout_search = traverse(searchNode("FB", root))
print(outout_search)

print(searchNode("FB", root))

outout_search = traverse(searchNode("FoB", root))
print(outout_search)


#
# print(dictionary)
#
# search("FrBA")
# search("FrBA")
