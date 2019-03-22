"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""

a = input('Введите какое нибудь большое число: ')

chet = []
nechet =[]

count_chet = 0
count_nechet = 0

for i in a:
    if int(i) % 2 == 0:
        chet.append(i)
        count_chet += 1
    else:
        nechet.append(i)
        count_nechet += 1

print(f'В числе {a} {count_chet} четные цифры: {chet} и {count_nechet} нечетные цифры {nechet}')
