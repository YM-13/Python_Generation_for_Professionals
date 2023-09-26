"""Вам доступен текстовый файл files.txt, содержащий информацию о файлах. Каждая строка файла содержит три значения,
разделенные символом пробела — имя файла, его размер (целое число) и единицы измерения:

cant-help-myself.mp3 7 MB
keep-yourself-alive.mp3 6 MB
bones.mp3 5 MB
...
Напишите программу, которая группирует данные файлы по расширению, определяя общий объем файлов каждой группы, и выводит
полученные группы файлов, указывая для каждой ее общий объем. Группы должны быть расположены в лексикографическом
порядке названий расширений, файлы в группах — в лексикографическом порядке их имен.

Примечание 1. Например, если бы файл files.txt имел вид:

input.txt 3000 B
scratch.zip 300 MB
output.txt 1 KB
temp.txt 4 KB
boy.bmp 2000 KB
mario.bmp 1 MB
data.zip 900 MB
то программа должна была бы вывести:

boy.bmp
mario.bmp
----------
Summary: 3 MB

input.txt
output.txt
temp.txt
----------
Summary: 8 KB

data.zip
scratch.zip
----------
Summary: 1 GB
где Summary — общий объем файлов группы.

Примечание 2. Гарантируется, что все имена файлов содержат расширение.

Примечание 3. Общий объем файлов группы записывается в самых крупных (максимально возможных) единицах измерения с
округлением до целых. Другими словами, сначала следует определить суммарный объем всех файлов группы, скажем, в байтах,
а затем перевести полученное значение в самые крупные (максимально возможные) единицы измерения. Примеры перевода:

1023 B -> 1023 B
1300 B -> 1 KB
1900 B -> 2 KB
Примечание 4. Значения единиц измерения такие же, какие приняты в информатике:

1 KB = 1024 B
1 MB = 1024 KB
1 GB = 1024 MB

Примечание 5. При открытии файла используйте явное указание кодировки UTF-8."""
def summarise_file_sizes(d, key):
	l = list(map(lambda x: x[1], d[key]))
	size = 0
	for j in l:
		if j[1] == 'KB':
			size += j[0] * 1024
		elif j[1] == 'MB':
			size += j[0] * 1024 ** 2
		elif j[1] == 'GB':
			size += j[0] * 1024 ** 3
		else:
			size += j[0]

	if 1024 <= size < 1024 ** 2:
		return int(round(size / 1024)), 'KB'
	elif 1024 ** 2 <= size <= 1024 ** 3:
		return int(round(size / 1024 ** 2)), 'MB'
	elif size >= 1024 ** 3:
		return int(round(size / 1024 ** 3)), 'GB'
	else:
		return size, 'B'


with open('files.txt', 'rt', encoding='UTF-8') as sorce:
	d = {}
	rows = list(map(lambda x: [x[0], (int(x[1]), x[2])], [l.rstrip('\n').split() for l in sorce.readlines()]))
	for k in rows:
		key = k[0][k[0].index('.') + 1:]
		if key not in d:
			d.setdefault(key, [])
		d[key].append(k)
	d = dict(sorted(d.items()))

	for key in d:
		d[key].sort()
		size, u_of_m = summarise_file_sizes(d, key)
		print(*map(lambda x: x[0], d[key]), sep='\n')
		print('-' * 10)
		print(f"Summary: {size} {u_of_m}")
		print()
