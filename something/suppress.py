import os
from contextlib import suppress

path = 'somefile.tmp'


def remove():  # faster
    if os.path.exists(path):
        os.remove(path)


def remove1():  # +- = remove3
    try:
        os.path.exists(path)
    except FileNotFoundError:
        pass


def remove3():  # +- = remove1
    with suppress(FileNotFoundError, ZeroDivisionError):
        os.remove(path)
        1 / 0
