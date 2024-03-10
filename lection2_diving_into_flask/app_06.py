"""
Функция-представление может быть разделена на две.
Каждая обработает свой вид запроса
"""
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi'


@app.get('/submit')
def submit_get():
    return render_template('form.html')


@app.post('/submit')  # функцию декорирования можно менять на горячую
def submit_post():
    name = request.form.get('name')
    return f'Hello {name}!'


if __name__ == '__main__':
    app.run(debug=True)
