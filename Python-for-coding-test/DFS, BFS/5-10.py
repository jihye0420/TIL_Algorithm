n, m = map(int, input().split())

# 2차원 리스트 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
print(graph)

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
# def DFS():
#     for i in range()
