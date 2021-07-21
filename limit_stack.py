class MaxSizeError(BaseException):
    pass


class LimitStack:
    def __init__(self, max_size):
        self.__stack = []
        self.max_size = max_size
        self.head = 0

    @property
    def isEmpty(self):
        return len(self.__stack) == 0

    def push(self, element):
        if self.size() == max_size:
            raise MaxSizeError('error: stack is max size')
        self.__stack.append(element)

    def pop(self):
        if self.isEmpty is False:
            self.head -= 1
            delete_head = self.__stack[self.head]
            self.__stack[self.head] ==  None
            return delete_head

    def peek(self):
        if self.size() != 0:
            return self.__stack[0]

    def size(self):
        return len(self.__stack)


if __name__ == '__main__':
    with open('limit_stack.txt', 'r') as f:
        data = [n.split() for n in f.read().split('\n') if n != '\n' and n != '']
    max_size = int(data[1][0])
    data = data[2:]
    limit_stack = LimitStack(max_size)
    commands = {
        'push': getattr(limit_stack, 'push'),
        'pop': getattr(limit_stack, 'pop'),
        'peek': getattr(limit_stack, 'peek'),
        'size': getattr(limit_stack, 'size'),
    }
    for elem in data:
        if commands.get(elem[0]):
            try:
                if len(elem) > 1:
                    commands.get(elem[0])(int(elem[1]))
                else:
                    print(commands.get(elem[0])())
            except MaxSizeError:
                print('error')

