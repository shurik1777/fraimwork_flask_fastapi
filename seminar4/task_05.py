"""
Задание №5.
� Создать программу, которая будет производить подсчет
количества слов в каждом файле в указанной директории и
выводить результаты в консоль.
� Используйте процессы.
"""
import os
import multiprocessing
import time


def count_words_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            word_count = len(content.split())
            print(f'File: {file_path}, Word Count: {word_count}')
    except Exception as e:
        print(f'Error processing file: {file_path}, {e}')


def process_files_in_directory(directory):
    processes = []

    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path):
            process = multiprocessing.Process(target=count_words_in_file, args=(file_path,))
            processes.append(process)
            process.start()

    for process in processes:
        process.join()


if __name__ == '__main__':
    start_time = time.time()
    directory = r'C:\Users\shuri\OneDrive\Рабочий стол\fraimwork_flask_fastapi\seminar4\output'
    process_files_in_directory(directory)
    print(f'Execution time: {(time.time() - start_time):.3f} seconds')
