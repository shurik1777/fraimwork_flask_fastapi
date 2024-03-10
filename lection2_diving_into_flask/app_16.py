"""
Сессии в Flask являются способом сохранения данных между запросами. Это может
быть полезно, например, для хранения информации о пользователе после
авторизации или для сохранения состояния формы при перезагрузке страницы.
Для работы с сессиями в Flask используется объект session. Он представляет собой
словарь, который можно использовать для записи и чтения данных. По сути сессия
— продвинутая версия cookies файлов.
"""
from flask import Flask, request, make_response, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = b'6cfb0f19c1e505e1e715b2ea4622858012176f59f9d21af0ea5fe99825320663'


@app.route('/')
def index():
    if 'username' in session:
        return f'Hello, {session["username"]}'
    else:
        return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form.get('username') or 'NoName'
        return redirect(url_for('index'))
    return render_template('username_form.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
