"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""


a = input('Введите число: ')
b = input('Введите число: ')
c = input('Введите число: ')

def summ(num):
    num = str(num)

    res = 0

    for i in num:
        res += int(i)

    return res

if summ(a) > summ(b) and summ(a) > summ(c):
    print(f'Сумма цифер числа {a} наибольшая и равна {summ(a)}')
elif summ(b) > summ(c) and summ(b) > summ(a):
    print(f'Сумма цифер числа {b} наибольшая и равна {summ(b)}')
else:
    print(f'Сумма цифер числа {c} наибольшая и равна {summ(c)}')