from app import db, login_manager
from flask_login import UserMixin

# декоратор, который сообщает Flask, что функция будет использоваться для загрузки пользователя по его ID
@login_manager.user_loader
def load_user(user_id):
    # отправляем в БД запрос для поиска юзера по ID
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):  # Функция, чтобы представить информацию о пользователе в виде одной строки
        return f'User: {self.username}, email: {self.emai}'
