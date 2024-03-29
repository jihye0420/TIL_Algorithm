# * 최소 힙: 값이 작은 데이터가 먼저 삭제
import heapq


# 오름차순 힙 정렬(Heap Sort)
def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result


result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)


# * 최대 힙: 파이썬은 최대 힙 제공하지 않음 -> 최소힙의 부호를 바꾸면 됨

# 내림차순 힙 정렬(Heap Sort)
def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result


result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)

"""
# 기존 리스트를 힙으로 변환
"""
import heapq

# 최소 힙 생성, push
heap_list = []
heapq.heappush(heap_list, 4)
heapq.heappush(heap_list, 1)
heapq.heappush(heap_list, 7)

# pop
heapq.heappop(heap_list)

# pop하지 않고 최솟값 얻기
print(heap_list[0])

# 기존 리스트를 힙으로 변환
a_list = [4, 1, 7, 3, 8, 5]
heapq.heapify(a_list)
