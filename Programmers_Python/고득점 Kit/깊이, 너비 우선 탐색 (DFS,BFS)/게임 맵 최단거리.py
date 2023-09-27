# https://school.programmers.co.kr/learn/courses/30/lessons/1844
# 최단거리 구하기 => BFS

"""
나의 풀이
"""
from collections import deque


def dfs(x, y, maps):
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 맵에서 벗어난 경우
            if nx < 0 or ny < 0 or nx >= len(maps) or ny >= len(maps[0]):
                continue
            # 이동 못하는 경우
            if maps[nx][ny] == 0:
                continue
            # 이동 가능한 경우
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
    return maps[len(maps) - 1][len(maps[0]) - 1]


def solution(maps):
    answer = 0
    answer = dfs(0, 0, maps)
    if answer == 1:  # 이동할 수 없는 경우
        answer = -1
    return answer


"""
다른 풀이
# 참고: https://jiwonlog.tistory.com/9
"""
# from collections import deque
#
#
# def solution(maps):
#     n = len(maps)
#     m = len(maps[0])
#     visited = [[False] * m for _ in range(n)]
#     q = deque()
#     q.append((0, 0))
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
#     visited[0][0] = True
#     while q:
#         y, x = q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] == 1:
#                 if not visited[ny][nx]:
#                     visited[ny][nx] = True
#                     q.append((ny, nx))
#                     maps[ny][nx] = maps[y][x] + 1
#     if maps[n - 1][m - 1] == 1:
#         return -1
#     else:
#         return maps[n - 1][m - 1]


if __name__ == '__main__':
    print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
    print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]))
