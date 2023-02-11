import math

min = int(input())
max = int(input())
step = float(input())
sum = 0
count = 0
proizv = 1
for i in range(min,max+1,step):
    y = i**2*math.e**(math.sin(i)+math.cos(i))
    sum += y
    count += 1
    print(f'x = {i}, y = {y}, сумма = {sum}, прогрессия меняется вот так: {round((sum/count),3)}')
print('итоговая арифметическое среднее = '+str(sum/count))
count = 0
for i in range(min,max+1,step):
    y = i**2*math.e**(math.sin(i)+math.cos(i))
    proizv = proizv*y
    count += 1
    print(f'x = {i}, y = {y}, произведение  = {proizv}, прогрессия меняется вот так: {round(proizv**(1/count), 3)}')
print('итоговая геометрическое среднее = '+str(proizv**(1/count)))