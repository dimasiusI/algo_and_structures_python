# 3.	По введенным пользователем координатам двух точек вывести
# уравнение прямой вида y = kx + b, проходящей через эти точки.

x1 = int(input('Vvedite Ax: '))
y1 = int(input('Vvedite Ay: '))


x2 = int(input('Vvedite Bx: '))
y2 = int(input('Vvedite By: '))


k = (y2 - y1) / (x2 - x1)

b = y2 - k*x1

print('Уравнение прямой: y = {}x + {}'.format(k, b))
