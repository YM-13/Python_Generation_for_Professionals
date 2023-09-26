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




from datetime import date
import locale


first_date = date(1992, 10, 6)
# birthday.isoformat()
# print('Название месяца:', birthday.strftime('%B'))
# print('Название дня недели:', birthday.strftime('%A'))
# print('Год:', birthday.strftime('%Y'))
# print('Месяц:', birthday.strftime('%m'))
# print('День:', birthday.strftime('%d'))

iso = 'Дата первого урагана в ISO формате: ' + first_date.isoformat()
ru = 'Дата первого урагана в RU формате: ' + first_date.strftime('%d.%m.%Y')
us = 'Дата первого урагана в US формате: ' + first_date.strftime('%m/%d/Y')

print(iso)
print(ru)
print(us)