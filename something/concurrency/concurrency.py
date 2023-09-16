# Конкурентность (concurrency) - запуск на выполнение сразу нескольких задач (не обязательно в 1 момент времени
# выполняется несколько). Зависит от ПО. Первые ОС с процессором без ядер - использовали только ее.
# Пример конкурентности - одновременная игра в шахматы одного гроссмейстера в нескольких партий

# Параллельность (parallel) - конкурентность, когда 2+ задачи выполняются одновременно. Зависит от железа. Вы не можете
# одновременно (!) выполнять больше задач, чем есть ядер в системе.


# GIL (Global Interpreter Lock) - глобальная блокировка интерпретатора, механизм гарантирующий, что в любой момент
# времени выполняется только 1 инструкция в питоне.

# Задачи для Python могут быть:
# CPU-bound - зависит от мощности процессора
# IO-bound - зависит от системы ввода/вывода

# threading - IO-bound задачи
# asyncio - IO-bound задачи
# multiprocessing - любые задачи

import threading
import time
import requests


def activity():
    # for e in range(1_000_000):
    #     abs(round(e ** 2 / 122) + e * 3.14)
    requests.get("https://yandex.ru")


def run(threaded=False):
    start = time.time()
    if not threaded:
        for e in range(10):
            activity()
    else:
        threads = [threading.Thread(target=activity, daemon=True) for _ in range(10)]
        for e in threads:
            e.start()
        for e in threads:
            e.join()

    end = time.time()
    print(f'Time: {end - start} seconds.')


if __name__ == '__main__':
    run(threaded=True)
