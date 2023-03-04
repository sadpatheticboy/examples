""" Условие задачи - https://stepik.org/lesson/701987/step/6?thread=solutions&unit=702088 """


class DigitRetrieve:
    def __call__(self, x, *args, **kwargs):
        if x.isdigit() or (x.startswith('-') and x[1:].isdigit()):
            return int(x)
        return None
