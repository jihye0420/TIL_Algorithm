# https://www.acmicpc.net/problem/11660
"""
나만의 풀이
"""
import sys

input = sys.stdin.readline  # 입력의 개수가 많은 경우

n, m = map(int, input().split())

"""
2차원 배열 초기화 및 선언
"""
# # 2차원 배열 선언
# x = n
# y = n
# z = [[0] * y for _ in range(x)]
# print(z)
#
# # 2차원 리스트 맵 정보 입력받기
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input().split())))
# print(graph)

"""
2차원 배열, 합 배열 선언
"""
A = [[0] * (n + 1)]
D = [[0] * (n + 1) for _ in range(n + 1)]
# print(A)
# print(D)

for i in range(1, n + 1):
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)
# print(A)

# 합배열 D[X][Y] 구하기
# D[X][Y] = 원본 배열의 (0,0)~(x,y)까지의 사각형 영역 안에 있는 수의 합
# D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        D[i][j] = D[i][j - 1] + D[i - 1][j] - D[i - 1][j - 1] + A[i][j]
# print(D)

# (x1, y1) ~ (x2, y2) 구간의 합 구하기
# 구간의 합 구하기
# result = D[x2][y2] - D[x1 - 1][y2] - D[x2][y1 - 1] + D[x1 - 1][y1 - 1]
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = D[x2][y2] - D[x1 - 1][y2] - D[x2][y1 - 1] + D[x1 - 1][y1 - 1]
    print(result)
