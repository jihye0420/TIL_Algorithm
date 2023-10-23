# https://school.programmers.co.kr/learn/courses/30/lessons/43162
"""
# * 나만의 풀이 => DFS로 해결
테스트 케이스는 다 맞음
정확성: 15.4
합계: 15.4 / 100.0
# ! 어느 부분에서 논리적 오류가 있는 것인지 파악이 안됨...!
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
DFS
BFS
"""


def BFS(n, computers, com, visited):
    visited[com] = True
    queue = []
    queue.append(com)
    while len(queue) != 0:
        com = queue.pop(0)
        visited[com] = True
        for connect in range(n):
            if connect != com and computers[com][connect] == 1:
                if visited[connect] == False:
                    queue.append(connect)


def DFS(n, computers, com, visited):
    visited[com] = True
    for connect in range(n):
        if connect != com and computers[com][connect] == 1:  # 연결된 컴퓨터
            if visited[connect] == False:
                DFS(n, computers, connect, visited)


def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    for com in range(n):
        if visited[com] == False:
            # * DFS 풀이
            DFS(n, computers, com, visited)
            answer += 1  # DFS로 최대한 컴퓨터들을 방문하고 빠져나오게 되면 그것이 하나의 네트워크.
            # * BFS 풀이
            # BFS(n, computers, com, visited)
            # answer += 1
    return answer


if __name__ == '__main__':
    print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
    print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
