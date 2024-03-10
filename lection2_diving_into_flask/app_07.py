"""
Загрузка файлов через POST запрос
"""
from flask import Flask, request, render_template
from pathlib import PurePath, Path  # для работы с файлами
from werkzeug.utils import secure_filename

# secure_filename для работы с преобразованием имени с целью обезопасить
# пересылаемую информацию

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi'


@app.route('/upload', methods=['GET', 'POST'])
def upload():  # Работает с двумя видами запросов
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'uploads',
                                    file_name))
        # Уточнение если не будет создана директория uploads
        # - то будут ошибки не найденных путей
        return f"Файл {file_name} загружен на сервер"
    return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)
