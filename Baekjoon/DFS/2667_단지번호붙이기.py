# https://www.acmicpc.net/problem/2667
# * 실버 1
"""
1. 아이디어
- 2중 for, 값 1 && 방문X => DFS
- DFS를 통해 찾은 값을 저장 후 정렬 해서 출력

2. 시간복잡도
- DFS : O(V+E)
- V, E : N^2, 4N^2
- V+E : 5N^2 ~= N^2 ~= 625 >> 가능

3. 자료구조
- 그래프 저장 : int[][]
- 방문여부 : bool[][]
- 결과값 : int[]
"""
# todo: 전역 변수, sys 라이브러리 보기
import sys

input = sys.stdin.readline

n = int(input())
map = [list(map(int, input().strip())) for _ in range(n)]
chk = [[False] * n for _ in range(n)]
each = 0
result = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    global each
    each += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if map[nx][ny] and chk[nx][ny] == False:
                chk[nx][ny] = True
                dfs(nx, ny)


for i in range(n):
    for j in range(n):
        if map[i][j] == 1 and chk[i][j] == False:
            each = 0
            chk[i][j] = True
            dfs(i, j)
            result.append(each)

print(len(result))
result.sort()
for i in result:
    print(i)

# if __name__ == "__main__":
#     print(solution())
