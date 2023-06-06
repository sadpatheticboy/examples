from multiprocessing import Process
from datetime import datetime
import time
import os


def sleeper():
    time.sleep(10)
    print(f"Process {os.getpid()} has been finished!")


if __name__ == "__main__":
    start = datetime.now()
    p = Process(target=sleeper)
    p.start()
    p.join()
    print(f"Program in main process {os.getpid()} has been finished! Total execution time: ", datetime.now() - start)
