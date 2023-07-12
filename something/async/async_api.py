import asyncio
import aiohttp


async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return data


async def process_call():
    print('Perfoming web request...')
    url = 'https://catfact.ninja/fact'
    data = await fetch_data(url)
    print(f'Recieved data: {data}')


async def imitate_responsive_ui():
    input('Hi! How was your day?\n')
    print('That\' great!')


async def main():
    task1 = process_call()
    task2 = imitate_responsive_ui()
    await asyncio.gather(task1, task2)


asyncio.run(main())
