import multiprocessing
import os


def update_main_list(shared_list, n):
    for i in range(n):
        shared_list.append(f"{os.getpid()}_{i}")


if __name__ == '__main__':
    n = 10
    count = 4

    manager = multiprocessing.Manager()
    shared_list = manager.list()

    with multiprocessing.Pool(count) as pool:
        for i in range(count):
            pool.apply(update_main_list, (shared_list, n))

    main_list = list(shared_list)
    print(main_list)
