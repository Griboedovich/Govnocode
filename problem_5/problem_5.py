import csv


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
	Создаёт новую таблицу с логинами и паролями

	data -  данные для новой таблицы
	"""
	with open('students_with_hash.csv', 'w') as csvfile:
		for row in data:
			csv_write = csv.writer(csvfile)
			csv_write.writerow(row)

def hash_gennerated(FIO):
	"""
	Создаёт хеш ФИО строки

	FIO -  текстовая строка содержащая ФИО
	"""
	
	bykovki = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', 'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', ' ']
	
	s = {}
	p = 67
	m = 10**9 + 9
	
	for i in range(len(bykovki)):
		s[bykovki[i]] = i+1
	
	hash = 0

	for j in range(len(FIO)):
		hash += s[FIO[j]]*(p**j)
	return hash % m
	
	
	

def change_data(data):
	"""
	Изменяет данные, а именно id изменяет на хэш

	data -  данные таблицы
	"""
	new_data = [data[0]]
	 
	for row in data[1:]:
		row[0] = hash_gennerated(row[1])
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
