# https://school.programmers.co.kr/learn/courses/30/lessons/42628
import heapq


def solution(operations):
    answer = []
    heap = []
    for i in operations:
        i = i.split()
        first = i[0]
        second = int(i[1])
        if first == 'I':
            heapq.heappush(heap, second)
        elif first == 'D':
            if second == 1 and len(heap):
                heap.pop(-1)
            elif second == -1 and len(heap):
                heapq.heappop(heap)
            else:
                continue
    answer.append(max(heap) if heap else 0)
    answer.append(min(heap) if heap else 0)
    return answer


"""
# 다른 풀이 
2개의 힙을 이용하는 것
"""

if __name__ == '__main__':
    print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
    print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
