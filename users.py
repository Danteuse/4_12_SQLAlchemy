import sqlalchemy as sa

from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base


DB_PATH = "sqlite:///sochi_athletes.sqlite3"

Base = declarative_base()

class User(Base):
	
    # задаем название таблицы
	__tablename__ = 'user'
    # идентификатор пользователя, первичный ключ
	id = sa.Column(sa.Integer, primary_key = True)
    # имя пользователя
	first_name = sa.Column(sa.Text)
    # фамилия пользователя
	last_name = sa.Column(sa.Text)
    # пол пользователя
	gender = sa.Column(sa.Text)
    # электронка пользователя
	email = sa.Column(sa.Text)
    # день рождения
	birthdate = sa.Column(sa.Text)
    # рост
	height = sa.Column(sa.Text)

def connect_db():
	
    # создаем соединение к базе данных
	engine = sa.create_engine(DB_PATH)
    # создаем описанные таблицы
	Base.metadata.create_all(engine)
    # создаем фабрику сессий
	session = sessionmaker(engine)
    # возвращаем сессию
	return session()

def request_data():
	
	print("Привет! Я запишу твои данные, кожаный мешок с костями!")
	
	first_name = input("Введи свое презренное имя: ")
	last_name = input("А теперь человеческую фамилию: ")
	gender = input("Какой у тебя пол, человек: ")
	email = input("Мне еще понадобится адрес твоей электронки: ")
	birthdate = input("День появления на свет в формате ГГГГ-ММ-ДД: ")
	height = input("Рост: ")
	
	#создаем нового пользователя
	user = User(
		#id = user_id,
		first_name = first_name,
		last_name = last_name,
		gender = gender,
		email = email,
		birthdate = birthdate,
		height = height
	)
	#возвращаем созданного пользователя
	return user


def main():
	
	session = connect_db()
    
	user = request_data()
		
	session.add(user)
		
	session.commit()
	print("Спасибо, данные сохранены!")
	
if __name__ == '__main__':
	main()

