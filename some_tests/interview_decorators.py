def second_outer(*dargs, **dkwargs):
    def outer(func):
        def inner(*args, **kwargs):
            attempts = dkwargs['attempts']
            while attempts > 0:
                try:
                    return func(*args, **kwargs)
                except Exception as err:
                    print(f'Error: {err}, attempts left: {attempts}')
                    attempts -= 1

        return inner

    return outer


def simple_deco(func):
    def inner(*args, **kwargs):
        print('Реклама')

        return func(*args, **kwargs)

    return inner


@simple_deco
@second_outer(attempts=3)
def div(a, b):
    return a / b


print(div(1, 0))
