import math


def func(x):
    return x**3-x
    return (x-2)**2


def der1(x):
    return 3*(x**2)-1
    return 2*x-4


def der2(x):
    return 6*x
    return 2


def newtonRaphson(x0, a, b, eps):
    print("Newton-Raphson method: ")
    x1 = x0
    counter = 0

    while True:
        x0 = x1
        x1 = x0 - der1(x0) / der2(x0)

        if x1 < a:
            x1 = a
        elif x1 > b:
            x1 = b
        counter += 1
        print(f"Iteration {counter}\t x1 = {x1}\t fx1 = {func(x1)}")
        if abs(x1 - x0) <= eps:
            break

def newton(x, eps):
    i = 0
    while abs(der1(x)) > eps:
        x = x - der1(x) / der2(x)
        i += 1
        print(f"Iteration {i} x1 = {x} f(x) = {func(x):.10f}")
    return x
print("newton")
print(newton(0.01, 0.0000001))


def midpointMethod(a, b, eps):
    print("\nMidpoint method: ")
    L = a
    R = b
    z, fz = 0, 0
    counter = 0

    while True:
        z = (R + L) / 2
        fz = der1(z)
        if fz > 0:
            R = z
        elif fz < 0:
            L = z
        if z == a or z == b:
            break
        counter += 1
        print(f"Iteration {counter}\t x1 = {z}\t fx1 = {func(z)}")
        if abs(fz) <= eps:
            break


def secant_method(x0, x1, eps):
    print("\nSecant method: ")
    counter = 0

    while True:
        x2 = x1 - der1(x1) * (x1 - x0) / (der1(x1) - der1(x0))
        x0 = x1
        x1 = x2
        counter += 1
        print(f"Iteration {counter}\t x1 = {x1}\t fx1 = {func(x1)}")
        if abs(x1 - x0) <= eps:
            break


def quadraticApproximationMethod(x1, x3, x2):
    # print("\nquadraticApproximationMethod: ")
    fx1 = func(x1)
    fx2 = func(x2)
    fx3 = func(x3)
    a1 = (fx2 - fx1) / (x2 - x1)
    a2 = (1 / (x3 - x2)) * (((fx3 - fx1) / (x3 - x1)) - ((fx2 - fx1) / (x2 - x1)))
    xopt = (x2 + x1) / 2 - (a1 / (2 * a2))
    return xopt


def PowellMethod(x1, x2, x3, dx, eps):
    print("\nPowellMethod: ")
    counter = 0

    a = x1
    b = x2

    fx1 = func(x1)
    fx2 = func(x2)
    fx3 = func(x3)

    if fx1 > fx2:
        x3 = x1 + 2 * dx
    elif fx1 < fx2:
        x3 = x1 - dx

    fmin = 0
    xmin = 0

    while True:
        counter += 1
        print(f"Iterations: {counter} x1 = {x1} f1 = {fx1} x2 = {x2} f2 = {fx2} x3 = {x3} f3 = {fx3}")

        xopt = quadraticApproximationMethod(x1, x3, x2)
        fopt = func(xopt)

        if x1 < a:
            x1 = a
        if x2 > b:
            x2 = b
        if x3 < x1 or x3 > x2:
            x3 = (x1 + x2) / 2.0

        if fx1 and fx2 > fx3:
            fmin = fx3
            xmin = x3
        elif fx2 and fx3 > fx1:
            fmin = fx1
            xmin = x1
        elif fx1 and fx3 > fx2:
            fmin = fx2
            xmin = x2

        if xopt > x2:
            x1 = x2
            fx1 = fx2
            x2 = xopt
            fx2 = fopt
        else:
            x3 = x2
            fx3 = fx2
            x2 = xopt
            fx2 = fopt

        if abs(fmin - fopt) <= eps and abs(xmin - xopt) <= eps:
            break

    print(f"\nMinimum found: x = {x1}, f(x) = {fx1}")


if __name__ == "__main__":
    a, b, eps, dx = 0.01, 1,  0.0000000001, 0.0001
    c = (b - a) / 2
    x0= b
    newtonRaphson(x0, b, a, eps)
    midpointMethod(a, b, eps)
    secant_method(a, b, eps)
    PowellMethod(a, b, c, dx, eps)


