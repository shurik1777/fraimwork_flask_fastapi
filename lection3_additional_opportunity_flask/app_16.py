from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect

from forms_3 import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = b'fd7d71c236032a5118354f0fa7f3442dbc2bb7a37ded0ffeefbc11609fb32c72'
csrf = CSRFProtect(app)
"""
Генерация надёжного секретного ключа
>>> import secrets
>>> secrets.token_hex()
"""


@app.route('/')
def index():
    return 'Hi!'


@app.route('/data/')
def data():
    return 'data'


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        # Обработка данных из формы
        pass
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
