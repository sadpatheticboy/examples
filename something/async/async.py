import asyncio
import random


async def some_task():
    wait = random.randint(0, 9)
    for i in range(10):
        print('Something...')
        if i == wait:
            await asyncio.sleep(1)


async def imitate_responsive_ui():
    input('Hi! How was your day?\n')
    print('That\' great!')


async def main():
    task1 = some_task()
    task2 = imitate_responsive_ui()
    await asyncio.gather(task1, task2)


asyncio.run(main())
