"""
Задание №6.
    Написать функцию, которая будет выводить на экран HTML
страницу с таблицей, содержащей информацию о студентах.
Таблица должна содержать следующие поля: "Имя",
"Фамилия", "Возраст", "Средний балл".
Данные о студентах должны быть переданы в шаблон через
контекст.
"""
from flask import Flask, render_template

app = Flask(__name__)

_users = [{'name': 'Ivan',
           'last_name': 'Ivanov',
           'age': '44',
           'average_mark': '4.8',
           },
          {'name': 'Fedor',
           'last_name': 'Petrovich',
           'age': '37',
           'average_mark': '4.9',
           }, ]


@app.route('/table/')
def table():  # сюда не нужно ничего передавать!
    return render_template("table.html", users=_users)


if __name__ == '__main__':
    app.run()
