""" Условие задачи - https://stepik.org/lesson/701986/step/11?unit=702087 """

import time


class GeyserClassic:
    MAX_DATE_FILTER = 100

    def __init__(self):
        self.filter_class = ('Mechanical', 'Aragon', 'Calcium')
        self.filters = {(1, 'Mechanical'): None, (2, 'Aragon'): None, (3, 'Calcium'): None}

    def add_filter(self, slot_num, filter):
        key = (slot_num, filter.__class__.__name__)
        if key in self.filters and not self.filters[key]:
            self.filters[key] = filter

    def remove_filter(self, slot_num):
        if type(slot_num) == int and 1 <= slot_num <= 3:
            key = (slot_num, self.filter_class[slot_num - 1])
            if key in self.filters:
                self.filters[key] = None

    def get_filters(self):
        return tuple(self.filters.values())

    def water_on(self):
        end = time.time()
        for f in self.filters.values():
            if f is None:
                return False
            start = f.date
            if end - start >= self.MAX_DATE_FILTER:
                return False
        return True


class Mechanical:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == 'date' and key in self.__dict__:
            return
        super().__setattr__(key, value)


class Aragon:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == 'date' and key in self.__dict__:
            return
        super().__setattr__(key, value)


class Calcium:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == 'date' and key in self.__dict__:
            return
        super().__setattr__(key, value)
