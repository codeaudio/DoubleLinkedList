from typing import Any


class Array(list):
    __type: Any = {
        'str': str,
        'int': int,
        'dict': dict,
        'tuple': tuple,
        'set': set,
        'None': 'any'
    }

    def __new__(cls, array, limit=None, type=None):
        if (len(array) > limit) or (False in (isinstance(i, cls.__type.get(type)) for i in array)):
            raise Exception(f"max limit {limit}, type {type}")
        return super().__new__(cls)

    def append(self, __object) -> None:
        if (len(self) > self.__limit) or (isinstance(__object, self.__type.get(self.type)) is False):
            raise Exception(f"max limit {self.__limit}, type {self.__type}")
        return super().append(__object)

    def insert(self, __index: int, __object) -> None:
        if (len(self) > self.__limit) or (isinstance(__object, self.__type.get(self.__type)) is False):
            raise Exception(f"max limit {self.__limit}, type {self.__type}")
        return super().insert(__index, __object)

    def extend(self, __iterable: list) -> None:
        if (len(self) + len(__iterable) > self.__limit) or (
                False in (isinstance(i, self.__type.get(self.__type)) for i in __iterable)):
            raise Exception(f"max limit {self.__limit}, type {self.__type}")
        return super().extend(__iterable)

    def __init__(self, array, limit=None, type=None):
        super().__init__(array)
        self.__limit = limit
        self.type = type
