import multiprocessing
import time


def write_to_file(file_path, queue, lock):
    line = queue.get()
    with lock:
        with open(file_path, 'a') as file:
            file.write(line)


if __name__ == '__main__':
    file_path = 'racing.txt'
    queue = multiprocessing.Queue()
    lock = multiprocessing.Lock()
    processes = []
    start = time.time()
    for i in range(50):
        queue.put(f'line {i}\n')
        process = multiprocessing.Process(target=write_to_file(file_path, queue, lock))
        processes.append(process)

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    print(time.time() - start)
    print('done')
