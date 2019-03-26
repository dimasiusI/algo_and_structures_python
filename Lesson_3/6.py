"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""


import random

lst1 = random.sample(range(-100, 100), 10)

print(lst1)

max_num = 0
index_max = 0
min_num = 100
index_min = 0
res = 0

for index, val in enumerate(lst1):
    if val > max_num:
        max_num = val
        index_max = index
    if val < min_num:
        min_num = val
        index_min = index

if index_max > index_min:
    i = index_min + 1
    while i < index_max:
        res += lst1[i]
        i += 1
elif index_min > index_max:
    i = index_max + 1
    while i < index_min:
        res += lst1[i]
        i += 1

print(f'Сумма элементов, находящихся между минимальным {min_num} и максимальным {max_num} элементами, равна {res}')