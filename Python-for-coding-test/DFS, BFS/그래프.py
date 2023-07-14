"""
* 그래프 : 노드(node)==정점(vertex)와 간선(edge)로 표현
* 그래프 2가지 표현 방식
    * 인접 행렬(Adjacency Matrix) : 2차원 배열로 그래프의 연결 관계를 표현하는 방식
    * 인접 리스트(Adjacency List) : 리스트로 그래프의 연결 관계를 표현하는 방식
"""

"""
인접 행렬 : 2차원 배열에 각 노드가 연결된 형태를 기록하는 방식
"""
INF = 999999999

graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

print(graph)

"""
인접 리스트 : 연결 리스트라는 자료구조를 이용해 구현 => 파이썬은 리스트 자료형이 배열과 연결 리스트의 기능을 모두 기본으로 제공 (.append() & 메소드를 제공)
"""

graph = [[] for _ in range(3)]

graph[0].append((1, 7))
graph[0].append((2, 5))

graph[1].append((0, 7))

graph[2].append((0, 5))

print(graph)
