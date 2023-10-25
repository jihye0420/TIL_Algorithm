# https://www.acmicpc.net/problem/2178
# * 실버 1
"""
1. 아이디어
- bfs
- 각 그래프에서 지나간 자리를 +1
2. 시간복잡도
3. 자료구조
- 2차원 그래프: int[][]
- Queue(BFS)
"""
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, input()))

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(graph, x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    q.append((nx, ny))
                    graph[nx][ny] = graph[x][y] + 1
    return graph[n - 1][m - 1]


print(bfs(graph, 0, 0))
