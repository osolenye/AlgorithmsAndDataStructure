import random

value = random.randint(10, 15)
array = []
for i in range(value):
    array.append(random.randint(0, 99))

print("количество элементов массива ", value)
print("неотсортированный массив ", array)

counter = 0
left = 0
right = len(array) - 1
while left <= right:
    for i in range(left, right, +1):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
            counter+=1
            print(counter, array)
    right -= 1
    for i in range(right, left, -1):
        if array[i - 1] > array[i]:
            array[i], array[i - 1] = array[i - 1], array[i]
            counter+=1
            print(counter, array)
    left += 1
print(array)