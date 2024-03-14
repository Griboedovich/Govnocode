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
	
	

def obrabotka(data):
	"""
	Строит словарь со значением средний оценки по классу и ключем класса
	
	data -  данные для обработке и построение словаря
	"""
	score_table = {}
	class_mas = []
	table = {}
	
	for row in data:
		class_number = row[3]
		if not (class_number in class_mas):
			class_mas.append(class_number)
			table[class_number] = []
		else:
			table[class_number].append(row[4])
	
	for class_number in class_mas:
	
		score_mas = []
		
		for score in table[class_number]:
			if score.isdigit():
				score_mas.append(int(score))
				
		res_score = sum(score_mas) / len(score_mas)
		
		score_table[class_number] = str(round(res_score,3))
	return score_table
		
		
	
def fix_data(data, score_table):
	"""
	Заменяет ошибки в поле оценки на среднию оценку по классу

	data -  данные таблицы
	score_table - словарь со значением средний оценки по классу и ключем класса
	"""
	new_data = [data[0]]
	for row in data[1:]:
		if not row[4].isdigit():
	 		row[4] = score_table[row[3]]
		new_data.append(row)
	return new_data
	
	
def create_newtable(data):
	"""
	Создаёт таблицу student_new.csv с исправлеными значенями оценки

	data -  данные таблицы
	"""
	with open('student_new.csv', 'w') as csvfile:
		for row in data:
			csv_write = csv.writer(csvfile)
			csv_write.writerow(row)

def search(name, data):
	"""
	Ищет в данных по Ф или ФИ или ФИО человека id проекта и оценку за него 

	data -  данные таблицы
	name - Ф или ФИ или ФИО человека чей id проекта и оценку нужно найти
	"""
	score = None
	project = None
	for row in data:
		if name in row[1]:
			score = row[4]
			project = row[2]
	return score, project

def main():
	"""
	Точка входа
	"""

	data = take_data()

	score_table = obrabotka(data[1:])
	
	new_data = fix_data(data, score_table)
	
	create_newtable(new_data)
	
	score, project = search("Хадаров Владимир", new_data)
	print(f"Ты получил: {score}, за проект - {project}")	
	
main()
