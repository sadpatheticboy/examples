""" Let's modify our MyRange iterator to accept an optional step argument. The step argument will determine the amount
 by which the iterator will increase between each element. If no step argument is provided, the iterator will default
 to increasing by 1. """


class MyRange:
    def __init__(self, start, stop, step=1):
        self.current = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.stop:
            value = self.current
            self.current += self.step
            return value
        else:
            raise StopIteration


my_range = MyRange(0, 10, 2)
for i in my_range:
    print(i)
