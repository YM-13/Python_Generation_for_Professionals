"""
Во время визита очередного гостя сотрудникам отеля приходится проверять, доступна ли та или иная дата для бронирования номера.

Реализуйте функцию is_available_date(), которая принимает два аргумента в следующем порядке:

booked_dates — список строковых дат, недоступных для бронирования. Элементом списка является либо одиночная дата, либо
период (две даты через дефис). Например:
['04.11.2021', '05.11.2021-09.11.2021']
date_for_booking — одиночная строковая дата или период (две даты через дефис), на которую гость желает забронировать
номер. Например:
'01.11.2021' или '01.11.2021-04.11.2021'
Функция is_available_date() должна возвращать True, если дата или период date_for_booking полностью доступна для
бронирования. В противном случае функция должна возвращать False.

Примечание 1. Гарантируется, что в периоде левая дата всегда меньше правой.

Примечание 2. В периоде (две даты через дефис) граничные даты включены.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию is_available_date(),
но не код, вызывающий ее.
"""


from datetime import datetime

def create_days(data):
	res = []
	for dt in data:
		if '-' in dt:
			from_data, to_data = [datetime.strptime(d, '%d.%m.%Y') for d in dt.split('-')]
			days = [*range(from_data.toordinal(), to_data.toordinal() + 1)]
			res.extend(days)
		else:
			res.append(datetime.strptime(dt, '%d.%m.%Y').toordinal())
	print(res)
	return res

def is_available_date(booked_dates: list[str], date_for_booking: str):
	booked_dates_all = create_days(booked_dates)
	booking_d = create_days([date_for_booking])
	b_d = set(booked_dates_all) & set(booking_d)
	return len(b_d) == 0


dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021'
print(is_available_date(dates, some_date))