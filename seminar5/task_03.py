"""
Задание №3.
Создать API для добавления нового пользователя в базу данных. Приложение
должно иметь возможность принимать POST запросы с данными нового
пользователя и сохранять их в базу данных.
Создайте модуль приложения и настройте сервер и маршрутизацию.
Создайте класс User с полями id, name, email и password.
Создайте список users для хранения пользователей.
Создайте маршрут для добавления нового пользователя (метод POST).
Реализуйте валидацию данных запроса и ответа.
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import uvicorn

app = FastAPI()


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str


users = []


@app.post("/users/", response_model=User)
def create_user(user: User):
    if any(u.email == user.email for u in users):
        raise HTTPException(status_code=400, detail="User with this email already exists")

    users.append(user)
    return user


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
