print('задание 1')
a = input()
array = []
for i in a:
    if i.isdigit():
        array.append(int(i))
print(min(array))
print(max(array))
print(sum(array))


print('задание 2')
a = input().split(' ')
array = []
result = []
for i in a:
    array.append(int(i))
for i in range(0, len(array)):
    if array.count(array[i])>1:
        result.append(array[i])
print(result)

print('задание 3')
a = input().split(',')
print(a)
array = []
chet = []
nechet = []
for j in a:
    array.append(int(j))
for i in array:
    if i%2==0:
        chet.append(i)
    else:
        nechet.append(i)
print(*chet)
print(*nechet)

print('задание 4')
a = input()
array = []
for i in a:
    array.append(i)
for i in array:
    if array.count(i)>2:
        for j in range(array.count(i)-2):
            array.remove(i)
print(*array,sep = '')

print('задание 5')
st = list(input())
err = st.index('#')
del st[err]
sp = ''.join(st)
word = max(sp.split(), key=len)
print(sp)
print(word)

print("задание 6")
array = input().split(' ')
result = []
for i in range(len(array)-1):
    if array[i].isalpha():
        result.append(array[i])

result.sort(key=len)
print(*result)

print('задание 7')
vowels = 'аиеёоуыэюя'
st = input().split()
lst1 = []
lst2 = []
for i in st:
    if i[0] in vowels:
        lst1.append(i)
    else:
        lst2.append(i)
print(lst1)
print(lst2)

print('задание 8')
keys = ['модель', 'цена', 'количество', 'размер', 'цвет', 'скидка']
values = ['XXLDude', 5678.00, 57, 'XXL', 'черный', '12%']
for i in range(len(keys)):
    print(keys[i], ": ", values[i])

print('задание 9')
a = input().split(' ')
array = []
for i in a:
    if i.isdigit():
        array.append(int(i))
print(sum(array)/len(array))

print('задание 10')
route = input().split()
s = sum([int(i[1:]) for i in route if i[0] == 's'])
n = sum([int(i[1:]) for i in route if i[0] == 'n'])
w = sum([int(i[1:]) for i in route if i[0] == 'w'])
e = sum([int(i[1:]) for i in route if i[0] == 'e'])
print(f'x: {e - w}, y: {n - s}')
