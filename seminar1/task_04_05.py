"""
Задание №4.
 Написать функцию, которая будет принимать на вход строку и
выводить на экран ее длину.
Задание №5.
 Написать функцию, которая будет выводить на экран HTML
страницу с заголовком "Моя первая HTML страница" и
абзацем "Привет, мир!".
"""
from flask import Flask

app = Flask(__name__)

html = """
<h1>Моя первая HTML страница!</h1>
<p>Привет, мир!</p>
"""


@app.route('/')  # Как заглушка если после http://127.0.0.1:5000/ нет ничего
def hello_world():
    return 'Hello World!'


@app.route('/length/<text>/')
def length_html(text):
    return str(len(text))  # выдаст + один символ если будет пробел


@app.route('/web/')
def web_html():
    return html


if __name__ == '__main__':
    app.run()
