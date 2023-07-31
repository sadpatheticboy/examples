import time as tm
import timeit as ti


def some_func(n):
    return [val ** 10 for val in range(1, n)]


# 1. time
# 1.a Обычный вариант использования замера времени
t_start = tm.time()  # Return the current time in seconds since the Epoch
a = some_func(500_000)
t_end = tm.time()
print(t_end - t_start)

# 1.b Небольшой эксперимент
t_start = tm.time()
tm.sleep(5)
t_end = tm.time()
print(t_end - t_start)

# 1.c Как отвязаться от Epoch time
t_start = tm.monotonic()
tm.sleep(5)
t_end = tm.monotonic()
print(t_end - t_start)

# 2. timeit
# 2.a Как получить данные timeit стандартным способом
print(ti.timeit(setup=some_func,
                stmt='some_func(500_000)',
                number=20))

# 2.b timeit repeat
print(ti.repeat(setup=some_func,
                stmt='some_func(500_000)',
                number=20,
                repeat=2))
