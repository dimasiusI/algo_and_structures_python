"""
4.	Написать программу, которая генерирует в указанных пользователем границах
●	случайное целое число,
●	случайное вещественное число,
●	случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f',
то вводятся эти символы. Программа должна вывести на экран любой
символ алфавита от 'a' до 'f' включительно.
"""

import random

print('Что вы хотите сгенерировать? \n 1. Случайное целое число \n 2. Случайное вешественное число \n 3. Случайный символ')

key = int(input('Key: '))

if key == 1:
    begin = int(input('Введите предел от: '))
    end = int(input('Введите предел до: '))

    print(random.randint(begin, end))

elif key == 2:
    begin = float(input('Введите предел от: '))
    end = float(input('Введите предел до: '))

    print(random.uniform(begin, end))

elif key == 3:
    alf = "abcdefghijklmnopqrstuvwxyz"
    begin = (input('Введите предел от: '))
    end = (input('Введите предел до: '))

    ib = alf.index(begin)
    ie = alf.index(end)

    print(alf[random.randint(ib, ie)])

else:
    print('Неверный ключ')