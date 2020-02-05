import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_PATH = "sqlite:///sochi_athletes.sqlite3"
Base = declarative_base()

class User(Base):

	__tablename__ = "user"
	id = sa.Column(sa.Integer, primary_key = True)
	first_name = sa.Column(sa.Text)
	last_name = sa.Column(sa.Text)
	gender = sa.Column(sa.Text)
	email = sa.Column(sa.Text)
	birthdate = sa.Column(sa.Text)
	height = sa.Column(sa.Float)

def connect_data_base():

	engine = sa.create_engine(DB_PATH)
	Base.metadata.create_all(engine)
	session = sessionmaker(engine)
	return session()

def request_data():

	print("Здравствуйте! Предоставьте ваши данные!")
	first_name = input("Введите имя: ")
	last_name = input("Введите фамилию: ")
	gender = input("Пол (допускаемые варианты: Male(мужской), Female(женский): ")
	email = input("Введите действующий адресс электронной почты: ")
	birthdate = input("Дата рождения (в формате ГГГГ-ММ-ДД): ")
	height = input("Введите рост (в формате - м.см. Например - 1.83): ")
	user = User(
		first_name = first_name,
		last_name = last_name,
		gender = gender,
		email = email,
		birthdate = birthdate,
		height = height,
		)
	return user

def main():

	session = connect_data_base()
	user = request_data()
	session.add(user)
	session.commit()
	print("Данные записаны в базуr данных!")

if __name__ == "__main__":
	main()
