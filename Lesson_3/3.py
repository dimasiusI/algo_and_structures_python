#3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.

import random

lst1 = random.sample(range(100), 10)

print(lst1)

max_num = 0
index_max = 0
min_num = 100
index_min = 0

for index, val in enumerate(lst1):
    if val > max_num:
        max_num = val
        index_max = index
    if val < min_num:
        min_num = val
        index_min = index


lst1[index_max] = min_num
lst1[index_min] = max_num

print(lst1)
