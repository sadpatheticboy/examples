# Аннотации типов - всего лишь подсказка, а не жёсткое указание
# Optional[int, float] - может принять None и любой из перечисленных типов. Аналог None | int | float
# Any - любой аргумент
# Union - аналог int | float и т.д.

from typing import List


def add(a: int | float, b: int | float) -> int | float:
    return a + b


def to_int(a_list: list[str]) -> list[int]:  # До версии 3.9 надо было писать List[int], после можно просто list[int]
    return [int(e) for e in a_list]


if __name__ == '__main__':
    print(add(1, 2))
    # add(2, 3).upper() # После указание возвращаемого значения int, PyCharm начинает подсказывать, что что-то не так
    # print(add(2, '3')) # После указания типа для аргументов, появлятся подсказки, что не типы данных
    print(add(1, 3.1))

    print(to_int(['1', '2']))
