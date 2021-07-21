from accessify import private


class EmptyError(BaseException):
    pass


class Stack:
    def __init__(self):
        self.__stack = []
        self.__parent_brackets = {
            ']': '[',
            '}': '{',
            ')': '(',
        }

    @property
    def isNotEmpty(self) -> bool:
        return len(self.__stack) != 0

    def stack_push(self, bracket: str) -> None:
        if self.__parent_brackets.get(bracket) in self.__stack:
            self.__stack_pop()
        else:
            self.__stack.append(bracket)

    @private
    def __stack_pop(self) -> None:
        if self.isNotEmpty:
            self.__stack.pop()
        else:
            raise EmptyError(f'Error: stack is empty {self.__stack}')

    def is_correct_bracket_seq(self, brackets_arr: list, len_brackets_arr: int) -> bool:
        for index, el in enumerate(brackets_arr):
            stack.stack_push(el)
            if index == len_brackets_arr:
                return not self.isNotEmpty
        return True


if __name__ == '__main__':
    with open('brackets.txt', 'r') as f:
        brackets_arr = [''.join(list(n)) for n in f.read() if n != '\n' and n != ' ']
    stack = Stack()
    len_brackets_arr = len(brackets_arr) - 1
    try:
        print(stack.is_correct_bracket_seq(brackets_arr, len_brackets_arr))
    except EmptyError:
        print('error: stack is empty')
