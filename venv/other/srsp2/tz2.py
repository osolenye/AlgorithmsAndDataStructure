import random

value = random.randint(10,15)
array = []

for i in range(value):
    array.append(random.randint(0, 99))

counter = 0
# print("неизмененный массив: "+str(array))
array.insert(random.randint(0, len(array)), 0)
for j in range(len(array)):
    if array[j] == 0:
        break;
    counter += 1


print("Количество элементов массива: "+str(value))
print("Массив: "+str(array))
print("Индекс нулевого элемента: "+str(counter))

number = int(input("добавить элемент: "))
if (array[0]!=0):
    for i in range(0, array.index(0)*2+1, 2):
        array.insert(i, number)
    array.pop(0)

else:
    print("Impossible to add numbers after elements")
print("Массив с добавлением указанного числа до нулевого элемента: "+str(array))
