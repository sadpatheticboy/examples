import time


def time_measure(func):
    def inner():
        start = time.time()
        func()
        end = time.time()
        print(f'{func.__name__} {end - start}')

    return inner()
