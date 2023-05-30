import multiprocessing
import os


def foo(l):
    for i in l:
        f(i)
    print(os.getpid())
    return False


def f(x):
    # print(os.getpid())
    return hash(x)


if __name__ == '__main__':
    n = 100

    with multiprocessing.Pool(processes=4) as pool:
        # multiple_results = [pool.apply_async(os.getpid(), ()) for i in range(n)]
        # print([res.get() for res in multiple_results])
        # pool.apply(foo, (range(n),))  # блокируется родительский процесс, родительский процесс в этот момент ожидает
        res = pool.apply_async(foo, (range(n),))  # id процесса не будет выведено, т.к. родительский завершится раньше
        while not res.ready():
            print('still going...')
        print(res.get())  # получение результата дочернего процесса
        print('the end')
