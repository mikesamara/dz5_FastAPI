'''
Создать веб-страницу для отображения списка пользователей. Приложение
должно использовать шаблонизатор Jinja для динамического формирования HTML
страницы.
Создайте модуль приложения и настройте сервер и маршрутизацию.
Создайте класс User с полями id, name, email и password.
Создайте список users для хранения пользователей.
Создайте HTML шаблон для отображения списка пользователей. Шаблон должен
содержать заголовок страницы, таблицу со списком пользователей и кнопку для
добавления нового пользователя.
Создайте маршрут для отображения списка пользователей (метод GET).
Создайте маршрут для удаления информации о пользователе (метод DELETE).
Создайте маршрут для обновления информации о пользователе (метод PUT).
Создайте маршрут для добавления нового пользователя (метод POST).
Реализуйте вывод списка пользователей через шаблонизатор Jinja.
'''
from fastapi import FastAPI, Request

from pydantic import BaseModel
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="./dz5/templates")

class User(BaseModel):
    user_id: int
    name: str
    email: str
    password: str


users = [
    User(user_id=1, name='User 1', email='user1@email', password="user1"),
    User(user_id=2, name='User 2', email='user1@email', password="user2"),
    User(user_id=3, name='User 3', email='user1@email', password="user3"),
    User(user_id=4, name='User 4', email='user1@email', password="user4"),
    User(user_id=5, name='User 5', email='user1@email', password="user5"),
    User(user_id=6, name='User 6', email='user1@email', password="user6")
]


@app.get('/', response_class=HTMLResponse)
async def main(request: Request):
    return templates.TemplateResponse('index.html', {'request': request, 'users':users})


@app.post('/new_user')
async def create_movie(new_user: User):
    users.append(new_user)
    return users

@app.put('/put_user')
async def put_user(user_id_put: int, user: User):
    for i in range(len(users)):
        if users[i].user_id == user_id_put:
            users[i] = user
    return {'id_user' : user_id_put}

@app.delete('/delete_user')
async def delete_user(user_id: int):
    for i in range(len(users)):
        if users[i].user_id == user_id:
            del users[i]
    return {'id_user': user_id}


