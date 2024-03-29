"""
# 개선된 다익스트라 알고리즘
# 힙 자료구조를 사용 : 우선순위 큐를 구현하기 위하여 사용하는 자료구조
* 자료구조 - 추출되는 데이터
스택: 가장 나중에 삽입된 데이터
큐: 가장 먼저 삽입된 데이터
우선순위 큐: 우선순위가 가장 높은 데이터
* 구현: 최소 힙 구조 기반 - 비용이 적은 노드를 우선 방문 => 우선순위 큐 라이브러리를 그대로 사용
* 최대 힙: 값이 큰 데이터가 먼저 삭제
* 최소 힙: 값이 작은 데이터가 먼저 삭제
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
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

# 노드 개수, 간선 개수 입력
n, m = map(int, input().split())
# 시작 노드 번호 입력
start = int(input())

# 각 노드에 연결되어 있는 노드 정보 담는 리스트
graph = [[] for i in range(n + 1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:  # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)  # => 거리, 노드
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시 (거리가 현재 값보다 크다면 무시)
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


# 다익스트라 알고리즘을 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])
