"""
Вам доступен текстовый файл diary.txt, в который космонавт записывал небольшие отчёты за день. Каждый новый отчёт он мог
записать либо в начало файла, либо в середину, либо в конец. Все отчеты разделены между собой пустой строкой. Каждый
новый отчёт начинается со строки с датой и временем в формате DD.MM.YYYY; HH:MM, после которой следуют события,
произошедшие за указанный день:

29.04.2006; 06:55
It wasn’t until several hours after launch that we were able to take the time to get out of our seats and enter
the “habitation module.”
Then, after another orbital maneuver, we finally were able to take a several hour break and get a little sleep.

03.05.2006; 20:24
Everybody had a sleeping bag although I only used mine on a couple of brief occasions, and then only when getting
a little chilly.

...
Напишите программу, которая расставляет все записи космонавта в хронологическом порядке и выводит полученный результат.

Примечание 1. Например, если бы файл diary.txt имел вид:

13.02.1994; 18:49
Уже несколько дней наблюдаем на теневой части орбиты в районе Канады мощнейшее полярное сияние.
Прежде всего, поражают масштабы происходящего. Под нами огромная зелено-розовая «змея».

03.02.1994; 20:18
Сегодня наблюдали и сняли на видео след Шаттла после выведения, дымит он прилично.
Готовимся к радиолюбительской связи с экипажем Шаттла и, конечно, с Сергеем.
При подготовке к сеансу связи с Шаттлом познакомился с Ритой, радиолюбителем из Австралии.
Она немного говорит по-русски и очень приятно слышать родную речь.

12.02.1994; 17:17
Сегодня возникли проблемы со сбросом через спутник ретранслятор видеоинформации по снятому нами следу Шаттла.
Как сообщил нам ЦУП, в Щелкове холодно, все замерзло, антенна не работает...
Все это наводит на грустные размышления о нашей безолаберности и разрухе.
то программа должна была бы вывести:

03.02.1994; 20:18
Сегодня наблюдали и сняли на видео след Шаттла после выведения, дымит он прилично.
Готовимся к радиолюбительской связи с экипажем Шаттла и, конечно, с Сергеем.
При подготовке к сеансу связи с Шаттлом познакомился с Ритой, радиолюбителем из Австралии.
Она немного говорит по-русски и очень приятно слышать родную речь.

12.02.1994; 17:17
Сегодня возникли проблемы со сбросом через спутник ретранслятор видеоинформации по снятому нами следу Шаттла.
Как сообщил нам ЦУП, в Щелкове холодно, все замерзло, антенна не работает...
Все это наводит на грустные размышления о нашей безолаберности и разрухе.

13.02.1994; 18:49
Уже несколько дней наблюдаем на теневой части орбиты в районе Канады мощнейшее полярное сияние.
Прежде всего, поражают масштабы происходящего. Под нами огромная зелено-розовая «змея».
"""

from  datetime import datetime
d = {}
with open('diary.txt', 'rt', encoding='UTF-8') as DF:

	l = DF.read().split('\n\n')
	dd = {datetime.strptime(k[:k.index('\n')], '%d.%m.%Y; %H:%M'): k for k in l}

	dd = dict(sorted(dd.items()))
	for j in dd:
		print(dd[j])
		print()

