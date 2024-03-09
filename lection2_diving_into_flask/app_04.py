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


if __name__ == '__main__':
    app.run(debug=True)
