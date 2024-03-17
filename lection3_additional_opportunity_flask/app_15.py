from flask import Flask
from flask_wtf.csrf import CSRFProtect

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


@app.route('/form', methods=['GET', 'POST'])
@csrf.exempt
def my_form():
    ...
    return 'NO CSRF protected!'


if __name__ == '__main__':
    app.run(debug=True)
