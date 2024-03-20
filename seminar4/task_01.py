"""
Задание №1.
� Написать программу, которая считывает список из 10 URL адресов
 и одновременно загружает данные с каждого адреса.
� После загрузки данных нужно записать их в отдельные
файлы.
� Используйте потоки.
"""
from pathlib import Path
from threading import Thread
from time import time

import requests


# Функция для загрузки данных по URL и записи в файл
def download_data(url, filename):
    response = requests.get(url)
    output_path = Path('output') / filename
    with open(output_path, 'wb') as file:
        file.write(response.content)
#

# Список URL адресов
urls = [
    'http://zagonka11.zagonkop.gb.net/108140-kotiki-2022-onlayn.html',
    'http://www.nnzoo.ru/animals.html'
]

if __name__ == '__main__':
    start_time = time()
    # Создаем и запускаем потоки для загрузки данных
    threads = []
    for i, url in enumerate(urls):
        filename = f'data_{i}.txt'
        thread = Thread(target=download_data, args=(url, filename))
        threads.append(thread)
        thread.start()

    # Ждем завершения всех потоков
    for thread in threads:
        thread.join()

    print(f'Время выполнения: {(time() - start_time):.10f}')
