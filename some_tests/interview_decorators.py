def second_outer(*dargs, **dkwargs):
    def outer(func): # f
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


@second_outer(attempts=2)
def div(a, b):
    return a / b


print(div(1, 0))
