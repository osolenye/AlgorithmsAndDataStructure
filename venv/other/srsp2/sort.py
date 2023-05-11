import random

value = random.randint(10, 15)
s = []
print("Количество элементов массива: "+str(value))


for i in range(value):
    s.append(random.randint(0, 99))
print("Неотсортированный массив: "+str(s))
array=s
gnome_array = s

#merge sort
def merge_two_list(a, b):
    c = []
    i = 0
    j = 0
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            c.append(a[i])
            i+=1
        else:
            c.append(b[j])
            j+=1
    if i<len(a):
        c += a[i:]
    elif j<len(b):
        c += b[j:]
    print(c)
    return c

def merge_sort(s):
    if len(s)==1:
        return s
    middle = len(s)//2
    left = merge_sort(s[:middle])
    right = merge_sort(s[middle:])
    return merge_two_list(left, right)


print("сортировка слиянием: ",merge_sort(s))

counter = 0
#mix sort
mix_left = 0
mix_right = len(array) - 1
while mix_left <= mix_right:
    for i in range(mix_left, mix_right, +1):
        #print(array)
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
            counter += 1
            print(counter, array)
    mix_right -= 1
    for i in range(mix_right, mix_left, -1):
        if array[i - 1] > array[i]:
            array[i], array[i - 1] = array[i - 1], array[i]
            counter += 1
            print(counter, array)
    mix_left += 1
print("сортировка коктейлем", array)

#gnome_sort
counter = 0
index = 1
i = 0
n = len(gnome_array)
while i<n-1:
    if gnome_array[i]<=gnome_array[i+1]:
        i, index = index, index+1
    else:
        gnome_array[i], gnome_array[i+1] = gnome_array[i+1], gnome_array[i]
        i = i-1
        if i<0:
            i, index = index, index+1
    counter += 1
    print(counter, array)

print("гномья сортировка: ",gnome_array)