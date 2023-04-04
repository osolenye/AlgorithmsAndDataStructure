import math

# x1 = float(input())
# x3 = float(input())
# x2 = 2.1
# pogr = float(input())
# d = pogr * 0.1
# counter = 0
x1 = -2
x3 = 20
x2 = 2.1
pogr = 0.0001
d = pogr * 0.1
counter = 0


def f(x):
    return (x - 2) ** 2


def approximation(x1,x2,x3,d):
    while abs(x3 - x1) > d:
        f1 = f(x1)
        f2 = f(x2)
        f3 = f(x3)
        a = (f3 - (f2 * x3 - f1 * x3 - f2 * x1 + f1 * x2) / (x2 - x1)) / ((x3 - x1) * (x3 - x2))
        b = (f2 - f1) / (x2 - x1) - a * (x1 + x2)
        c = f1 - a * x1 ** 2 - b * x1

        x = -b / (2 * a)

        if x < x1 or x > x3:
            if abs(x - x1) < abs(x - x3):
                x = x1
            else:
                x = x3

        f4 = f(x)

        if x < x2:
            if f4 < f2:
                x3 = x2
                x2 = x
            else:
                x1 = x
        else:
            if f4 < f2:
                x1 = x2
                x2 = x
            else:
                x3 = x
        return x2, f(x2)

print(approximation(x1,x2,x3,d))

