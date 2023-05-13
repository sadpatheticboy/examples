from contextlib import contextmanager


class Resourse:
    def __init__(self):
        self.opened = False

    def open(self, *args):
        print(f'Resourse was open with argumets {args}')
        self.opened = True

    def close(self):
        print(f'Resourse was closed!')
        self.opened = False

    def __del__(self):
        if self.opened:
            print('Memory leak detected! Resourse was not closed')

    def action(self):
        print('Do something with resourse')


@contextmanager
def open_resourse(*args):
    resourse = None
    try:
        resourse = Resourse()
        resourse.open(*args)
        yield resourse
    except Exception:
        raise
    finally:
        if resourse:
            resourse.close()


class ResourceWorker:
    def __init__(self, *args):
        self.args = args
        self.resourse = None

    def __enter__(self):
        self.resourse = Resourse()
        self.resourse.open(*self.args)
        return self.resourse

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.resourse:
            self.resourse.close()


if __name__ == '__main__':
    with ResourceWorker(1, 2, 3) as res:
        res.action()
