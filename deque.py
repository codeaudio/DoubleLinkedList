class EmptyError(Exception):
    pass


'''https://contest.yandex.ru/contest/23759/run-report/52196811/'''


class Deque:
    def __init__(self, max_size):
        self.__deque = [None] * max_size
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push_front(self, element):
        if self.size == self.max_size:
            raise IndexError()
        self.head = (self.head + 1) % self.max_size
        self.__deque[self.head] = element
        self.size += 1

    def pop_front(self):
        if self.is_empty():
            raise EmptyError()
        get_head_element = self.__deque[self.head]
        self.__deque[self.head] = None
        self.head = (self.head - 1) % self.max_size
        self.size -= 1
        return get_head_element

    def push_back(self, element):
        if self.size == self.max_size:
            raise IndexError()
        self.__deque[self.tail] = element
        self.tail = (self.tail - 1) % self.max_size
        self.size += 1

    def pop_back(self):
        if self.is_empty():
            raise EmptyError()
        self.tail = (self.tail + 1) % self.max_size
        get_tail_element = self.__deque[self.tail]
        self.__deque[self.tail] = None
        self.size -= 1
        return get_tail_element


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = [list(n.split()) for n in f.read().split('\n')]
    max_size = int(data[1][0])
    data = data[2::]
    deque = Deque(max_size)
    commands = {
        'push_front': getattr(deque, 'push_front'),
        'push_back':  getattr(deque, 'push_back'),
        'pop_front': getattr(deque, 'pop_front'),
        'pop_back': getattr(deque, 'pop_back'),
    }
    for i, elem in enumerate(data):
        try:
            try:
                if commands.get(elem[0]):
                    commands.get(elem[0])(int(elem[1]))
            except:
                if commands.get(elem[0]):
                    print(commands.get(elem[0])())
        except:
            if len(data) - 1 == i:
                break
            print('error')
