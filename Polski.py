import math
from accessify import private

'''https://contest.yandex.ru/contest/23759/run-report/52196792/'''


class EmptyError(BaseException):
    pass


class Stack:
    def __init__(self):
        self.__stack = []
        self.commands = {
            '+': lambda x, y: x + y,
            '/': lambda x, y: math.floor(x / y),
            '*': lambda x, y: x * y,
            '-': lambda x, y: x - y
        }

    @property
    def is_not_empty(self):
        return len(self.__stack) != 0

    @private
    def stack_pop(self):
        if self.is_not_empty:
            self.__stack.pop()
        else:
            raise EmptyError()

    def push(self, element):
        if element in self.commands:
            el1, el2 = int(self.__stack[-2]), int(self.__stack[-1])
            self.stack_pop(), self.stack_pop()
            self.__stack.append(str(self.commands.get(element)(el1, el2)))
        else:
            self.__stack.append(element)
        return self.__stack


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = [(n.split()) for n in f.read().split('\n')]
    stack = Stack()
    len_data = len(data[0]) - 1
    for index, el in enumerate(data[0]):
        try:
            if index == len_data:
                print(stack.push(el)[-1])
            else:
                stack.push(el)
        except:
            print('Error: stack is empty')
