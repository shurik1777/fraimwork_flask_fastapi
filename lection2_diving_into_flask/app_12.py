"""
Flash сообщения в Flask являются способом передачи информации между
запросами.
 Это может быть полезно, например, для вывода сообщений об
успешном выполнении операции или об ошибках ввода данных.
Для работы с flash сообщениями используется функция flash().
Она принимает сообщение и категорию, к которой это сообщение относится,
и сохраняет его во временном хранилище.
"""
from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = b'6cfb0f19c1e505e1e715b2ea4622858012176f59f9d21af0ea5fe99825320663'
"""
Генерация надёжного секретного ключа из python console
>>> import secrets
>>> secrets.token_hex()
"""


@app.route('/')
def index():
    return 'Добро пожаловать на главную страницу!'


@app.route('/form/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Обработка данных формы
        flash('Форма успешно отправлена!', 'success')
        return redirect(url_for('form'))
    return render_template('flash_form.html')


if __name__ == '__main__':
    app.run(debug=True)
