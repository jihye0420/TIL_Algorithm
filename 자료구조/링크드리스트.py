# Python으로 Node 구성 : 데이터 저장하는 변수 & 다음 노드 가리키는 포인터 존재
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Python LinkedList 구성 : 아래 코드에서는 중간 데이터 삽입 코드는 작성하지 않음
class LinkedList:
    def __init__(self):
        self.head = None

    # 헤더부터 탐색해 뒤에 새로운 노드 추가하기
    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = new_node

    # 중간에 노드 추가하기
    def add_node(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        node = self.get_node(index - 1)
        next_node = node.next
        node.next = new_node
        new_node.next = next_node

    # 노드 삭제 (data 기준)
    def delete(self, data):
        node = self.head
        if node.data == data:
            self.head = node.next
            del node
        else:
            while node.next:
                next_node = node.next
                if next_node.data == data:
                    node.next = next_node.next
                    del next_node
                else:
                    node = node.next

    # 노드 삭제 (index 기준)
    def delete_index(self, index):
        if index == 0:
            self.head = self.head.next
            return
        node = self.get_node(index - 1)
        node.next = node.next.next

    # 노드 찾기 (data 기준)
    def find(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next

    # 노드 찾기 (index 기준)
    def find_idex(self, index):
        cnt = 0
        node = self.head
        while cnt < index:
            cnt += 1
            node = node.next
        return node

    # 모든 노드 값 출력
    def print(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
