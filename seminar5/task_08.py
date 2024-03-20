"""
Задание №8.
Необходимо создать API для управления списком задач. Каждая задача должна
содержать заголовок и описание. Для каждой задачи должна быть возможность
указать статус (выполнена/не выполнена).
API должен содержать следующие конечные точки:
○ GET /tasks - возвращает список всех задач.
○ GET /tasks/{id} - возвращает задачу с указанным идентификатором.
○ POST /tasks - добавляет новую задачу.
○ PUT /tasks/{id} - обновляет задачу с указанным идентификатором.
○ DELETE /tasks/{id} - удаляет задачу с указанным идентификатором.
Для каждой конечной точки необходимо проводить валидацию данных запроса и
ответа. Для этого использовать библиотеку Pydantic.
"""
from pathlib import Path

for path, directories, files in Path('yuore_path').walk():
    print(path, directories, files)
