from decimal import Decimal
from typing import Any


class Array(list):
    __type: Any = {
        'str': str,
        'int': int,
        'float': float,
        'bool': bool,
        'list': list,
        'dict': dict,
        'tuple': tuple,
        'set': set,
        'frozenset': frozenset,
        'decimal': Decimal
    }

    def __new__(cls, array: list, __array_type: str, limit: int = None):
        if (len(array) > limit) or (False in (isinstance(i, cls.__type.get(__array_type)) for i in array)):
            raise Exception(f"max limit {limit}, type {__array_type}")
        return super().__new__(cls)

    def append(self, __object) -> None:
        if (len(self) > self.__limit) or (isinstance(__object, self.__type.get(self.array_type)) is False):
            raise Exception(f"max limit {self.__limit}, type {self.__array_type}")
        return super().append(__object)

    def insert(self, __index: int, __object) -> None:
        if (len(self) > self.__limit) or (isinstance(__object, self.__type.get(self.array_type)) is False):
            raise Exception(f"max limit {self.__limit}, type {self.__array_type}")
        return super().insert(__index, __object)

    def extend(self, __iterable: list) -> None:
        if ((len(self) + len(__iterable) > self.__limit) or
                (False in (isinstance(i, self.__type.get(self.array_type)) for i in __iterable))):
            raise Exception(f"max limit {self.__limit}, type {self.__array_type}")
        return super().extend(__iterable)

    def __init__(self, array: list, array_type: str, limit: int = None):
        super().__init__(array)
        self.__limit = limit
        self.__array_type = array_type
