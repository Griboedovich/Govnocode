import csv
import random

def take_data():
	"""
	Считывает файл students.csv 
	"""

	data = []

	with open('students.csv') as file:
		csv_read = csv.reader(file)
		for row in csv_read:
			data.append(row)
	return data

def create_newtable(data):
	"""
	Создаёмт новую таблицу с логинами и паролями

	data -  данные для новой таблицы
	"""
	with open('students_password.csv', 'w') as csvfile:
		for row in data:
			csv_write = csv.writer(csvfile)
			csv_write.writerow(row)
		
def generate_login(FIO):
	"""
	Генерирует логин на основе ФИО

	FIO -  строка содержащая ФИО
	"""
	return FIO[0] + '_' + FIO[1][0] + FIO[2][0] 
	
def generate_password():
	"""
	Генерирует пароль который содержит заглавные, прописные символы англ алфавита а также цифры. состоит из 8 символов
	"""
	
	password = []
	
	S = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	s = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	
	Sx = random.randint(1,6)
	sy = random.randint(1,7-Sx)
	nz = 8 - (Sx+sy)
	
	for i in range(Sx):
		password.append(random.choice(S))
	for j in range(sy):
		password.append(random.choice(s))
	for k in range(nz):
		password.append(str(random.randint(0,9)))
	
	random.shuffle (password)
	
	res_pass = ''
	for i in password:
		res_pass += i
	
	return res_pass

def change_data(data):
	"""
	Обновляет данные таблицы, добавляет логин и пароль каждому пользователю

	data -  данные из таблицы для редактирования
	"""
	new_data = [data[0]]
	 
	for row in data[1:]:
		row.append(generate_login(row[1].split()))
		row.append(generate_password())
		new_data.append(row)
	return new_data

def main():
	"""
	Точка входа
	"""

	data = take_data()
	new_data = change_data(data)
	
	create_newtable(new_data)
	
main()
