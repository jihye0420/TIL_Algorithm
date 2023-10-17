# 최소 힙
import heapq


def min_heapq_sort(data):
    h = []
    result = []
    for i in data:
        heapq.heappush(h, i)
    print(h)
    for j in range(len(h)):
        result.append(heapq.heappop(h))
    return result


print(min_heapq_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))


# 최대 힙
def max_heapq_sort(data):
    h = []
    result = []
    for i in data:
        heapq.heappush(h, -i)
    print(h)
    for j in range(len(h)):
        result.append(-heapq.heappop(h))
    return result


print(max_heapq_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))
