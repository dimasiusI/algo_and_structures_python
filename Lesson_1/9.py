# 9.Вводятся три разных числа. Найти, какое из них
# является средним (больше одного, но меньше другого).

a = int(input('First number: '))
b = int(input('Second number: '))
c = int(input('Third number: '))


if a > b and a > c:
    if b < c:
        print(f'Среднее число {c}')
    else:
        print(f'Среднее число {b}')
elif b > a and b > c:
    if c < a:
        print(f'Среднее число {a}')
    else:
        print(f'Среднее число {c}')
else:
    print(f'Среднее число {b}')

