class ArgumentEqualZeroError(Exception):
    """When the divisor equal zero"""


class ArgumentNotIntger(Exception):
    """When argument not integer"""


def divide(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ArgumentNotIntger('Incorrect types of arguments, must be int')
    if b == 0:
        raise ArgumentEqualZeroError('Divisor cannot be 0')

    return a // b


if __name__ == '__main__':
    try:
        result = divide(4, 2)
    except (ArgumentNotIntger, ArgumentEqualZeroError) as exc:
        print(exc)
    finally:
        print('Finish')
