"""
Разные типы
Вам доступен файл data.json, содержащий список различных объектов:

[
   "nwkWXma",
   null,
   {
      "ISgHT": "dIUbf"
   },
   "Pzt",
   "BXcbGVTE",
   ...
]
Напишите программу, которая создает список, элементами которого являются объекты из списка, содержащегося в файле
data.json, измененные по следующим правилам:

если объект является строкой, в его конец добавляется восклицательный знак
если объект является числом, он увеличивается на единицу
если объект является логическим значением, он инвертируется
если объект является списком, он удваивается
если объект является JSON-объектом (словарем), в него добавляется новая пара "newkey": null
если объект является пустым значением (null), он не добавляется
Полученный список программа должна записать в файл updated_data.json.

Примечание 1. Например, если бы файл data.json имел вид:

["Hello", 179, true, null, [1, 2, 3], {"key": "value"}]
то программа должна была бы создать файл updated_data.json со следующим содержанием:

["Hello!", 180, false, [1, 2, 3, 1, 2, 3], {"key": "value", "newkey": null}]
"""

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
