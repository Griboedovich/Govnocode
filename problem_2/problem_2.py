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
	
def vstavka_sort(ndata):
	"""
	Сортирует данные методом сортировки вставками
	
	ndata - данные об участниках, без title строки
	"""
	data = ndata
	mx = None
	mxind = 0
	for i in range(len(data)):
		if data[i][4].isdigit():
			if mx == None or int(mx) > int(data[i][4]):
				mx = data[i][4]
				mxind = i
		else:
			data[i][4] = 0
	data[mxind], data[0] = data[0], data[mxind]
	
	for i  in range(1, len(data)):
		object = data[i]
		
		j = i-1

		while j >= 0 and int(data[j][4]) < int(object[4]):
			data[j+1] = data[j]
			j-=1

		data[j + 1] = object 
	return data
	
def search_ten(sort_data):
	"""
	Ищет в отсортированых в порядке убывания данных учеников 10-ч классов
	
	sort_data - отсортированыу в порядке убывания данные
	"""
	ten_data = []
	for row in sort_data:
		if row[3][:2] == '10':
			ten_data.append(row)
	return ten_data	
	
def liders(liders_list):
	"""
	Возвращает список с ИФ первых 3 мест в данном списке участников
	
	liders_list - список участников, отсортированый в порядке убывания
	"""
	lider_names = []
	for i in range(3):
		mas = liders_list[i][1].split()
		lider_names.append(f"{mas[1][0]}. {mas[0]}")
	return lider_names
	
def main():
	"""
	Точка входа
	"""

	data = take_data()
	new_data = (vstavka_sort(data[1:]))
	
	liders_ten = search_ten(new_data)
	
	res = liders(liders_ten)
	
	print(f"10 класс:\n1 место: {res[0]}\n2 место: {res[1]}\n3 место: {res[2]}")
	
main()
