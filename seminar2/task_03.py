"""
Задание №3.
Создать страницу, на которой будет форма для ввода логина
и пароля
При нажатии на кнопку "Отправить" будет произведена
проверка соответствия логина и пароля и переход на
страницу приветствия пользователя или страницу с
ошибкой.
"""
from flask import Flask, render_template, request


app = Flask(__name__)

LOGIN = 'admin'
PASSWORD = '123'
@app.route('/', methods=['GET', 'POST'])
# @app.route('/login/')
def login_():
    if request.method == 'GET':
        return render_template('login.html')

    get_login = request.values.get('login')
    get_password = request.values.get('password')
    if get_login == LOGIN and get_password == PASSWORD:
        return render_template('index.html')
    return render_template('error.html')


if __name__ == '__main__':
    app.run(debug=True)
