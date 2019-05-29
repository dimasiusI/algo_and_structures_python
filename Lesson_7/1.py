"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""

import random

def bubble (arr):
    count = 1
    globalcount = 0 #Сколько раз пройдет цикл, чтобы достичь результата

    while count != 0:
        if count > 0:
            count = 0
        for i in range(len(arr)-1):
            if arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                count += 1

        globalcount += 1

    return arr, globalcount


n = random.sample(range(-100, 100), 25)

print(n)

print(bubble(n))
