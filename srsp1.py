import math

a = float(input())
b = float(input())

c = (a+b)/2
pogr = float(input())
d = pogr*0.1

def f(x):
    return (math.sin(2*x)-x)

counter = 0

while(b-a)>pogr:
    x1 = ((a+b)/2) - d
    f1 = f(x1)
    x2 = ((a+b)/2) + d
    f2 = f(x2)
    if f1<f2:
        b = x2
    if f1>=f2:
        a = x1
    counter += 1
print(counter)

x = (a+b)/2
print(x)
print(f(x))
