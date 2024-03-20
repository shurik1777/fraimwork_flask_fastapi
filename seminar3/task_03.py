"""
Задание №3.
Доработаем задача про студентов.
Создать базу данных для хранения информации о студентах и их оценках в
учебном заведении.
База данных должна содержать две таблицы: "Студенты" и "Оценки".
В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, группа
и email.
В таблице "Оценки" должны быть следующие поля: id, id студента, название
предмета и оценка.
Необходимо создать связь между таблицами "Студенты" и "Оценки".
Написать функцию-обработчик, которая будет выводить список всех
студентов с указанием их оценок.
"""
from flask import Flask, render_template
from models import db, Gender, Faculty, Student, Grade
from random import choice, randint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase_sem31.db'
db.init_app(app)


@app.route('/')
def index():
    return render_template('index_t1.html')


@app.route('/students/')
def students():
    students = db.session.query(Student).all()
    grades_data = []
    for student in students:
        grades = db.session.query(Grade).filter_by(student_id=student.id).all()
        grades_data.append((student, grades))
    return render_template('students.html', grades=grades_data)


@app.cli.command('init-db')
def initdb_command():
    db.create_all()
    print('Initialized the database.')


@app.cli.command('fill-db')
def fill_db():
    # Добавляем студентов
    count = 10
    for student in range(1, count + 1):
        new_student = Student(
            name=f'student{student}',
            last_name=f'last_name{student}',
            age=choice([student, student * 5]),
            gender=choice([Gender.male, Gender.female]),
            group=f'group{student}',
            faculty_id=randint(1, 10),
            email=f'student{student}@example.com'
        )
        db.session.add(new_student)
    db.session.commit()

    # Добавляем факультеты
    for faculty in range(1, count):
        new_faculty = Faculty(faculty_name=f'faculty{faculty}')
        db.session.add(new_faculty)
    db.session.commit()

    # Добавляем оценки
    for student in db.session.query(Student).all():
        grade = Grade(student_id=student.id,
                      subject_name='Math',
                      grade=randint(2, 5))
        db.session.add(grade)
    db.session.commit()


if __name__ == '__main__':
    app.run(debug=True)
