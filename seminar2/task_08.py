"""
Задание №8.
Создать страницу, на которой будет форма для ввода имени
и кнопка "Отправить"
При нажатии на кнопку будет произведено
перенаправление на страницу с flash сообщением, где будет
выведено "Привет, {имя}!".
"""
from flask import Flask, render_template, redirect, url_for, request, flash

app = Flask(__name__)
app.secret_key = '6cfb0f19c1e505e1e715b2ea4622858012176f59f9d21af0ea5fe99825320663'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        flash(f'Привет, {name}!')
        return redirect(url_for('message'))
    return render_template('index.html')


@app.route('/message')
def message():
    return render_template('message.html')


if __name__ == '__main__':
    app.run(debug=True)
