# https://www.acmicpc.net/problem/1260
# * 실버 2
"""
1. 아이디어
2. 시간복잡도
3. 자료구조
- DFS, BFS
- DFS: 스택, 재귀함수
- BFS: 큐
"""
from collections import deque
import sys

input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False for _ in range(n + 1)]
# print(graph)
# print(visited)

for i in graph:
    i.sort()


# DFS
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        # print("i: ", i)
        if not visited[i]:
            dfs(graph, i, visited)


# BFS
def bfs(graph, v, visited):
    q = deque()
    q.append(v)
    visited[v] = True
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


dfs(graph, v, visited)
print()
visited = [False for _ in range(n + 1)]
bfs(graph, v, visited)
