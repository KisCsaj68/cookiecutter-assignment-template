from typing import Any, List, Tuple, Union


def min(x: int, y: int) -> int:
    result: int = x if x < y else y
    return result


def max(values_list: List[int]) -> int:
    result: int = values_list[0]
    for num in values_list:
        if num > result:
            result = num
    return result


def len(values_list: List[Any]) -> int:
    result: int = 0
    for value in values_list:
        result += 1
    return result


def multiply(x, y) -> int:
    result: int = 0
    if x == 0 or y == 0:
        return 0
    if y < 0:
        y = -y
        x = -x
    for i in range(y):
        result += x
    return result


def pow(x, y) -> int:
    result: int = 1
    if x == 0:
        result = 0
    for i in range(y):
        result *= x
    return result


def divmod(x: int, y: int) -> Union[str, Tuple[int, int]]:
    if y == 0:
        return "Div with 0 not possible"
    if x == y:
        return 1, 0
    if x < y and x > 0:
        return 0, x
    if x > y and x < 0 and y < 0:
        return 0, x

    counter: int = 0
    if x > y and y > 0:
        while x > y:
            counter += 1
            x -= y
        return counter, x

    if x < 0 and y < 0:
        while x < y:
            counter += 1
            x -= y
        return counter, x

    if x < 0 and y > 0:
        while x < 0:
            counter -= 1
            x += y
        return counter, x

    if x > 0 and y < 0:
        while x > 0:
            counter -= 1
            x += y
        return counter, x
