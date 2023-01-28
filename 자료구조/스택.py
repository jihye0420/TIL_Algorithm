stack = []

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
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


# class로 구현한 코드
class ListStack:
    def __init__(self):
        self.my_list = list()

    def push(self, data):
        self.my_list.append(data)

    def pop(self):
        return self.my_list.pop()
