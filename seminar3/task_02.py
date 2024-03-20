"""
Задание №2.
Создать базу данных для хранения информации о книгах в библиотеке.
База данных должна содержать две таблицы: "Книги" и "Авторы".
В таблице "Книги" должны быть следующие поля: id, название, год издания,
количество экземпляров и id автора.
В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.
Необходимо создать связь между таблицами "Книги" и "Авторы".
Написать функцию-обработчик, которая будет выводить список всех книг с
указанием их авторов.
"""
from flask import Flask, render_template
from models_lib import Book, Author
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
db = SQLAlchemy(app)


@app.route('/')
def index():
    books = Book.query.all()
    return render_template(
        'templates/index.html', books=books)


@app.route('/authors/')
def authors_page():
    authors = Author.query.all()
    return render_template(
        'authors.html', authors=authors)


@app.cli.command('init-db')
def initdb_command():
    db.create_all()
    print('Initialized the database.')


@app.cli.command('fill-db')
def fill_db():
    count = 10
    for authors in range(1, count + 1):
        new_authors = Author(
            first_name='John', last_name='Doe'
        )
        # authors = [
    #     Author(first_name='John', last_name='Doe'),
    #     Author(first_name='Anna', last_name='Smith'),
    #     Author(first_name='Peter', last_name='Jones'),
    #     # Можно добавить еще авторов здесь
    # ]
    #
    # books = [
    #     Book(title='Title 1', year=2020, copies=100, author=authors[0]),
    #     Book(title='Title 2', year=2021, copies=200, author=authors[1]),
    #     Book(title='Title 3', year=2022, copies=300, author=authors[2]),
    #     # Можно добавить еще книги здесь
    # ]
    #
    # for author in authors:
    #     db.session.add(author)
    # for book in books:
    #     db.session.add(book)
    # db.session.commit()


if __name__ == '__main__':
    app.run(debug=True)
