from collections import deque


def dfs(start, visited, graph):
    visited[start] = True
    print(start, end=' ')
    for i in graph[start]:
        if not visited[i]:
            dfs(i, visited, graph)


def bfs(start, visited, graph):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


n, m, start = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

print(graph)

visited = [False] * (n + 1)
dfs(start, visited, graph)
print()
visited = [False] * (n + 1)
bfs(start, visited, graph)
