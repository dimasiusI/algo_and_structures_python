# 8.	Определить, является ли год, который ввел пользователем,
# високосным или не високосным.
#Год является високосным в двух случаях: либо он кратен 4,
# но при этом не кратен 100, либо кратен 400.

y = int(input('Введите год: '))

if y % 4 == 0 and y % 100 != 0 or y % 4 == 0 and y % 400 == 0:
    print('Год високосный!')
else:
    print('Год не високосный!')
