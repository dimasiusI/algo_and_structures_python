"""
8.	Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""

import random

matrix = [ [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0] ]

def zapros():
    #return int(input('ВВедите число: '))
    return random.randint(0, 9)

i = 0
while i < 4:
    j = 0
    while j < 5:
        if j < 4:
            matrix[i][j] = zapros()
        else:
            res = 0
            for k in matrix[i]:
                res += k
            matrix[i][j] = res
        j += 1
    i += 1


for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=' ')
    print()
