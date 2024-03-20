"""
Задание №8.
� Напишите программу, которая будет скачивать страницы из
списка URL-адресов и сохранять их в отдельные файлы на
диске.
� В списке может быть несколько сотен URL-адресов.
� При решении задачи нужно использовать многопоточность,
многопроцессорность и асинхронность.
� Представьте три варианта решения.
"""
import asyncio
import aiohttp
import os
import time

url_list = ["http://zagonka11.zagonkop.gb.net/108140-kotiki-2022-onlayn", "http://www.nnzoo.ru/animals"]


async def download_page(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            content = await response.read()
            # Извлекаем имя сайта из URL
            website_name = url.split('//')[1]
            # Создаем директорию, если её нет
            if not os.path.exists(website_name):
                os.makedirs(website_name)
            with open(f"{website_name}/index.html", "wb") as file:
                file.write(content)


async def main():
    tasks = [download_page(url) for url in url_list]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(main())
    print(f'Время выполнения: {(time.time() - start_time):.10f}')
# urls = ['http://zagonka11.zagonkop.gb.net/108140-kotiki-2022-onlayn.html', 'http://www.nnzoo.ru/animals.html']
