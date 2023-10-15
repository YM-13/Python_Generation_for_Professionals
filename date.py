
#********************************************************************#
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
#********************************************************************#
#********************************************************************#



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




#********************************************************************#
#********************************************************************#


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




#********************************************************************#
#********************************************************************#


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


#********************************************************************#
#********************************************************************#

# import sys
#
# print('Python')
#
# sys.stdout = open('file.txt', 'w')
#
# print('is')
# print('Power')

#********************************************************************#
#********************************************************************#

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


#********************************************************************#
#********************************************************************#


# import sys
#
# count = 0
# for line in sys.stdin:
# 	if line.startswith('#'):
# 		count += 1
#
# print(count)\

#********************************************************************#
#********************************************************************#


import sys

d = {}
for line in ['На рейсах Поражения второй пилот будет исполнять обязанности бортпроводника / Авиация / 0.3',
             'Огурец исключит из своих рядов членов, не проголосовавших за Единую Арстоцку на выборах / Политика / 0.8',
             'Орбистанские точки общепита будут закрыты для вакцинированных граждан / Общество / 0.7',
             'Джорджи Костава получил членский билет Независимого Кобрастана / Политика / 0.0',
             'В Колечии повысят призывной возраст до 40 лет / Политика / 1.0',
             'Всем гражданам Антегрии въезд в Арстоцку запрещен / Политика / 0.8', 'Политика']: # sys.stdin:
	l = line.strip().split(' / ') # На рейсах Поражения второй пилот будет исполнять обязанности бортпроводника / Авиация / 0.3
	if len(l) > 1:
		key = l[1] # Авиация
		key_r = float(l[2]) # 0.3
		if key not in d:
			d.setdefault(key, {})
		if key_r not in d[key]:
			d[key].setdefault(key_r, [])
		d[key][key_r].append(l[0])
	else:
		key = l[0]
		news = sorted(d[key].items())
		news = dict(news)
		print(news)
		for k in news:
			N = sorted(news[k])
			print(*N, sep='\n')