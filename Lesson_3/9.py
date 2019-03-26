# 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

#создаем матрицу 5х5
a = [[random.randint(-9,9) for i in range(5)] for j in range(5)]

def searchMinInCol(arr, col):
    min_num = 10
    i = 0
    while i < len(arr):
        if min_num > arr[i][col]:
            min_num = arr[i][col]
        i += 1
    return min_num

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()

min_ = []

#для матрицы 5х5
j = 0
while j < 5:
    min_.append(searchMinInCol(a, j))
    j += 1

max_in_min = max(min_)

print(min_)
print(max_in_min)