"""
Задание №4.
� Создать программу, которая будет производить подсчет
количества слов в каждом файле в указанной директории и
выводить результаты в консоль.
� Используйте потоки.
"""
# import os
# from concurrent.futures import ThreadPoolExecutor
#
#
# def count_words_in_file(file_path):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         content = file.read()
#         word_count = len(content.split())
#         print(f"{file_path}: {word_count} слов")
#
#
# def main(directory):
#     with ThreadPoolExecutor() as executor:
#         for root, _, files in os.walk(directory):
#             for file in files:
#                 file_path = os.path.join(root, file)
#                 executor.submit(count_words_in_file, file_path)
#
#
# if __name__ == "__main__":
#     directory_path = 'output'
#     main(directory_path)
import threading
import os

MY_PATH = '.'


def count_words_in_file(file_):
    with open(file_, 'r', encoding='utf-8') as f:
        content = f.read()
        num_words = len(content.split())
        print(f'Слов в файле {file_}: {num_words}')


def process_files_in_directory(directory):
    threads = []

    for root, dirs, file_names in os.walk(directory):
        for file_name in file_names:
            file_path = os.path.join(root, file_name)
            t = threading.Thread(target=count_words_in_file, args=(file_path,))
            threads.append(t)
            t.start()

    for t in threads:
        t.join()


if __name__ == "__main__":
    process_files_in_directory(MY_PATH)
