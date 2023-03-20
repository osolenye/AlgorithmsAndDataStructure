import random

value = random.randint(10, 15)
array = []

for i in range(value):
    array.append(random.randint(0, 99))

maximum = 0
counter = 0
for i in range(len(array)):
    if array[i]>maximum:
        maximum = array[i]
        counter = i

print(value)
print(array)
print(maximum)
print(counter)
if (counter!=0):
    array.pop(counter-1)
else:
    print("Didn't delete anything.")
print(array)

