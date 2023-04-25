def logger(func):
    def wrapper(*args):
        print(f'{func.__name__} started')
        result = func(*args)
        print(f'{func.__name__} finished')
        return result

    return wrapper


@logger
def suma(a, b):  # в момент интерпретации suma=wrapper
    return a + b


if __name__ == '__main__':
    # function = logger(suma)
    # print(function(2, 3))

    # print(logger(suma)(2, 3))

    # suma = logger(suma) # Именно это делает интерпретатор
    # print(suma(2, 3))

    print(suma(2, 3))
    # print(suma) # <function logger.<locals>.wrapper at 0x0000024643645EE0>
