# 6.	Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

index = int(input('Введите номер буквы: '))

alf = 'abcdefghijklmnopqrstuvwxyz'

print(alf[index-1])