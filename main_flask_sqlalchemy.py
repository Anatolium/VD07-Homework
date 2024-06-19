from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Создаём контекст приложения
with app.app_context():
    # Создаём базу данных
    db.create_all()

# С помощью декоратора создаём маршрут, который будет вызывать функцию
@app.route('/add_user')
def add_user():
    new_user = User(username='new_username')
    # Добавляем в сессию, сессия – это "временное хранилище перед добавлением в БД"
    db.session.add(new_user)
    # Сохраняем изменения в базу данных
    db.session.commit()
    return 'User added'

@app.route('/users')
def get_users():
    # Получаем всех юзеров из базы данных
    users = User.query.all()
    return str(users)

if __name__ == '__main__':
    app.run(debug=True)

