"""
Задание №2.
 Дорабатываем задачу 1.
Добавьте две дополнительные страницы в ваше веб-приложение:
○ страницу "about"
○ страницу "contact"
Задание №3.
 Написать функцию, которая будет принимать на вход два
числа и выводить на экран их сумму.
"""
from flask import Flask, render_template  # в этом коде можно через render_template, а можно без

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/contact/')
def contact_html():
    # return '.templates/contact.html'
    return render_template('contact.html', title='Contact')


@app.route('/about/')
def about_html():
    return '.templates/about.html'
    # return render_template('about.html', title='About')


@app.route('/sum/<int:num1>/<int:num2>/')  # маршруты должны быть всегда корректны с передаваемыми аргументами
def sum_html(num1, num2):
    return str(num1 + num2)


if __name__ == '__main__':
    app.run()
