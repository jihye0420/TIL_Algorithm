# https://www.acmicpc.net/problem/2178
from collections import deque


def bfs(n, m, graph):
    queue = deque()
    queue.append((0, 0))

    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n - 1][m - 1]


def solution():
    n, m = map(int, input().split())
    # 2차원 배열 선언
    graph = [[0] * m for _ in range(n)]
    for i in range(n):
        graph[i] = list(map(int, input()))

    # print(graph)

    print(bfs(n, m, graph))
    return


solution()
