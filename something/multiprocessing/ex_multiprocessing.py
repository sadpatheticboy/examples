import time
from multiprocessing import Process
import os

CNT = 0


def f_2():
    global CNT
    CNT += 1
    print(f"f_2: {CNT} from", os.getpid())


def f_1():
    global CNT
    CNT += 3
    print(f"f_1: {CNT} from", os.getpid())


def f():
    global CNT
    CNT += 2
    print(f"f: {CNT} from", os.getpid())


if __name__ == "__main__":
    time.sleep(1)
    print(f"{os.getpid()} ENTERED!")
    p = Process(target=f, args=())  # создаём объект, в котором хотим запустить функцию с параметрами
    p_1 = Process(target=f_1, args=())
    p_2 = Process(target=f_2, args=())
    p.start()  # тут будет под капотом форкнут процесс и в нём выполнена функция с параметрами
    p_1.start()
    p_2.start()
    p.join()  # ожидание завершения всех дочерних процессов
    p_1.join()
    p_2.join()
    print(f"{os.getpid()} FINISNED!")
    print(f"value = {CNT}")
