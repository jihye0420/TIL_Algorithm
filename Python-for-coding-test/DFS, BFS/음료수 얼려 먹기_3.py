def dfs(x, y):
    # 상하좌우
    # dx = [-1, 1, 0, 0]
    # dy = [0, 0, -1, 1]
    if x <= -1 or y <= -1 or x >= n or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        # 상하좌우 => 재귀호출
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


n, m = map(int, input().split())
# 2차원 배열 선언
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))

# 2차원 배열 선언
graph = [[0] * m for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, input()))

# print(graph)
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
print(result)
