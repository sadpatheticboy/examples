""" Условие задачи - https://stepik.org/lesson/701988/step/11?unit=702089 """


class PolyLine:
    def __init__(self, *args):
        self.coords = list(args)

    def add_coord(self, x, y):
        self.coords.append((x, y))

    def remove_coord(self, indx):
        self.coords.pop(indx)

    def get_coords(self):
        return self.coords
