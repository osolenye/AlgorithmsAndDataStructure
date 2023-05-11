import random

value = random.randint(10, 15)
array = []

for i in range(value):
    array.append(random.randint(0, 99))

print("неотсортированный массив ", array)
print("количество элементов массива ", value)

counter = 0
index = 1
i = 0
n = len(array)
while i<n-1:
    if array[i]<=array[i+1]:
        i, index = index, index+1
    else:
        array[i], array[i+1] = array[i+1], array[i]
        i = i-1
        if i<0:
            i, index = index, index+1
    
    counter += 1
    print(counter, array)
print(array)
