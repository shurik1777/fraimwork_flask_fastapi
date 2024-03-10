from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = b'6cfb0f19c1e505e1e715b2ea4622858012176f59f9d21af0ea5fe99825320663'


@app.route('/')
def index():
    return 'Добро пожаловать на главную страницу!'


@app.route('/form/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Обработка данных формы
        if not request.form['name']:
            flash('Введите имя!', 'danger')
            return redirect(url_for('form'))
        flash('Форма успешно отправлена!', 'success')
        return redirect(url_for('form'))
    return render_template('flash_form.html')


if __name__ == '__main__':
    app.run(debug=True)
