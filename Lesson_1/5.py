#5.	Пользователь вводит две буквы. Определить, на каких местах
# алфавита они стоят, и сколько между ними находится букв.

begin = input('Введите начальную букву ENG : ')
end = input('Введите конечную букву ENG: ')

alf = 'abcdefghijklmnopqrstuvwxyz'

ib = alf.index(begin) + 1
ie = alf.index(end) + 1

k = abs(ie - (ib + 1))

print('Буква {} стоит на {} месте в алфавите'.format(begin, ib))
print('Буква {} стоит на {} месте в алфавите'.format(end, ie))
print('Между ними {} букв'.format(k))