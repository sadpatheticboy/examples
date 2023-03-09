""" Условие задачи - https://stepik.org/lesson/701990/step/8?unit=702091 """


class FileAcceptor:
    def __init__(self, *args):
        self.exts = args

    def __call__(self, filename, *args, **kwargs):
        if isinstance(filename, str) and '.' in filename:
            indx = filename.rfind('.')
            return [False, True][filename[indx + 1:] in self.exts]

    def __add__(self, other):
        return FileAcceptor(*(self.exts + other.exts))

    def __radd__(self, other):
        return self.__add__(other)


acceptor1 = FileAcceptor("jpg", "jpeg", "png")
acceptor2 = FileAcceptor("png", "bmp")
acceptor12 = acceptor1 + acceptor2  # ("jpg", "jpeg", "png", "bmp")

print(acceptor12)
