n = int(input())
a = []

for i in range(n):
    num = int(input())
    a.append(num)
print(a)

maxChet = a[0]
for i in a:
    if (i>maxChet and i%2==0):
        maxChet = i
print(maxChet)

maxNechet = a[0]
for j in a:
    if (j>maxNechet and j%2!=0):
        maxNechet = j
print(maxNechet)

mas = []
for i in range(0, min(a.index(maxChet), a.index(maxNechet))):
    mas.append(a[i])
for j in range(max(a.index(maxChet), a.index(maxNechet))+1, n):
    mas.append(a[j])
print(mas)

summa = 0
counter = 0
for i in mas:
    summa += i
    counter += 1
print(summa/counter)
