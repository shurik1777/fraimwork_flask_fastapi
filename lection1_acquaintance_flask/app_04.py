from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/<name>/')
def hello(name='Незнакомец'):
    return f'Привет, {name.capitalize()}!'


@app.route('/file/<path:file>')  # если переменную file убрать, то будет 404 ошибка
def set_path(file):
    print(type(file))
    return f'Путь до файла {file}'


@app.route('/number/<float:num>')  # при отрицательном значении - будет 404
def set_number(num):
    print(type(num))
    return f'Передано число {num}'


if __name__ == '__main__':
    app.run(debug=True)