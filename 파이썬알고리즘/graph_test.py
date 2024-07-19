import copy
from typing import *

graph = {
    1: [2,3,4],
    2: [5],
    3: [5],
    4: [],
    5: [6,7],
    6: [],
    7: [3],
}


def recursive_dfs(v: int, path: List[int] = []) -> None:
    if v in path:
        return None

    path.append(v)
    for w in graph[v]:
        recursive_dfs(w, path)

path = []
recursive_dfs(1, path)
print(path)

path = []

def recursive_dfs(v: int) -> None:
    if v in path:
        return None

    path.append(v)
    for w in graph[v]:
        recursive_dfs(w)

recursive_dfs(1)
print(path)




graph = {
    1: [2,3,4],
    2: [5],
    3: [5],
    4: [],
    5: [6,7],
    6: [],
    7: [3],
}


def iterative_stack_dfs(start_v: int) -> List[int]:
    path = []
    stack = [start_v]

    while stack:
        v = stack.pop()
        if v not in path:
            path.append(v)
            for w in graph[v]:
                stack.append(w)

    return path

print(iterative_stack_dfs(1))


import collections

graph = {
    1: [2,3,4],
    2: [5],
    3: [5],
    4: [],
    5: [6,7],
    6: [],
    7: [3],
}

def iterative_queue_bfs(start_v) -> List[int]:
    path: List[int] = []

    q = collections.deque()
    q.append(start_v)

    while q:
        v = q.popleft()
        if v not in path:
            path.append(v)
            for w in graph[v]:
                q.append(w)

    return path

print(iterative_queue_bfs(1))



