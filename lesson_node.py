class DoubleConnectedNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def solution(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

    @staticmethod
    def get_node_by_index(node, idx):
        while idx:
            node = node.next
            idx -= 1
        return node

    def insert(self, idx, value, head=None):
        new_node = DoubleConnectedNode(value)
        if idx == 0:
            new_node.next = self.head
            self.head = new_node
            return self.head
        else:
            prev = self.get_node_by_index(node=head or self.head, idx=idx - 1)
            new_node.next = prev.next
            prev.next = new_node
            return self.head

    def delete(self, idx):
        if idx == 0:
            self.head = self.head.next
            return self.head
        else:
            current = self.get_node_by_index(node=self.head, idx=idx)
            prev = self.get_node_by_index(node=self.head, idx=idx - 1)
            prev.next = current.next
            return self.head

    def search(self, element):
        current = self.head
        index = 0
        while current is not None and current.value != element:
            index += 1
            current = current.next
        return index

    def revers(self, node=None):
        if node is not None:
            self.head = node
            current = self.head
        else:
            current = self.head
        while current:
            save = current.next
            if save is None:
                current.next = current.prev
                current.prev = save
                self.head = current
                return self.head
            else:
                current.next = current.prev
                current.prev = save
                current = save





n3 = DoubleConnectedNode('third')
n2 = DoubleConnectedNode('second', n3)
n1 = DoubleConnectedNode('first', n2)
f = LinkedList(n1)
n3.prev = n2
n2.prev = n1

f.solution()
