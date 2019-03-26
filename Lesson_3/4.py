# 4.	Определить, какое число в массиве встречается чаще всего.

import random

lst1 = [random.randint(0, 10) for x in range(0, 155)]
lst2 = {x:0 for x in range(0, 10)}

for i in lst2.keys():
    for j in lst1:
        if i == j:
            lst2[i] += 1

key_max = 0
val_max = 0
print(lst2)

for i in lst2.keys():
    if lst2[i] > val_max:
        val_max = lst2[i]
        key_max = i

print(f'В данном случайном массиве цифра {key_max} встречается чаще всего. {val_max} раз(-а).')
