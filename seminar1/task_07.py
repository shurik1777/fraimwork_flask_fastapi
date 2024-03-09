"""
Задание №7.
    Написать функцию, которая будет выводить на экран HTML
страницу с блоками новостей.
Каждый блок должен содержать заголовок новости,
краткое описание и дату публикации.
Данные о новостях должны быть переданы в шаблон через
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

news_content = [{'title': 'Main_news',
                 'description': 'safgafafaf',
                 'date': '2024-03-09',
                 },
                {'title': 'Holiday',
                 'description': '8emarta',
                 'date': '2024-03-08',
                 }, ]


@app.route('/table/')
def table():  # сюда не нужно ничего передавать!
    return render_template("table.html", users=_users)


@app.route('/news/')
def news_html():
    return render_template("news.html", content=news_content)


if __name__ == '__main__':
    app.run()
