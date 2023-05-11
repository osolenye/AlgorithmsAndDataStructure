import math

lst = []
a = int(input())
b = int(input())
step = float(input())
for i in range(a, b+1):
    y = i*math.sin(i)-i/2 * math.cos(i/2)
    lst.append(y)
    a += step


print(f'в точке {min(lst)} достигается минимум функции')
print(f'в точке {max(lst)} достигается максимум функции')


#pls