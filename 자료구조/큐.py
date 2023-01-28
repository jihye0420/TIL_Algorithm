import queue

queue = queue.PriorityQueue()
queue.put((1, 1))  # (우선순위, 값)
queue.put((10, 1))
queue.put((7, 2))

print(queue.get())  # 우선순위가 높은 것부터 순서대로 출력됨
print(queue.qsize())

# Python에서는 queue라이브러리를 제공 &  but, 큐 자료구조는 list로 구현 가능
# Queue(): 일반적인 큐 자료구조
import queue

data_queue = queue.Queue()
data_queue.put(1)  # 1
data_queue.put(2)  # 1 - 2
data_queue.put(3)  # 1 - 2 - 3
data_queue.get()  # 1 출력
data_queue.get()  # 2 출력

# 큐(Queue) 구현을 위해 deque 라이브러리 사용
from collections import deque

queue = deque()

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)  # 먼저 들어온 순서대로 출력
queue.reverse()  # 다음 출력을 위해 역순으로 바꾸기
print(queue)  # 나중에 들어온 원소부터 출력

# LifoQueue(): 나중에 입력된 데이터가 먼저 출력되는 구조(Stack과 동일)
data_queue = queue.LifoQueue()
data_queue.put(1)  # 1
data_queue.put(2)  # 2 - 1
data_queue.put(3)  # 3 - 2 - 1
data_queue.get()  # 3 출력
data_queue.get()  # 2 출력

# PriorityQueue(): 데이터마다 우선순위를 지정하여, 정렬된 큐로, 우선순위 높은 순으로 출력하는 자료 구조
data_queue = queue.PriorityQueue()
data_queue.put((10, 1))  # (10,1)
data_queue.put((5, 2))  # (5, 2) - (10,1)
data_queue.put((15, 3))  # (5, 2) - (10, 1) - (15,3)
data_queue.get()  # (5,2) 출력
data_queue.get()  # (10, 1) 출력


# 리스트로 Queue 구현
class ListQueue:
    def __init__(self):
        self.my_list = list()

    # Enqueue
    def put(self, element):
        self.my_list.append(element)

    # Dequeue
    def get(self):
        return self.my_list.pop(0)

    # 큐의 길이 반환
    def qsize(self):
        return len(self.my_list)


# 리스트로 PriorityQueue 구현
class ListPriorityQueue:
    def __init__(self):
        self.my_list = list()

    def put(self, element):
        self.my_list.append(element)
        self.my_list.sort(key=lambda x: x[0])

    def get(self):
        return self.my_list.pop(0)

    def qsize(self):
        return len(self.my_list)
