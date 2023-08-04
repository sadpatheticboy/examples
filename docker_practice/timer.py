from datetime import datetime
from time import sleep

counter = 0
while counter < 20:
    print(f'{datetime.now()}: {counter}')
    counter += 1
    sleep(1)