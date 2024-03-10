from flask import request, Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi'


@app.route('/get/')
def get_diving():
    if level := request.args.get('level'):
        text = f'Похоже ты опытный игрок, раз имеешь уровень {level}<br>'
    else:
        text = 'Привет, новичок.<br>'
    return f'{text} {request.args}'


"""
Перейдём по адресу http://127.0.0.1:5000/get/?name=alex&age=13&level=80 и
увидим следующий вывод:
Похоже ты опытный игрок, раз имеешь уровень 80
ImmutableMultiDict([('name', 'alex'), ('age', '13'), ('level',
'80')])
"""

if __name__ == '__main__':
    app.run(debug=True)
