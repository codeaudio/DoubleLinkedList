from decimal import Decimal
from typing import Any


class UnsupportedAttributeError(AttributeError):
    pass


class DeletedAttribute:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        cls_name = owner.__name__
        raise UnsupportedAttributeError(f'attribute {self.name!r} of {cls_name} has been deleted')


class Array(list):
    extend = DeletedAttribute()

    insert = DeletedAttribute()

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
        if (self.head >= self.__limit) or (
                isinstance(__object, self.__type.get(self.__array_type)) is False) or None not in self:
            raise Exception(f"max limit {self.__limit}, type {self.__array_type}")
        self[self.head] = __object
        self.head += 1

    def pop(self, *args):
        self.head -= 1
        self[self.head] = None

    def __init__(self, array: list, array_type: str, limit: int):
        ln = len(array)
        super().__init__(array + ([None] * (limit - ln)))
        self.head = ln
        self.__limit = limit
        self.__array_type = array_type
