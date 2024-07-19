# 깊이 우선 탐색
# Depth  First Search (DFS)
# - 스택이나 재귀

# 너비 우선 탐색
# Breath First Search (BFS)
# - 큐

graph = {
    1: [2,3,4],
    2: [5],
    3: [5],
    4: [],
    5: [6,7],
    6: [],
    7: [3],
}

# DFS 재귀

output = []
def recursive_dfs(v):
    output.append(v)
    for w in graph[v]:
        if w not in output:     # stop 조건
            recursive_dfs(w)

recursive_dfs(1)
print(output)
# [1, 2, 5, 6, 7, 3, 4]


# DFS 재귀
# Stop 조건을 명백하게

output = []
def recursive_dfs(v):
    if not v or v in output:    # stop 조건
        return None

    output.append(v)
    for w in graph[v]:
        recursive_dfs(w)

recursive_dfs(1)
print(output)
# [1, 2, 5, 6, 7, 3, 4]


# 스택

def iterative_dfs(start_v):
    output = []
    stack = [start_v]

    while stack:
        v = stack.pop()
        if v not in output:     # stop 조건
            output.append(v)
            for w in graph[v]:
                stack.append(w)

    return output

print(iterative_dfs(1))
# [1, 4, 3, 5, 7, 6, 2]
# 스텍으로 구현했기 때문에
# 끝 노드가 먼저 삽입


# 큐

def iterative_bfs(start_v):
    output = []
    queue = [start_v]

    while queue:
        v = queue.pop(0)        # 스택 소스코드와 이 부분만 다름
        if v not in output:     # stop 조건
            output.append(v)
            for w in graph[v]:
                queue.append(w)

    return output

print(iterative_bfs(1))
# [1, 2, 3, 4, 5, 6, 7]







