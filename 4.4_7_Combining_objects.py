"""
Объединение объектов
Вам доступны два файла data1.json и data2.json, каждый из которых содержит по единственному JSON-объекту:

{
   "Holly-Anne": [
      33,
      "failed"
   ],
   "Caty": [
      36,
      "failed"
   ],
   ...
}
Напишите программу, которая объединяет два данных JSON-объекта в один JSON-объект, причем если пары из первого и второго объектов имеют совпадающие ключи, то значение следует взять из второго объекта. Полученный JSON-объект программа должна записать в файл data_merge.json.

Примечание 1. Например, если бы файлы data1.json и data2.json имели вид:

{
   "Timur": 99,
   "Anri": 97
}
{
   "Dima": 99,
   "Anri": 100
}
то программа должна была бы создать файл data_merge.json со следующим содержанием:

{
   "Anri": 100,
   "Dima": 99,
   "Timur": 99
}
Примечание 2. Элементы в результирующем JSON-объекте могут располагаться в произвольном порядке.
"""

import json

with open('data_CO_1.json', 'rt', encoding='UTF-8') as f1, open('data_CO_2.json', 'rt', encoding='UTF-8') as f2:
	data = json.load(f1)
	# data2 = json.load(f2)
	data |= json.load(f2) # data2
with open('data_merge.json', 'w', encoding='utf-8') as res_f:
	json.dump(data, res_f, indent=3)

