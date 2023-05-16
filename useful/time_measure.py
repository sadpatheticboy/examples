import time


def time_measure(func):
    def inner(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__} {end - start}')
        return func(*args, **kwargs)

    return inner
