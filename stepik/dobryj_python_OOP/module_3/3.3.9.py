""" Условие задачи - https://stepik.org/lesson/701988/step/9?unit=702089 """


class Clock:
    def __init__(self, hours, minutes, seconds):
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds

    def get_time(self):
        return self._hours * 3600 + self._minutes * 60 + self._seconds


class DeltaClock:
    def __init__(self, clock1, clock2):
        self._clock1 = clock1
        self._clock2 = clock2

    def __len__(self):
        diff = self._clock1.get_time() - self._clock2.get_time()
        return diff if diff > 0 else 0

    def __str__(self):
        d = self.__len__()
        h = d // 3600
        m = d % 3600 // 60
        s = d % 3600 % 60
        return f'{h:02}: {m:02}: {s:02}'
