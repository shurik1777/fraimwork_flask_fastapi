from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import enum

db = SQLAlchemy()


class Gender(enum.Enum):
    male = 'Муж'
    female = 'Жен'


class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    faculty_name = db.Column(db.String(80), nullable=False)
    student = db.relationship('Student', backref=db.backref(f'faculty'), lazy=True)

    def __repr__(self):
        return f'Faculty({self.faculty_name})'


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.Enum(Gender), nullable=False)
    group = db.Column(db.Integer, nullable=False)
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id'), nullable=False)

    def __repr__(self):
        return f'Student({self.name}, {self.last_name})'


# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(80), nullable=False)
#     content = db.Column(db.Text, nullable=False)
#     author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     created_at = db.Column(db.DateTime, default=datetime.now)

    # def __repr__(self):
    #     return f'Post({self.title}, {self.content})'
