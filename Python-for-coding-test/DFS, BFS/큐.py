"""
# * deque 라이브러리로 구현
# * 삽입 : deque.append(원소)
# * 삭제 : deque.popleft() : 가장 먼저 들어간 원소 제거 / deque.pop() : 가장 마지막 원소 제거
"""
from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)
