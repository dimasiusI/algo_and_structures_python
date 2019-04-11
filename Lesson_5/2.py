"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

def summ (a,b):

    #по умолчанию b > a
    if len(a)>len(b):
        a, b = b, a

    while len(a) != len(b):
        a.insert(0, '0')

    a.reverse()
    b.reverse()

    sum_plus = 0
    res = []
    i = 0
    while i < len(a):
        sum_ = chisla[a[i]] + chisla[b[i]]
        if sum_plus == 1:
            sum_ += 1

        if sum_ == 16:
            sum_plus = 1
            res.append('0')

        if sum_ > 16:
            sum_plus = sum_% 16
            res.append(znachenie[sum_plus])
            sum_plus = 1
        elif sum_ < 16:
            res.append(znachenie[sum_])
            sum_plus = 0

        i += 1

    res.reverse()
    a.reverse()
    b.reverse()

    return res

def help_func_mult(a, b):
    sum_plus = 0
    res = []
    for j in a:
        mult_ = chisla[j] * chisla[b]

        if sum_plus >= 1:
            mult_ += sum_plus

        if mult_ == 16:
            sum_plus = 1
            res.append('0')

        if mult_ > 16:
            add_plus = mult_ % 16
            res.append(znachenie[add_plus])
            sum_plus = mult_ // 16
        elif mult_ < 16:
            res.append(znachenie[mult_])
            sum_plus = 0

        if sum_plus > 1 and len(res) == len(a):
            res.append(znachenie[sum_plus])
            return res
            break

    return res

def mult (a, b):
    a.reverse()
    b.reverse()

    #по умолчанию b > a
    if len(a)>len(b):
        a, b = b, a

    prom_res = []


    razryad = 0
    while razryad < len(b):
        res = help_func_mult(a, b[razryad])
        res.reverse()

        if razryad >= 1:
            i = 0
            while i < razryad:
                res.append('0')
                i += 1

        prom_res.append(res)

        razryad += 1

    #print(prom_res) #[‘7’, ‘C’, ‘9’, ‘F’, ‘E’]

    while 1 != len(prom_res):
        c = prom_res[0]
        d = prom_res[1]
        prom_res[0] = summ(c, d)
        prom_res.pop(1)


    a.reverse()
    b.reverse()

    return prom_res[0]



a = 'A2'
b = 'C4F'

a = list(a)
b = list(b)

chisla = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
znachenie = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}


print(f'Умножение двух шестнадцатеричных чисел {"".join(a)} и {"".join(b)} равняется {"".join(mult(a, b))}')
print(f'Сумма двух шестнадцатеричных чисел {"".join(a)} и {"".join(b)} равняется {"".join(summ(a, b))}')



