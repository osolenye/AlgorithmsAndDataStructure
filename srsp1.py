import math

a = float(input())
b = float(input())
pogr = float(input())


d = pogr*0.1

def f(x):
    return (x-2)**2

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
    print()
    counter += 1
    print(counter)
    # print(round(x1, 8), round(f(x1), 8))
    # print(round(x2, 8), round(f(x2), 8))
    print(round(b-a, 8))
    # x = (a + b) / 2
    # print(x)
    # print(f(x))
x = (a+b)/2
print(x)
print(f(x))
