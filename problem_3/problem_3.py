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
	
def line_search(data, project):
	"""
	Ищет информацию в данных учапстников по id проекта
	
	data - данные об участниках, без title строки
	project - id проекта
	"""
	for i in range(len(data)):
		if data[i][2] == project:
			return data[i]
	return None

def loop(data):
	"""
	цикл который принимает запрос, отсеивает невозможные значения запроса, цикл останавливается по команде "СТОП", если запрос коректный - то отправляет егот на линейный поиск по данным
	
	data - данные об участниках, без title строки
	"""
	while 1:
		zapros = input()
		if zapros == "СТОП":
			break
		if not(zapros.isdigit()):
			print("Ничего не найдено")
		else:
			search_res = line_search(data,zapros)
			if search_res is None:
				print("Ничего не найдено")
			else:
				print(f"Проект № {search_res[2]} делал: {search_res[1].split()[1][0]}. {search_res[1].split()[0]} он(а) получил(а) оценку - {search_res[4]}")
			

def main():
	"""
	Точка входа

	"""

	data = take_data()[1:]
	
	loop(data)
	
main()
