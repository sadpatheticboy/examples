from multiprocessing import Process, Pool
from time import sleep
from random import random


def file_writer(start: int, finish: int):
    with open("locker.txt", "w") as f_o:
        for i in range(start, finish):
            sleep(.5)
            print(i)
            f_o.write(f"{i}\n")


if __name__ == "__main__":
    p1 = Process(target=file_writer, args=(0, 5))
    p2 = Process (target=file_writer, args = (5, 10))
    p1.start()
    p2.start()
