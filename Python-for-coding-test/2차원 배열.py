n = 3
m = 4
# ! 2차원 배열 선언 및 초기화
graph = [[0] * m for _ in range(n)]
print(graph)
# out: [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# ! 2차원 배열 입력받기
# * 입력1
# 1 2 3 4
# 2 3 4 5
# 3 4 5 6
graph2 = []
for i in range(n):
    graph2.append(list(map(int, input().split())))
print(graph2)
# out: [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]

# * 입력2
# 1234
# 2345
# 3456
graph3 = []
for i in range(n):
    graph3.append(list(map(int, input())))
print(graph3)
# out: [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]

# * 초기화 및 입력
# 1234
# 2345
# 3456
graph4 = [[0] * m for _ in range(n)]
for i in range(n):
    graph4[i] = list(map(int, input()))
print(graph4)
# out: [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
