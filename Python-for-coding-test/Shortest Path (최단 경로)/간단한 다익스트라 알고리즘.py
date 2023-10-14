"""
# 간단한 다익스트라 알고리즘
* 구현: 단계마다 ‘방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택’하기 위해 매 단계마다 1차원 리스트의 모든 원소를 확인(순차 탐색)
[입력]
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
"""
import sys

# input = sys.stdin.readline() # input : 입력한 문자열
input = sys.stdin.readline  # 객체
# print(input)

INF = int(1e9)  # 무한의미 => 10억

# 노드 개수, 간선 개수 입력
n, m = map(int, input().split())
# 시작 노드 번호 입력
start = int(input())

# 각 노드에 연결되어 있는 노드 정보 담는 리스트
graph = [[] for i in range(n + 1)]
# 방문 여부 체크 목적의 리스트
visited = [False] * (n + 1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)
# print(graph)
# print(visited)
# print(distance)

# 모든 간선 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드 -> b번 노드 이동 비용 => c
    graph[a].append((b, c))


# print(graph)
# [[], [(2, 2), (3, 5), (4, 1)], [(3, 3), (4, 2)], [(2, 3), (6, 5)], [(3, 3), (5, 1)], [(3, 1), (6, 2)], []]


# 방문하지 않은 노드 중에서, 가장 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0  # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    # * 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        # graph의 연결된 노드 index = value 간선 비용
        distance[j[0]] = j[1]
    # print("distance: ", distance)
    # distance:  [1000000000, 0, 2, 5, 1, 1000000000, 1000000000]
    # * 시작 노드를 제외한 전체 n-1개의 노드에 대해서 반복
    for i in range(n - 1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        # print("now: ", now)
        # now:  4
        # now:  2
        # now:  5
        # now:  3
        # now:  6
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]  # 최단거리를 가진 노드까지의 거리 + 각 노드의 이동거리
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost


# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
