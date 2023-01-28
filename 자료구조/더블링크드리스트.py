# Python으로 Node 구성 : 데이터 저장하는 변수 & 이전, 다음 노드 가리키는 포인터 존재
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# tail 변수 추가, add 시 tail 변수 고려! 이하 동일
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head

    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            new_node.prev = node
            node.next = new_node
            self.tail = new_node
