"""
Задание №6.
� Создать программу, которая будет производить подсчет
количества слов в каждом файле в указанной директории и
выводить результаты в консоль.
� Используйте асинхронный подход.
"""
import os
import asyncio
from time import time


async def count_words_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            word_count = len(content.split())
            print(f'File: {file_path}, Word Count: {word_count}')
    except Exception as e:
        print(f'Error processing file: {file_path}, {e}')


async def process_files_in_directory(directory):
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path):
            await count_words_in_file(file_path)


async def main():
    directory = r'C:\Users\shuri\OneDrive\Рабочий стол\fraimwork_flask_fastapi\seminar4\output'
    await process_files_in_directory(directory)


if __name__ == '__main__':
    start_time = time()
    asyncio.run(main())
    print(f'Время выполнения: {(time() - start_time):.10f}')
# Execution time: 0.0009982586 seconds
# Время выполнени 0.0019934177
# import asyncio
# import os
# import aiofiles
# from time import time
#
# MY_PATH = r'C:\Users\shuri\OneDrive\Рабочий стол\fraimwork_flask_fastapi\seminar4'
#
#
# async def worker(file_):
#     async with aiofiles.open(file_, 'r', encoding='utf-8') as f:
#         content = await f.read()
#         print(f'Слов в {file_} : {len(content.split())}')
#
#
# async def main():
#     for root, dirs, file_name in os.walk(MY_PATH):
#         for f in file_name:
#             task = asyncio.create_task(worker(f))
#             await task
#
#
# if __name__ == '__main__':
#     start_time = time()
#     asyncio.run(main())
#     print(f'{time() - start_time}')
