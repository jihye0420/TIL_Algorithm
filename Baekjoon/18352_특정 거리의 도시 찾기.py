# https://www.acmicpc.net/problem/18352
import sys
from collections import deque

input = sys.stdin.readline


def bfs(x, graph, d):
    queue = deque([x])
    while queue:
        now = queue.popleft()
        # 현재 도시에서 이동 할 수 있는 도시 모두 확인
        for next in graph[now]:
            # 아직 방문하지 않은 도시라면
            if d[next] == -1:
                d[next] = d[now] + 1
                queue.append(next)
    return


n, m, k, x = map(int, input().split())  # 정점 개수, 간선 개수, 거리 정보, 출발 도시의 번호
graph = [[] for _ in range(n + 1)]
# print(graph)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

for i in graph:
    i.sort()

# print(graph)

"""
모든 도시에 대한 최단 거리 초기화
"""
d = [-1] * (n + 1)
d[x] = 0

bfs(x, graph, d)
print(d)
check = False
for i in range(1, n + 1):
    if d[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)
