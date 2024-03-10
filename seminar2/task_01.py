"""
Задание №1.
Создать страницу на которой будет кнопка "Нажми меня",
при нажатии на которую будет переход на другую страницу с
приветствием пользователя по имени.
"""
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index() -> str:
    return render_template('about.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        return f'{name} submitted!'
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)
