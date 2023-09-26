"""В онлайн-школе "BEEGEEK" сотрудникам положена корпоративная почта, которая формируется
как <имя-фамилия>@beegeek.bzz, например, timyr-guev@beegeek.bzz. При таком подходе существует проблема тёзок.
Для решения такой проблемы было решено приписывать справа номер.

Тогда первый Тимур Гуев получает ящик timyr-guev@beegeek.bzz (без номера), второй — timyr-guev1@beegeek.bzz,
третий — timyr-guev2@beegeek.bzz, и так далее.

Вам дан список уже занятых ящиков в порядке их выдачи и имена-фамилии новых сотрудников в заранее подготовленном виде
(латиницей с символом - между ними). Напишите программу, которая раздает корпоративные ящики новым сотрудникам школы.

Формат входных данных:
На вход программе в первой строке подается целое неотрицательное число n — количество выданных ящиков.
В следующих n строках перечислены сами ящики в порядке выдачи, по одному на строке. На следующей строке задано целое
неотрицательное число m — количество новых сотрудников, которым нужно раздать корпоративные ящики.
Каждая из последующих m строк представляет собой имя и фамилию сотрудника в подготовленном к использованию формате.

Формат выходных данных:
Программа должна вывести почтовые ящики (m строк) для новых сотрудников в том порядке, в котором они раздавались."""

d = {}
mail_end = '@beegeek.bzz'
def highlight_the_email_and_its_number(mail: str) -> tuple[str, int]:
	key = mail.rstrip(mail_end)
	em_num = []
	for j in key: # [::-1]
		if j.isdigit():
			em_num.append(j)
		#break
	# em_num.reverse()
	key = key[:len(key) - len(em_num)]
	return (key, 0) if not em_num else (key, int(''.join(em_num)))


def regestration_existing_mail(N: int):
	for _ in range(N):
		key, num = highlight_the_email_and_its_number(input())
		if key not in d:
			d.setdefault(key, [])
		d[key].append(num)


def available_num(name: str) -> str:
	if name not in d:
		d[name] = [0]
		print(f'Не было ключа! {name}: {d[name]}')
		return ''


	d[name].sort()
	print(f'SORTED: {d[name]}')
	used_nums = d[name]
	check_nums = [*range(max(used_nums) + 1)]
	print(check_nums)

	if used_nums == check_nums:
		num = max(used_nums) + 1
		d[name].append(num)
		return str(num)

	for i in check_nums:
		if i not in used_nums:
			d[name].append(i)
			if i == 0:
				return ''
			return str(i)


def email_generator(M: int):
	for _ in range(M):
		name = input()
		num = available_num(name)
		print(name + num + mail_end)


n = int(input())
regestration_existing_mail(n)

m = int(input())
email_generator(m)
