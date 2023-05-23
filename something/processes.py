import multiprocessing


def infinity():
    while True:
        print('Do you like infinity?')


if __name__ == '__main__':
    process = multiprocessing.Process(target=infinity)
    process.start()
    # process.join()

    print('The end!')
