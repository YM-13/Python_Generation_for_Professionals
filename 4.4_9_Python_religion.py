"""
Я исповедую Python, а ты?
Вам доступен файл countries.json, содержащий список JSON-объектов c информацией о странах и исповедуемых в них религиях:

[
   {
      "country": "Afghanistan",
      "religion": "Islam"
   },
   {
      "country": "Albania",
      "religion": "Islam"
   },
   ...
]
Каждый объект из этого списка содержит два атрибута:

country — страна
religion — исповедуемая религия
Напишите программу, которая создает единственный JSON-объект, имеющий в качестве ключа название религии, а в качестве
значения — список стран, в которых исповедуется данная религия. Полученный JSON-объект программа должна записать в файл religion.json.

Примечание 1. Страны в списках должны располагаться в своем исходном порядке.

Примечание 2. Начальная часть файла religion.json выглядит так:

{
   "Islam":[
      "Afghanistan",
      "Albania",
      "Algeria",
      ...
   ],
   ...
}
"""

# import json
#
# with open('countries.json', 'r', encoding='UTF-8') as file, open('religion.json', 'w', encoding='UTF-8') as new_f:
# 	data = json.load(file)
# 	d = {}
# 	for j in data:
# 		v, k = j.values()
# 		if k not in d:
# 			d.setdefault(k, [])
# 		d[k].append(v)
#
# 	json.dump(d, new_f)



#*****************************************************************************
import json

with open("countries.json") as file_in, open("religion.json", "w") as file_out:

	d = {}
	datas = json.load(file_in)
	for data in datas:
		d[data['religion']] = d.setdefault(data['religion'], []) + [data['country']]

	json.dump(d, file_out, indent=3)