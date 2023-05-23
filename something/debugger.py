def one(x, y):
    result = x + y
    return two(result)


def two(result):
    result = f'{result}!!'
    return three(result)


def three(result):
    return 100 / result.count('!')


def cycle(value):
    even_squares = [e ** 2 for e in range(10) if e % 2 == 0]
    for e in range(6):
        value += e
        print(value)
    return value


if __name__ == '__main__':
    # print(one(1, 2))
    cycle(50)