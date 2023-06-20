import threading


def print_numbers(start, finish):
    for i in range(start, finish):
        print(i)


thread = threading.Thread(target=print_numbers, args=(1, 10))
thread.start()
thread.join()

print_numbers(51, 60)
