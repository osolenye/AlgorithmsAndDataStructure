import math

a = []
for i in range(1, 26):
    a.append(i)


maxChet = 0
maxNeChet = 0
for j in a:
    if (j%2==0 and j>maxChet):
        maxChet = j
    if (j%2!=0 and j>maxNeChet):
        maxNeChet = j

# print(maxChet)
# print(maxNeChet)

numberMin = min(maxChet, maxNeChet)
numberMax = max(maxChet, maxNeChet)
c = []

for k in range(1,numberMin):
    c.append(k)

for k in range(numberMax, 25):
    c.append(k)

counter = 0
arithmeticAverage =0
for i in c:
    arithmeticAverage += k
    counter += 1

print(c)
print(maxChet)
print(maxNeChet)
print(arithmeticAverage/counter)
#123
