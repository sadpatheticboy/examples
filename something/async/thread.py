import threading


def some_task():
    for i in range(25):
        print('Something...')


def greetings():
    input('Hi! How was your day?\n')
    print('That\' great!')


def main():
    threading.Thread(target=some_task).start()
    threading.Thread(target=greetings).start()


main()
