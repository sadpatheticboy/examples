import multiprocessing

main_list = []


# def update_main_list(queue, proc_num, n):
def update_main_list(shared_list, proc_num, n):
    # main_list = queue.get()
    for i in range(n):
        shared_list.append(f"{proc_num}_{i}")
    # print(main_list)
    # queue.put(main_list)
    print(shared_list)


if __name__ == '__main__':
    n = 10
    count = 4
    procs = []
    # queue = multiprocessing.Queue()
    # queue.put(main_list)

    manager = multiprocessing.Manager()
    shared_list = manager.list()

    for i in range(count):
        # procs.append(multiprocessing.Process(target=update_main_list, args=[queue, i + 1, n]))
        procs.append(multiprocessing.Process(target=update_main_list, args=[shared_list, i + 1, n]))

    for proc in procs:
        proc.start()

    for proc in procs:
        proc.join()

    # main_list = queue.get()
    main_list = list(shared_list)

    print(main_list)
