a = int(input())
b = int(input())
dx = int(input())

negative = []
positive = []

for x in range(a, b+1, dx):
    y = 2*x**3 - x**2 - 3*x
    if y<0:
        negative.append(y)
    elif y>0:
        positive.append(y)

maxNegative = negative[0]
minPositive = positive[0]
maxArgument = 0
minArgument = 0


for i in negative:
    if maxNegative<i:
        maxNegative = i
        maxArgument = i

for j in positive:
    if minPositive>j:
        minPositive = j
        minArgument = j

print(maxNegative, maxArgument)
print(minPositive, minArgument)