"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""

import cProfile
import timeit
##import sys

n = 100

def summ(n):
    if n == 1:
        return 1
    return n + summ(n - 1)

def dok(n):
    return int(n*(n+1)/2)

if summ(n) == dok(n):
    print(f'{summ(n)} = {dok(n)}')

t = timeit.timeit('summ(n)', setup='from __main__ import summ, n') #приблизительно 21,5 сек
print(f'Без меморизации выполнение данной функции заняло {t} секунд')

def main():
    summ(100)
    dok(100)

if __name__ == '__main__':
    cProfile.run('main()')

def summ_1(n, memory=[0, 1]):
    if n > len(memory):
        return 1
    else:
        r =  n + summ(n - 1)
        memory.append(r)
        return r


t = timeit.timeit('summ_1(n)', setup='from __main__ import summ_1, n') #приблизительно 0,2 сек
print(f'С меморизацией выполнение данной функции заняло {t} секунд')