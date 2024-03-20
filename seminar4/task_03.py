"""
Задание №3.
� Написать программу, которая считывает список из 10 URLадресов и одновременно загружает данные с каждого
адреса.
� После загрузки данных нужно записать их в отдельные
файлы.
� Используйте асинхронный подход.
"""
import asyncio
import aiohttp
from time import time
from concurrent.futures import ThreadPoolExecutor  # Этот код использует ThreadPoolExecutor для записи данных в файл вне асинхронной среды


async def download_data(url, filename):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.read()
            output_path = f"output/{filename}"
            loop = asyncio.get_event_loop()
            with ThreadPoolExecutor() as pool:
                await loop.run_in_executor(pool, write_to_file, data, output_path)


def write_to_file(data, filename):
    with open(filename, 'wb') as file:
        file.write(data)


urls = [
    'http://zagonka11.zagonkop.gb.net/108140-kotiki-2022-onlayn.html',
    'http://www.nnzoo.ru/animals.html'
]


async def main():
    start_time = time()

    async_tasks = []
    for i, url in enumerate(urls):
        filename = f'data_{i}.txt'
        task = asyncio.create_task(download_data(url, filename))
        async_tasks.append(task)

    await asyncio.gather(*async_tasks)

    print(f'Время выполнения: {(time() - start_time):.10f}')


if __name__ == '__main__':
    asyncio.run(main())
