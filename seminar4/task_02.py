"""
Задание №2.
� Написать программу, которая считывает список из 10 URLадресов и одновременно загружает данные с каждого
адреса.
� После загрузки данных нужно записать их в отдельные
файлы.
� Используйте процессы.
"""
from multiprocessing import Process
from time import time
from pathlib import Path
import requests


def download_data(url, filename):
    response = requests.get(url)
    output_path = Path('output') / filename
    with open(output_path, 'wb') as file:
        file.write(response.content)


urls = [
    'http://zagonka11.zagonkop.gb.net/108140-kotiki-2022-onlayn.html',
    'http://www.nnzoo.ru/animals.html'
]

if __name__ == '__main__':
    start_time = time()
    processes = []

    for i, url in enumerate(urls):
        filename = f'data_{i}.txt'
        process = Process(target=download_data, args=(url, filename))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print(f'Execution time: {(time() - start_time):.10f}')
