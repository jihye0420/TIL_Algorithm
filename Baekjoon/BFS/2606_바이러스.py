# https://www.acmicpc.net/problem/2606
# * 실버 3
"""
1. 아이디어
- bfs
2. 시간복잡도
3. 자료구조
- 2차원 그래프: int[][]
- visited: int[0] * n
- Queue(bfs)
"""
from collections import deque


def bfs(graph, v, visited):
    q = deque([v])
    visited[v] = True
    rs = 0
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                rs += 1
    return rs


def solution():
    n = int(input())
    m = int(input())
    graph = [[] for _ in range(n + 1)]
    # graph = [[0]] * (n + 1) # !이렇게 작성하면 안됨.
    # print(graph)

    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in graph:
        i.sort()
    print(graph)
    visited = [0] * (n + 1)
    result = 0
    result = bfs(graph, 1, visited)
    print()
    return result


if __name__ == '__main__':
    print(solution())
