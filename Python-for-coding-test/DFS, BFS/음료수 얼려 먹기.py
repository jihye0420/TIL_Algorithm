"""
1. 특정 지점 주변 상하좌우 중 주변 지점 중에서 값이 0이면서 아직 방문하지 않은 지점이 있다면 해당 지점을 방문
2. 방문한 지점에서 다시 상하좌우 방문 진행 -> 연결된 모든 지점 방문 처리
3. 1~2번의 과정을 모든 노드에 반복하며 방문하지 않은 지점의 수를 셈
"""
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))


# DFS로 특정 노드를 방문한 뒤 연결된 모든 노드들도 방문
def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        # print(x, y)
        # print(graph)
        # 방문처리
        graph[x][y] = 1
        # 상하좌우 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


result = 0
# 모든 노드에 대하여 음료수 채우기
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
print(graph)
print(result)
