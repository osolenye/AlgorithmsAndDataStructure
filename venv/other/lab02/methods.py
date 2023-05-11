import math


def f(x):
    return (x-2)**2


def f1(x):
    return 2*x-4


def f2(x):
    return 2


def newtonRaphson(x0, a, b, eps):
    print("Метод Ньютона Рафсона")
    x1 = x0
    counter = 0

    while True:
        x0 = x1
        x1 = x0 - f1(x0) / f2(x0)

        if x1 < a:
            x1 = a
        elif x1 > b:
            x1 = b
        counter += 1
        print(f"номер итерации: {counter} x1: {x1} f(x1): {f(x1)}")
        if abs(f1(x0)) <= eps:
            break


def newton(x, eps):
    print("Ньютон")
    i = 0
    while abs(f1(x)) > eps:
        x = x - f1(x) / f2(x)
        i += 1
        print(f"номер итерации: {i} x1: {x} f(x): {f(x)}")
    return x


def midpoint(a, b, eps):
    print("Метод средней точки")
    L = a
    R = b
    z, fz = 0, 0
    counter = 0

    while True:
        z = (R + L) / 2
        fz = f1(z)
        if fz > 0:
            R = z
        elif fz < 0:
            L = z
        if z == a or z == b:
            break
        counter += 1
        print(f"номер итерации: {counter} x1: {z} f(x1): {f(z)}")
        if abs(fz) <= eps:
            break


def sec_method(x0, x1, eps):
    print("Метод секущих")
    counter = 0

    while True:
        x2 = x1 - f1(x1) * (x1 - x0) / (f1(x1) - f1(x0))
        x0 = x1
        x1 = x2
        counter += 1
        print(f"номер итерации: {counter} x1: {x1} fx1: {f(x1)}")
        if abs(x1 - x0) <= eps:
            break


def quadraticApproximationMethod(x1, x3, x2):
    fx1 = f(x1)
    fx2 = f(x2)
    fx3 = f(x3)
    a1 = (fx2 - fx1) / (x2 - x1)
    a2 = (1 / (x3 - x2)) * (((fx3 - fx1) / (x3 - x1)) - ((fx2 - fx1) / (x2 - x1)))
    xopt = (x2 + x1) / 2 - (a1 / (2 * a2))
    return xopt







a = -2
b = 2
eps = 0.0001
dx = 0.0001
c = (b - a) / 2
x0= b
print(newton(0.01, 0.0000001))
newtonRaphson(x0, b, a, eps)
midpoint(a, b, eps)
sec_method(a, b, eps)



