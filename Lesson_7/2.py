"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
"""
import random

def merge(arr):
    if len(arr)>1:
        mid = len(arr)//2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        merge(lefthalf)
        merge(righthalf)

        i = 0
        j = 0
        k = 0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                    arr[k]=lefthalf[i]
                    i=i+1
            else:
                arr[k]=righthalf[j]
                j=j+1
            k=k+1

            while i<len(lefthalf):
                arr[k]=lefthalf[i]
                i=i+1
                k=k+1

            while j<len(righthalf):
                arr[k]=righthalf[j]
                j=j+1
                k=k+1

    return arr


n = random.sample(range(0, 50), 25)

print(n)

merge(n)

print(n)
