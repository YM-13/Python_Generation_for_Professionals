"""
Команда BEEGEEK планирует выпустить свой новый курс 08.11.2022 ровно в 12:00. Напишите программу, которая принимает на
вход текущие дату и время и определяет, сколько времени осталось до выхода курса.

Формат входных данных
На вход программе подаются текущие дата и время в формате DD.MM.YYYY HH:MM.

Формат выходных данных
Программа должна вывести текст с указанием количества дней и часов, оставшихся до выхода курса, в следующем формате:

До выхода курса осталось: <кол-во дней> дней и <кол-во часов> часов
Если в данном случае количество часов равно нулю, то вывести нужно только дни.

Если количество дней равно нулю, то вывести нужно только часы и минуты в следующем формате:

До выхода курса осталось: <кол-во часов> часов и <кол-во минут> минут
Если в данном случае количество минут равно нулю, то вывести нужно только часы. Аналогично, если количество часов равно нулю, то вывести нужно только минуты.

Если введенные дата и время больше либо равны 08.11.2022 12:00, программа должна вывести текст:

Курс уже вышел!
"""


from datetime import datetime, timedelta

def choose_plural(amount, declensions):
	key = amount
	if amount > 99:
		key %= 100

	if key in (11, 12, 13, 14):
		return f'{amount} {declensions[2]}'

	last_d = key % 10

	if last_d in (0, 5, 6, 7, 8, 9):
		return f'{amount} {declensions[2]}'

	if last_d in (2, 3, 4):
		return f'{amount} {declensions[1]}'

	if last_d == 1:
		return f'{amount} {declensions[0]}'


release = datetime(2022, 11, 8, 12, 00)
current_date = datetime.strptime(input(), '%d.%m.%Y %H:%M')
difference = release - current_date
D = ('день', 'дня', 'дней')
H = ('час', 'часа', 'часов')
M = ('минута', 'минуты', 'минут')

days = difference.days
hours = (difference - timedelta(days=days)).seconds // 3600
minutes = (difference - timedelta(days=days) - timedelta(hours=hours)).seconds // 60


if difference <= timedelta(seconds=0):
	print('Курс уже вышел!')
elif days and hours:
	print(f'До выхода курса осталось: {choose_plural(days, D)} и {choose_plural(hours, H)}')
elif days and not hours:
	print(f'До выхода курса осталось: {choose_plural(days, D)}')
elif hours and not days and not minutes:
	print(f'До выхода курса осталось: {choose_plural(hours, H)}')
elif hours and minutes and not days:
	print(f'До выхода курса осталось: {choose_plural(hours, H)} и {choose_plural(minutes, M)}')
elif minutes and not days and not hours:
	print(f'До выхода курса осталось: {choose_plural(minutes, M)}')
