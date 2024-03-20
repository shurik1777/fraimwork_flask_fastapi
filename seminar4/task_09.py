"""
Задание №9.
� Написать программу, которая скачивает изображения с заданных URL-адресов и
сохраняет их на диск. Каждое изображение должно сохраняться в отдельном
файле, название которого соответствует названию изображения в URL-адресе.
� Например URL-адрес: https://example/images/image1.jpg -> файл на диске:
image1.jpg
� Программа должна использовать многопоточный, многопроцессорный и
асинхронный подходы.
� Программа должна иметь возможность задавать список URL-адресов через
аргументы командной строки.
� Программа должна выводить в консоль информацию о времени скачивания
каждого изображения и общем времени выполнения программы.
"""
## Многопоточный

import requests
import os
import time
import threading
import sys


def download_image(url):
    response = requests.get(url)
    if response.status_code == 200:
        filename = url.split('/')[-1]
        path = os.path.join('images', filename)  # Путь к папке "images" и имени файла
        os.makedirs('images', exist_ok=True)  # Создание папки "images", если её не существует
        with open(path, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded {filename}")
    else:
        print(f"Failed to download {url}")


def multi_threaded_downloader(urls):
    start_time = time.time()
    threads = []
    for url in urls:
        thread = threading.Thread(target=download_image, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"Total execution time: {end_time - start_time} seconds")


if __name__ == "__main__":
    urls = sys.argv[1:]
    if not urls:
        print("Usage: python program.py <url1> <url2> ...")
        sys.exit(1)

    multi_threaded_downloader(urls)
# python task_09.py http://o-keramika.ru/wa-data/public/shop/products/02/10/1002/images/1172/1172.750.jpg http://o-keramika.ru/wa-data/public/shop/products/38/16/1638/images/2842/2842.750.jpg

## Многопроцессорный
# import requests
# import os
# import time
# import multiprocessing
# import sys
# 
# 
# def download_image(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         filename = url.split('/')[-1]
#         path = os.path.join('images', filename)  # Путь к папке "images" и имени файла
#         os.makedirs('images', exist_ok=True)  # Создание папки "images", если её не существует
#         with open(path, 'wb') as file:
#             file.write(response.content)
#         print(f"Downloaded {filename}")
#     else:
#         print(f"Failed to download {url}")
# 
# 
# def multi_process_downloader(urls):
#     start_time = time.time()
#     processes = []
#     for url in urls:
#         process = multiprocessing.Process(target=download_image, args=(url,))
#         processes.append(process)
#         process.start()
# 
#     for process in processes:
#         process.join()
# 
#     end_time = time.time()
#     print(f"Total execution time: {end_time - start_time} seconds")
# 
# 
# if __name__ == "__main__":
#     urls = sys.argv[1:]
#     if not urls:
#         print("Usage: python program.py <url1> <url2> ...")
#         sys.exit(1)
# 
#     multi_process_downloader(urls)
## Ассинхронный
# import aiohttp
# import aiofiles
# import asyncio
# import os
# import sys
# import time
#
# async def download_image(url):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             if response.status == 200:
#                 filename = url.split('/')[-1]
#                 path = os.path.join('images', filename)  # Путь к папке "images" и имени файла
#                 os.makedirs('images', exist_ok=True)  # Создание папки "images", если её не существует
#                 async with aiofiles.open(path, 'wb') as file:
#                     await file.write(await response.read())
#                 print(f"Downloaded {filename}")
#             else:
#                 print(f"Failed to download {url}")
#
# async def async_downloader(urls):
#     start_time = time.time()
#     tasks = [download_image(url) for url in urls]
#     await asyncio.gather(*tasks)
#     end_time = time.time()
#     print(f"Total execution time: {end_time - start_time} seconds")
#
# if __name__ == "__main__":
#     urls = sys.argv[1:]
#     if not urls:
#         print("Usage: python program.py <url1> <url2> ...")
#         sys.exit(1)
#
#     asyncio.run(async_downloader(urls))
