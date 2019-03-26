# 1.	В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

lst = [x for x in range(2, 100)]

lst2 = {x:0 for x in range(2, 10)}

print(lst2)

for i in lst2.keys():
    for j in lst:
        if j % i == 0:
            lst2[i] += 1

for i in lst2.keys():
    print(f'Числу {i} в диапазоне от 2 до 99 кратно {lst2[i]} чисел')
