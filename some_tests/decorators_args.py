def typed(type_):
    def real_decorator(func):
        def wrapper(*args):
            for arg in args:
                if not isinstance(arg, type_):
                    raise ValueError(f'Тип должен быть {type_}')
            return func(*args)

        return wrapper

    return real_decorator


@typed(int)
def calculate(a, b, c):
    # Logic
    return a + b + c


@typed(str)
def convert(a, b):
    # Logic
    return a + b


if __name__ == '__main__':
    # calculate = typed(int)(calculate)
    print(calculate(1, 2, 3))
    print(convert('1', '2'))
