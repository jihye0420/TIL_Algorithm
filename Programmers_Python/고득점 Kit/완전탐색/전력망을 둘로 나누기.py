# https://school.programmers.co.kr/learn/courses/30/lessons/86971
# * 배운점 : BFS
from collections import deque


def bfs(start, visitied, graph):
    queue = deque([start])
    result = 1
    visitied[start] = True
    while queue:
        now = queue.popleft()

        for i in graph[now]:
            if visitied[i] == False:
                result += 1
                queue.append(i)
                visitied[i] = True
    return result


def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n + 1)]

    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
    print(graph)

    for start, not_visit in wires:
        visitied = [False] * (n + 1)
        visitied[not_visit] = True
        print(visitied)
        result = bfs(start, visitied, graph)
        print(result)
        print(resu)
        if abs(result - (n - result)) < answer:
            answer = abs(result - (n - result))
    return answer


if __name__ == '__main__':
    print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
    # print(solution(4, [[1, 2], [2, 3], [3, 4]]))
    # print(solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]))
