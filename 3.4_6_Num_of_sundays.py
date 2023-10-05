"""
Реализуйте функцию num_of_sundays(), которая принимает на вход один аргумент:

year — натуральное число, год
Функция должна возвращать количество воскресений в году year.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию num_of_sundays(), но не код, вызывающий ее.
"""

from datetime import timedelta, date
def num_of_sundays(year):
    counter, td = 0, timedelta(days=7)
    d = date(year, 1, 1)
    d += timedelta(days=6 - d.weekday())
    while d.year == year:
        d += td
        counter += 1
    return counter