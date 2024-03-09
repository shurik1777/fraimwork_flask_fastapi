"""
Задание №8.
    Создать базовый шаблон для всего сайта, содержащий
общие элементы дизайна (шапка, меню, подвал), и
дочерние шаблоны для каждой отдельной страницы.
Например, создать страницу "О нас" и "Контакты",
используя базовый шаблон.
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/main/')
def main():
    return render_template('all_for_us.html')


@app.route('/jacket/')
def jacket():
    return render_template('jacket.html')


@app.route('/shoes/')
def shoes_html():
    return render_template('shoes.html')


@app.route('/clothing/')
def clothing_html():
    return render_template('clothing.html')


@app.route('/data/')
def data():
    return render_template('all_contact.html')


if __name__ == '__main__':
    app.run()
