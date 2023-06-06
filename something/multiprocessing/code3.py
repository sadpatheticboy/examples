import time
from random import randint
import os
import multiprocessing
from datetime import datetime
from multiprocessing import Process


# with open("file.txt", "w") as f_o:
#     for _ in range(10_000_000):
#         f_o.write(f" {randint(0, 9)}\n")


def laborator(*args, **kwargs):
    result = 0
    with open("file.txt", "r") as f_o:
        for s in f_o:
            # time.sleep(100)
            result += randint(0, int(s))  # Именно на эту строчку будут приходиться основные расходы
    print(os.getpid(), result)


# # простой запуск (подсчет чисел, 1 процесс) - 0:00:20.829156
# if __name__ == '__main__':
#     start = datetime.now()
#     laborator()
#     laborator()
#     print(datetime.now() - start)

# # Запуск с процессами - 0:00:13.079955
# if __name__ == '__main__':
#     start = datetime.now()
#     p = Process(target=laborator)
#     p_1 = Process(target=laborator)
#     p.start()  # Призыв к исполнению
#     p_1.start()  # Призыв к исполнению
#     p.join()  # Синхронизация, не пойдём дальше до тех пор, пока р не завершится
#     print("p завершился")
#     p_1.join()  # Синхронизация, н  е пойдём дальше до тех пор, пока р_1 не завершится
#     print("p_1 завершился")
#     print(datetime.now() - start)

# # Запуск с процессами + рефакторинг - 0:00:12.364683
# if __name__ == '__main__':
#     start = datetime.now()
#     p_list = [Process(target=laborator) for _ in range(2)]
#     for p in p_list:
#         p.start()
#     for p in p_list:  # без этого основной поток завершит работу, но это не помешает работать дочерним
#         p.join()
#     print(datetime.now() - start)

# Запуск с 1 потоком - 0:00:22.624497
# С 2 потоками - 0:00:12.710826
if __name__ == '__main__':
    # Пул процессов удобен для того, чтобы одну и ту же функцию вызвать с разными аргументами в нескольих потоках
    # Однако, есть одна особенность - пул работает для функций, у которых есть аргументы
    start = datetime.now()
    with multiprocessing.Pool(2) as pool:
        pool.map(laborator, (1, 2))  # Второй аргумент - аргументы в фунцию laborator, можно указать *args и **kwargs
    print(datetime.now() - start)


