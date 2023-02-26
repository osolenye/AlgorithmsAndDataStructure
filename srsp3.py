def f(x):
    return (x-2)**2

a = int(input())
b = int(input())
n = int(input())
tol = 0.0000001


x1 = ((b-a)*f(n-1)+tol*(-1)**n)/f(n)+a
x0 = a
x3 = b
f1 = f(x1)
x2 = x0 - x1 + x3
f2 = f(x2)
counter = 0
while (counter)<n:
    x2 = x0 - x1 + x3
    f2 = f(x2)
    if f2>f1:
        if x2>x1:
            x3 = x2
        elif x2<x1:
            x0 = x2
    elif f2<f1:
        if x1>x2:
            x3 = x1
            x1 = x2
            f1 = f(x2)
        elif x1<x2:
            x0 = x1
            x1 = x2
            f1 = f(x2)
    counter += 1
    print(counter)
    print(round(x0, 8), round(x3, 8))
    print(round(f1, 8), round(f2, 8))
    # print((x0+x3)/2)
    # print((f1+f2)/2)


