"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""

n = int(input('Введите количество элементов: '))

m = 1
count = 1
nums = []

i = 0
while n > i:
    if n == i:
        break

    if count % 2 == 0:
        nums.append(-m)
    else:
        nums.append(m)

    m = m/2
    n -= 1
    count += 1

res = 0

for i in nums:
    res += i

print(nums)
print(res)

