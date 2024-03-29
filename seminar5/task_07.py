"""
Задание №7.
Создать RESTful API для управления списком задач. Приложение должно
использовать FastAPI и поддерживать следующие функции:
○ Получение списка всех задач.
○ Получение информации о задаче по её ID.
○ Добавление новой задачи.
○ Обновление информации о задаче по её ID.
○ Удаление задачи по её ID.
Каждая задача должна содержать следующие поля: ID (целое число),
Название (строка), Описание (строка), Статус (строка): "to do", "in progress",
"done".
Задание №7 (продолжение).
Создайте модуль приложения и настройте сервер и маршрутизацию.
Создайте класс Task с полями id, title, description и status.
Создайте список tasks для хранения задач.
Создайте функцию get_tasks для получения списка всех задач (метод GET).
Создайте функцию get_task для получения информации о задаче по её ID
(метод GET).
Создайте функцию create_task для добавления новой задачи (метод POST).
Создайте функцию update_task для обновления информации о задаче по её ID
(метод PUT).
Создайте функцию delete_task для удаления задачи по её ID (метод DELETE).
"""