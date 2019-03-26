"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""

import random

def insertion_sort(arrayToSort):
    a = arrayToSort
    for i in range(len(a)):
        v = a[i]
        j = i;
        while (a[j-1] > v) and (j > 0):
            a[j] = a[j-1]
            j = j - 1
        a[j] = v
    return a

lst1 = random.sample(range(-100, 100), 10)

print(lst1)

lst1 = insertion_sort(lst1)

a = lst1[0]
b = lst1[1]

print(f'Два наименьших числа в данном массиве {a} и {b}')