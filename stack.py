class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peak(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def isEmpty(self) -> bool:
        return len(self.items) == 0

a = Stack()
a.push(1)
a.push(2)
a.push(3)
print(a.isEmpty())
print(a.peak())

