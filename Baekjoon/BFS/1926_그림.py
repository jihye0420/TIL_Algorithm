# https://www.acmicpc.net/problem/1926
# * 실버 1
"""
1. 아이디어
- 2중 for문 => 값 1 && 방문 x => BFS
- BFS 돌면서 그림 개수 +1, 최댓값을 갱신

2. 시간복잡도
- BFS : O(V+E)

3. 자료구조
- 그래프 전체 지도 : int[][]
- 방문 : bool[][]
- Queue(BFS)
"""

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
map = [list(map(int, input().split())) for i in range(n)]
chk = [[False] * m for _ in range(n)]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    rs = 1
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if map[nx][ny] == 1 and chk[nx][ny] == False:
                    rs += 1
                    chk[nx][ny] = True
                    q.append((nx, ny))
    return rs  # 각 1씩 모여 있는 개수 그림을 구성하는 넓이


cnt = 0  # 전체 그림 개수
maxv = 0  # 최댓값
for i in range(n):
    for j in range(m):
        if map[i][j] == 1 and chk[i][j] == False:
            # 방문 완료
            chk[i][j] = True
            # 전체 그림 개수를 +1
            cnt += 1
            # BFS => 그림 크기를 구해주고, 최댓값을 갱신
            maxv = max(maxv, bfs(i, j))

print(cnt)
print(maxv)
