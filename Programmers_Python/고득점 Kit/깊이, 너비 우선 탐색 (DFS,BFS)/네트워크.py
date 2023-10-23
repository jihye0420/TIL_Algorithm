# https://school.programmers.co.kr/learn/courses/30/lessons/43162
"""
# * 나만의 풀이 => DFS로 해결
테스트 케이스는 다 맞음
정확성: 15.4
합계: 15.4 / 100.0
"""

# def dfs(x, y, computers, n):
#     if x < 0 or y < 0 or x >= n or y >= n:
#         return False
#     if computers[x][y] == 1:
#         # 방문처리
#         computers[x][y] = 0
#         # 상하좌우 모두 재귀적으로 호출!
#         dfs(x - 1, y, computers, n)
#         dfs(x + 1, y, computers, n)
#         dfs(x, y - 1, computers, n)
#         dfs(x, y + 1, computers, n)
#         return True
#     return False
#
#
# def solution(n, computers):
#     answer = 0
#     # visited = [0] * n
#     # dfs(computers, 0, visited)
#     for i in range(n):
#         for j in range(n):
#             if dfs(i, j, computers, n) == True:
#                 answer += 1
#     return answer

"""
# ! 다른 풀이
"""


def solution(n, computers):
    def DFS(i):
        visited[i] = 1
        for a in range(n):
            if computers[i][a] and not visited[a]:
                DFS(a)

    answer = 0
    visited = [0 for i in range(len(computers))]
    for i in range(n):
        if not visited[i]:
            DFS(i)
            answer += 1

    return answer


if __name__ == '__main__':
    print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
    print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
