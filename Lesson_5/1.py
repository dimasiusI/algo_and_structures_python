"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""

from random import randint

count = 4 #int(input('Сколько предприятий будем сравнивать?'))
names= ['vbn', 'fgh', 'rtw', 'usb'] #чтобы не писать каждый раз в ручную

all_pred = {}

def add_pred():
    pred = {1:0, 2:0, 3:0, 4:0}
    for i in range(1,5):
        pred[i] = randint(10, 50) #int(input(f'Прибыль за {i+1}-й месяц: '))

    return pred


for i in range(count):
    name = names[i] #input('Name: ')
    all_pred[name] = add_pred()

print(all_pred)

obshak = 0

for i in all_pred.values():
    for j in i.values():
        obshak += j

print(f'Средняя прибыль равна {int(obshak/count)}')

new_all_pred = {}

for i in all_pred:
    srednyaya = 0
    for j in all_pred[i].values():
        srednyaya += j
    new_all_pred[i] = srednyaya

print(new_all_pred)

for i in new_all_pred:
    j = new_all_pred[i]
    if j > obshak/count:
        print(f'Предприятие {i} имеет доход выше среднего {j}')
    else:
        print(f'Предприятие {i} имеет доход ниже среднего {j}')

