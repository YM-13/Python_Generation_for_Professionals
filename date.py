# from datetime import date
#
# def get_min_max(dates):
# 	if dates:
# 		return min(dates), max(dates)
# 	return tuple()
#
#
# dates = [date(2021, 10, 5), date(1992, 6, 10), date(2012, 2, 23), date(1995, 10, 12)]
#
# print(get_min_max(dates))
# print(get_min_max([]))



# from datetime import date
#
# def get_date_range(start: date, end: date):
# 	if start > end:
# 		return []
# 	return [date.fromordinal(d) for d in range(start.toordinal(), end.toordinal() + 1)]
#
#
# date1 = date(2021, 10, 1)
# date2 = date(2021, 10, 5)
#
# print(*get_date_range(date1, date2), sep='\n')


#
# from datetime import date
#
# def saturdays_between_two_dates(start: date, end: date):
# 	period = (start, end)
# 	count = 0
# 	for dat in range(min(period).toordinal(), max(period).toordinal() + 1):
# 		if date.fromordinal(dat).weekday() == 5:
# 			count += 1
# 	return count




# from datetime import date
#
# andrew = date(1992, 8, 24)
#
# print(andrew.strftime('%Y-%m'))   # выводим дату в формате YYYY-MM
# print(andrew.strftime('%B (%Y)'))   # выводим дату в формате month_name (YYYY)
# print(andrew.strftime('%Y-%j'))   # выводим дату в формате YYYY-day_number



# from datetime import date
#
# d1 = date.fromisoformat(input())
# d2 = date.fromisoformat(input())
#
# print(min(d1, d2).strftime('%d-%m (%Y)'))




# from datetime import date
#
# l: list[date] = [date.fromisoformat(input()) for _ in range(int(input()))]
# l.sort()
# [print(j.strftime('%d/%m/%Y')) for j in l]



# from datetime import date
#
# def print_good_dates(data: list[date]):
# 	l = [k for k in data if k.year == 1992 and k.day + k.month == 29]
# 	l.sort()
# 	[print(j.strftime('%B %d, %Y')) for j in l]




# from datetime import date
# def is_correct(day, month, year):
# 	try:
# 		date(year, month, day)
# 		return True
# 	except:
# 		return False
#
#
# print(is_correct(31, 13, 2021))




# from datetime import date
#
# def correct_data():
# 	count = 0
# 	while True:
# 		dt = input()
# 		if dt =='end':
# 			break
# 		try:
# 			l = [int(i) for i in dt.split('.')]
# 			l.reverse()
# 			date(*l)
# 			count += 1
# 			print('Корректная')
# 		except:
# 			print('Некорректная')
#
# 	print(count)
#
#
# correct_data()




# from datetime import datetime
#
# text = 'Уважаемый пациент, доктор готов принять Вас 15.07.2022 в 08:30'
#
# dt = datetime.strptime(text, 'Уважаемый пациент, доктор готов принять Вас %d.%m.%Y в %H:%M')
#
# print(dt)






# from datetime import datetime
#
# times_of_purchases = [datetime(2017, 10, 1, 12, 23, 25), datetime(2017, 10, 1, 15, 26, 26),
#                       datetime(2017, 10, 1, 15, 42, 57), datetime(2017, 10, 1, 17, 49, 59),
#                       datetime(2017, 10, 2, 6, 37, 10), datetime(2017, 10, 2, 6, 42, 53),
#                       datetime(2017, 10, 2, 8, 56, 45), datetime(2017, 10, 2, 9, 18, 3),
#                       datetime(2017, 10, 2, 12, 23, 48), datetime(2017, 10, 2, 12, 45, 5),
#                       datetime(2017, 10, 2, 12, 48, 8), datetime(2017, 10, 2, 12, 10, 54),
#                       datetime(2017, 10, 2, 19, 18, 10), datetime(2017, 10, 2, 12, 31, 45),
#                       datetime(2017, 10, 3, 20, 57, 10), datetime(2017, 10, 4, 7, 4, 57),
#                       datetime(2017, 10, 4, 7, 13, 31), datetime(2017, 10, 4, 7, 13, 42),
#                       datetime(2017, 10, 4, 7, 21, 54), datetime(2017, 10, 4, 14, 22, 12),
#                       datetime(2017, 10, 4, 14, 50), datetime(2017, 10, 4, 15, 7, 27),
#                       datetime(2017, 10, 4, 12, 44, 49), datetime(2017, 10, 4, 12, 46, 41),
#                       datetime(2017, 10, 4, 16, 32, 33), datetime(2017, 10, 4, 16, 34, 44),
#                       datetime(2017, 10, 4, 16, 46, 59), datetime(2017, 10, 4, 12, 26, 6)]
#
#
# l = [dt.strftime('%p') for dt in times_of_purchases]
# print(['После полудня', 'До полудня'][l.count('AM') > l.count('PM')])





# from datetime import date, time, datetime
#
# dates = [date(1793, 8, 23), date(1410, 3, 11), date(804, 11, 12), date(632, 6, 4),
#          date(295, 1, 23), date(327, 8, 24), date(167, 4, 16), date(229, 1, 24),
#          date(1239, 2, 5), date(1957, 7, 14), date(197, 8, 24), date(479, 9, 6)]
#
# times = [time(7, 33, 27), time(21, 2, 10), time(17, 20, 47), time(20, 8, 59),
#          time(12, 42, 56), time(15, 9, 57), time(17, 47, 9), time(9, 40, 2),
#          time(11, 47, 1), time(17, 27, 10), time(17, 55, 40), time(9, 14, 9)]
#
#
# l = [datetime.combine(d, t) for d,t in zip(dates, times)]
# l.sort(key=lambda x: x.second)
#
# [print(j) for j in l]





# from datetime import datetime
# 
# data = {'Дима': ('03.11.2021 09:31:18', '03.11.2021 11:41:28'),
#         'Геор': ('01.11.2021 09:03:04', '01.11.2021 12:40:35'),
#         'Анна': ('02.11.2021 04:41:54', '02.11.2021 05:39:40'),
#         'Илина': ('02.11.2021 01:36:40', '02.11.2021 04:48:27'),
#         'Герман': ('04.11.2021 07:51:19', '04.11.2021 09:53:53'),
#         'Руслан': ('01.11.2021 11:26:06', '01.11.2021 12:56:24'),
#         'Лера': ('03.11.2021 11:09:41', '03.11.2021 14:37:41'),
#         'Егор': ('03.11.2021 05:29:38', '03.11.2021 06:01:59'),
#         'Максим': ('05.11.2021 13:05:03', '05.11.2021 14:27:41'),
#         'Саша': ('03.11.2021 04:14:26', '03.11.2021 05:10:58'),
#         'Марина': ('05.11.2021 15:21:06', '05.11.2021 18:33:46')}
# 
# d = {}
# for key in data:
# 	t_f = datetime.strptime(data[key][1], '%d.%m.%Y %H:%M:%S')#.timestamp()
# 	t_s = datetime.strptime(data[key][0], '%d.%m.%Y %H:%M:%S')#.timestamp()
# 	print((t_f - t_s).seconds)
# 	d[t_f - t_s] = key
# 
# print(d[min(d)])





