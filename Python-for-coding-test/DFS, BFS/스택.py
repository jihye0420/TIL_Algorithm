"""
# * 리스트로 구현
# * 삽입 : 리스트.append(원소)
# * 삭제 : 리스트.pop()
"""
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)  # 최하단 원소부터 출력
print(stack[::-1])  # 최상단 원소부터 출력
