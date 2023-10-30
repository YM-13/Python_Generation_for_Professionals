"""
Вам доступен файл student_counts.csv, который содержит данные о количестве учеников в некотором учебном заведении за период
2000
2000 —
2021
2021 г. В первом столбце записан год, в последующих столбцах записан класс и количество учеников в данном классе в этом году:

year,5-Б,3-Б,8-А,2-Г,7-Б,1-Б,3-Г,3-А,2-В,6-Б,6-А,8-Б,8-Г,11-А,2-А,7-А,5-А,2-Б,10-А,11-Б,8-В,4-А,7-В,3-В,1-А,9-А,11-В
2000,19,15,18,29,19,17,26,29,28,30,26,27,27,22,29,19,27,20,16,18,15,27,19,29,22,20,23
2001,21,30,22,19,26,20,24,27,20,30,24,30,29,21,20,19,29,27,23,25,30,30,23,22,22,18,22
...
Напишите программу, которая записывает данную таблицу в файл sorted_student_counts.csv, располагая все столбцы в порядке возрастания классов, при совпадении классов — в порядке возрастания букв.

Примечание 1. Каждый класс содержит номер и букву и записывается в следующем формате:

<номер класса>-<буква класса>
Примечание 2. Разделителем в файле student_counts.csv является запятая, при этом кавычки не используются.
"""

import csv

with open('student_counts.csv', 'r', encoding='UTF-8') as students_in, open('sorted_student_counts.csv', 'w', encoding='UTF-8', newline='') as students_out:
	reader = csv.DictReader(students_in, delimiter=',')
	columns = list(reader.fieldnames)
	c_1 = columns.pop(0)
	columns = [j.split('-') for j in columns]
	columns.sort(key=lambda x: (int(x[0]), x[1]))
	columns = [c_1] + list(map(lambda x: "-".join(x), columns))

	writer = csv.DictWriter(students_out, fieldnames=columns, delimiter=',')
	writer.writeheader()
	[writer.writerow(row) for row in reader]






#********************************************************************#
#********************************************************************#

# import csv
#
# def key_func(grade):
# 	number, letter = grade.split('-')
# 	return int(number), letter
#
# with open('student_counts.csv', encoding='utf-8') as file:
# 	reader = csv.DictReader(file)
# 	columns = ['year'] + sorted(reader.fieldnames[1:], key=key_func)
# 	rows = list(reader)
#
# with open('sorted_student_counts.csv', 'w', encoding='utf-8') as file:
# 	writer = csv.DictWriter(file, fieldnames=columns)
# 	writer.writeheader()
# 	writer.writerows(rows)