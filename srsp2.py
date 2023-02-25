import math

a = float(input())
b = float(input())
pogr  = float(input())

def f(x):
    return math.sin(2*x)-x

k2 = (math.sqrt(5)-1)/2
k1 = 1-k2
x1 = a+k1*(b-a)
x2 = a+k2*(b-a)
f1 = f(x1)
f2 = f(x2)

while (b-a)<pogr:
    if f1<f2:
        b = x2
        x2 = x1
        f2 = f1
        x1 = a+k1*(b-a)
        f1 = f(x1)
    else:
        a = x1
        x1 = x2
        f1 = f2
        x2 = a+k2*(b-a)
        f2 = f(x2)
x = (a+b)/2
y = f(x)
print(x, y)




