import queue

queue = queue.PriorityQueue()
queue.put((1, 1)) # (우선순위, 값)
queue.put((10, 1))
queue.put((7, 2))

print(queue.get()) # 우선순위가 높은 것부터 순서대로 출력됨
print(queue.qsize())