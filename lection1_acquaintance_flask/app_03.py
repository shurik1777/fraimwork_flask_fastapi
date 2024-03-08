from flask import Flask
"""
Множественное декорирование
Одна функция-представление может быть декорирована несколькими
декораторами.
@app.route('/Фёдор/')
@app.route('/Fedor/')
@app.route('/Федя/')
def fedor():
return 'Привет, Феодор!'
Функция представления имеет три декоратора. При переходе по любому из этих
адресов в браузере отобразится одна и та же строка «Привет, Феодор!».
"""
app = Flask(__name__)


@app.route('/')
def index():
    return 'Привет, незнакомец!'


@app.route('/Фёдор/')
@app.route('/Fedor/')
@app.route('/Федя/')
def fedor():
    return 'Привет, Феодор!'


if __name__ == '__main__':
    app.run(debug=True)
