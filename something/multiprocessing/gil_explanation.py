import threading

a = 0
lock = threading.Lock()


def x():
    global a
    lock.acquire()
    for i in range(100_000):
        a += 1
    lock.release()


threads = []
for j in range(2):
    thread = threading.Thread(target=x)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()


assert a == 200_000
