import threading
import multiprocessing
import time


def print_numbers(start, finish):
    for i in range(start, finish):
        print(i)


def threads(n):
    thrs = []
    for i in range(1, n):
        thrs.append(threading.Thread(target=print_numbers, args=(i * 100, i * 100 + 10)))
    for t in thrs:
        t.start()
    for t in thrs:
        t.join()


def processes(n):
    procs = []
    for i in range(1, n):
        procs.append(multiprocessing.Process(target=print_numbers, args=(i * 100, i * 100 + 10)))
    for t in procs:
        t.start()
    for t in procs:
        t.join()


if __name__ == '__main__':
    n = 100
    start = time.time()
    # processes(n) # 4.4470131397247314
    threads(n)  # 0.02945399284362793
    finish = time.time()
    print(finish - start)
