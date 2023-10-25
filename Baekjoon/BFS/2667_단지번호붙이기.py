# https://www.acmicpc.net/problem/2667
# * 실버 1
"""
1. 아이디어
- bfs
2. 시간복잡도
3. 자료구조
- 2차원 그래프: int[][]
- Queue(bfs)
- 방문 체크: check
"""
from collections import deque


def bfs(graph, check, i, j):
    q = deque()
    q.append((i, j))
    check[i][j] = True
    rs = 1
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1 and check[nx][ny] == False:
                    rs += 1
                    check[nx][ny] = True
                    q.append((nx, ny))
    return rs


def solution():
    count = 0
    home_num_list = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1 and check[i][j] == False:
                # 방문했는지 확인
                check[i][j] = True
                # 전체 단지수 +1
                count += 1
                # home_num_list 추가
                home_num_list.append(bfs(graph, check, i, j))
    home_num_list.sort()
    print(count)
    for i in home_num_list:
        print(i)
    return


if __name__ == '__main__':
    n = int(input())
    graph = [[] for _ in range(n)]
    # graph = [] * n # ! 이것도 이상함
    # print(graph)
    for i in range(n):
        # graph[i].append(list(map(int, input())))  # ! 이러면 안됌
        graph[i] = list(map(int, input()))

    # print(graph)
    check = [[False] * n for _ in range(n)]
    # print(check)
    solution()
