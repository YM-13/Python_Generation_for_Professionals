# from functools import reduce
# from operator import itemgetter, ...
# ''.splitlines()


# ********************************************************************#
# from datetime import datetime, date
#
# def fined_index(dates: list[date]):
# 	for i in range(len(dates)):
# 		if (dates[i].month + dates[i].day) % 2 != 0:
# 			return i
# 	return None
#
# d1 = datetime.strptime(input(), '%d.%m.%Y')
# d2 = datetime.strptime(input(), '%d.%m.%Y')
#
# a = d1.toordinal()
# b = d2.toordinal()
# l_dates = [date.fromordinal(k) for k in [*range(a, b + 1)]]
# I = fined_index(l_dates)
# if I != None:
# 	for j in range(I, len(l_dates), 3):
# 		d = l_dates[j]
# 		if d.weekday() not in (0,3):
# 			print(d.strftime('%d.%m.%Y'))
#
#
#
#
#
# from datetime import datetime, timedelta
#
# pattern = '%d.%m.%Y'
# start = datetime.strptime(input(), pattern)
# end = datetime.strptime(input(), pattern)
#
# while not (start.month + start.day) % 2:
#     start += timedelta(days=1)
#
# while start <= end:
#     week = start.isoweekday()
#     if week in (2,3,5,6,7):
#         print(start.strftime(pattern))
#     start += timedelta(days=3)
# ********************************************************************#
# ********************************************************************#


# from functools import reduce
# from operator import itemgetter
# from datetime import datetime, timedelta, date
# from time import perf_counter, monotonic, sleep
# import time

# result = time.gmtime()
# print(result)
# print(result.tm_year)
# print(result[0])

# time_tuple = (2021, 8, 31, 5, 31, 58, 1, 243, 0)
# time_obj = time.struct_time(time_tuple)
# print(time_obj)


# ********************************************************************#
# ********************************************************************#


# import calendar
# from calendar import monthrange, month_name
# from datetime import date

# months = [*month_name]
# Y, MONTH = input().split()
#
# print(monthrange(int(Y), months.index(MONTH))[1])
#
# def get_days_in_month(year: int, month: str) -> list[date]:
# 	M = [*month_name].index(month)
# 	Ds = monthrange(year, M)[1]
# 	res = [date(year, M, d) for d in range(1, Ds + 1)]
# 	return res


# ********************************************************************#
# ********************************************************************#


# from calendar import monthrange, isleap
# from datetime import date
#
# def finde_first_thursday(Y, M):
# 	first_day = monthrange(Y, M)[0]
# 	if first_day > 3:
# 		return 25 - first_day
# 	elif first_day < 3:
# 		return 18 - first_day
# 	else:
# 		return 15
#
# def get_3_thusday(year: int):
# 	for m in range(1, 13):
# 		d = finde_first_thursday(year, m)
# 		res = date(year, m, d)
# 		print(res.strftime('%d.%m.%Y'))
#
#
# get_3_thusday(int(input()))


# ********************************************************************#
# ********************************************************************#

# import sys
#
# print('Python')
#
# sys.stdout = open('file.txt', 'w')
#
# print('is')
# print('Power')

# ********************************************************************#
# ********************************************************************#

#
# import sys
#
# l = list(map(str.strip, sys.stdin)) #sys.stdin.read().rstrip('\n').split('\n')
# if len(l) == 0:
# 	print('нет учеников')
# else:
# 	nums = list(map(int, l))
# 	print(f'Рост самого низкого ученика: {min(nums)}')
# 	print(f'Рост самого высокого ученика: {max(nums)}')
# 	print(f'Средний рост: {sum(nums) / len(nums)}')


# ********************************************************************#
# ********************************************************************#


# import sys
#
# count = 0
# for line in sys.stdin:
# 	if line.startswith('#'):
# 		count += 1
#
# print(count)\

# ********************************************************************#
# ********************************************************************#


# import sys
# from datetime import datetime
#
# l = list(map(lambda s: datetime.strptime(s.strip(), '%d.%m.%Y'), sys.stdin))
# l_up = sorted(l)
# print(l_up)
# l_down = sorted(l, reverse=True)
# if len(set(l)) < len(l):
# 	print('MIX')
# elif l == l_up:
# 	print('ASC')
# elif l == l_down:
# 	print('DESC')
# else:
# 	print('MIX')


# ********************************************************************#
# ********************************************************************#


# import sys
#
# nums = list(map(int,  map(str.strip, sys.stdin)))
#
#
# a = nums[0]
# b = nums[-1]
#
# s = nums[1] - nums[0]
# ar = [*range(a, b + 1, s)]
#
# d = nums[1] / nums[0]
# f_n = nums[0]
# mult = []
# for _ in range(len(nums)):
# 	mult.append(f_n)
# 	f_n *= d
#
# if nums == ar:
# 	print('Арифметическая прогрессия')
# elif nums == mult:
# 	print('Геометрическая прогрессия')
# else:
# 	print('Не прогрессия')


# ********************************************************************#
# ********************************************************************#

# import csv
#
# def csv_columns(filename):
# 	with open(filename, 'r',  encoding='UTF-8') as file:
# 		data = list(csv.reader(file, delimiter=','))
#
# 	return {key: value for key, *value in zip(*data)} # певое значение присв ключу, а все оставшиеся упаковіваются в звезду
#
#
# print(csv_columns('deniro.csv'))


# ********************************************************************#
# ********************************************************************#


# import csv
#
# with open("data.csv", 'r',  encoding='UTF-8') as data_B, open("domain_usage.csv", 'w',  encoding='UTF-8', newline='') as d_u:
#
# 	data = [j[2] for j in csv.reader(data_B, delimiter=',')]
# 	d = {}
# 	for email in data[1:]:
# 		key = email.split('@')[1]
# 		d[key] = d.get(key, 0) + 1
# 	print(d.items())
# 	sorted_list = sorted(d.items(), key=lambda x: x[1])
# 	d2 = {}
# 	for v, k in sorted_list:
# 		if k not in d2:
# 			d2.setdefault(k, [])
# 		d2[k].append(v)
#
# 	for key in d2:
# 		sorted_l: list = sorted(d2[key])
# 		d2[key] = sorted_l
#
# 	writer = csv.writer(d_u, delimiter=',')
# 	columns = ['domain', 'count']
# 	writer.writerow(columns)
# 	[writer.writerow([j, key]) for key, l in d2.items() for j in l]


# ********************************************************************#
# ********************************************************************#

# import csv
#
# with open("wifi.csv", 'r',  encoding='UTF-8') as wifi_b:
# 	reder = tuple(csv.reader(wifi_b, delimiter=';'))
# 	d = {}
# 	for row in reder[1:]:
# 		_, R, _, Q = row
# 		d[R] = d.get(R, 0) + int(Q)
#
# 	[print(f'{j[0]}: {j[1]}') for j in sorted(d.items(), key=lambda x: (-x[1], x[0]))]

# ********************************************************************#
# ********************************************************************#

# import csv
#
# with open('titanic.csv', 'r', encoding='UTF-8') as data:
# 	reader = [[float(k) if set(k).issubset(set('1234567890.')) else k for k in l] for l in csv.reader(data, delimiter=';')]
# 	female_p = []
# 	for row in reader[1:]:
# 		survived, name, sex, age = row
# 		if survived == 1 and age < 18:
# 			print(name) if sex == 'male' else female_p.append(name)
# 	print(*female_p, sep='\n')


# ********************************************************************#
# ********************************************************************#
# 4.2  name, email, "datetime"
# ВАЖНО

# import csv
# from datetime import datetime
#
# with open('name_log.csv', 'r', encoding='UTF-8') as log_in, open('new_name_log.csv', 'w', encoding='UTF=8', newline='') as new_l_g:
# 	pattern = '%d/%m/%Y %H:%M'
# 	d = {}
# 	reader = csv.reader(log_in, delimiter=',')
# 	for row in reader:
# 		columns = row
# 		l = sorted(map(lambda x: [x[0], x[1], datetime.strptime(x[2], pattern)], reader), key=lambda x: x[1])
#
# 	for row in l:
# 		name, email, date = row
# 		if email not in d:
# 			d.setdefault(email, [])
# 		d[email].append((name, date))
#
# 	writer = csv.writer(new_l_g, delimiter=',')
# 	writer.writerow(columns)
# 	for email in d:
# 		name, date = max(d[email],  key=lambda x: x[1])
# 		writer.writerow([name, email, date.strftime(pattern)])
#
#
#
#
#
# import csv
# from datetime import datetime
#
# with open('name_log.csv', encoding='UTF-8') as f:
# 	header, *rows = csv.reader(f)
#
# d = {i[1]:i for i in sorted(rows, key=lambda x: datetime.strptime(x[2], '%d/%m/%Y %H:%M'))}
#
# with open('new_name_log.csv', 'w', encoding='UTF-8', newline='') as f:
# 	w = csv.writer(f)
# 	w.writerow(header)
# 	w.writerows(sorted(d.values(), key=lambda x: x[1]))


# ********************************************************************#
# ********************************************************************#
#
# import csv
# def condense_csv(filename:csv, id_name:str):
# 	d = {}
# 	with open(filename, 'r', encoding='UTF-8') as file_in, open('condensed.csv', 'w', encoding='UTF-8', newline='') as file_out:
# 		reader = csv.reader(file_in, delimiter=',')
# 		for row in reader:
# 			a, b, c = row
# 			if a not in d:
# 				d.setdefault(a, [(id_name, a), (b, c)])
# 			else:
# 				d[a].append((b, c))
# 		data = [dict(d[key]) for key in d]
# 		columns = list(data[0].keys())
#
# 		writer = csv.DictWriter(file_out, fieldnames=columns)
# 		writer.writeheader()
# 		for row in data:
# 			writer.writerow(row)
#
#
# text = '''01,Title,Ran So Hard the Sun Went Down
# 02,Title,Honky Tonk Heroes (Like Me)'''
#
# with open('data_1.csv', 'w', encoding='utf-8') as file:
# 	file.write(text)
#
# condense_csv('data_1.csv', id_name='ID')
#
# with open('condensed.csv', encoding='utf-8') as file:
# 	print(file.read().strip())
#
#
# text = '''01,Artist,Otis Taylor
# 01,Title,Ran So Hard the Sun Went Down
# 01,Time,3:52
# 02,Artist,Waylon Jennings
# 02,Title,Honky Tonk Heroes (Like Me)
# 02,Time,3:29'''
#
# with open('data_1.csv', 'w', encoding='utf-8') as file:
# 	file.write(text)
#
# condense_csv('data_1.csv', id_name='ID')
#
# with open('condensed.csv', encoding='utf-8') as file:
# 	print(file.read().strip())


import sys
import json

update_operations = {
    str: lambda x: f'{x}!',
    int: lambda x: x + 1,
    float: lambda x: x + 1,
    bool: lambda x: not x,
    list: lambda x: x * 2,
    dict: lambda x: x | {'newkey': None}
}

with open('data.json') as file, open('updated_data.json', 'w', encoding='UTF-8') as new_file:
	data = json.load(file)
	l = []

	for j in data:
		if j != None:
			f = update_operations[type(j)]
			l.append(f(j))

	json.dump(l, new_file, indent=3)
