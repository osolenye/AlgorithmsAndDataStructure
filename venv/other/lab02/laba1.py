def f(x):
    return (x-2)**2
def f1(x):
    return 2*x-4

def f2(x):
    return x

def midpoint(f, a, b, eps=1e-5, iterations=100):
    print("метод средней точки")
    for i in range(iterations):
        c = (a + b) / 2
        if abs(f(c)) < eps:
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c

x_minimum = midpoint(f, -2, 2)
print("Минимум функции:", f(x_minimum), "x: ", x_minimum)

def quadraticApproximationMethod(x1, x3, x2):
    print("квадратная аппроксимация")
    fx1 = f(x1)
    fx2 = f(x2)
    fx3 = f(x3)
    a1 = (fx2 - fx1) / (x2 - x1)
    a2 = (1 / (x3 - x2)) * (((fx3 - fx1) / (x3 - x1)) - ((fx2 - fx1) / (x2 - x1)))
    x_min = (x2 + x1) / 2 - (a1 / (2 * a2))
    return "минимум х: ", x_min, "минимальная функция: ", f(x_min)
print(quadraticApproximationMethod(-2, 2, 0.01))


def newton_raphson(x0, eps=1e-5, max_iter=100):
    print("newton raphson")
    x_old = x0
    for i in range(max_iter):
        x_new = x_old - f1(x_old) / f2(x_old)
        if abs(x_new - x_old) < eps:
            break
        x_old = x_new
    return x_new

x_min = newton_raphson(2)
print("Минимум функции:", f(x_min), "минимум х: ", x_min)





print("метод Пауэлла")
def powell():
    a = 0
    x1 = a
    step = 0.09
    eps = 0.01

    while True:
        x2 = x1 + step
        f1 = f(x1)
        f2 = f(x2)

        if f1 > f2:
            x3 = x1 + 2 * step
        elif f1 < f2:
            x3 = x1 - step

        f3 = f(x3)

        if f1 < f2 and f1 < f3:
            fmin = f1
            xmin = x1
        elif f2 < f1 and f2 < f3:
            fmin = f2
            xmin = x2
        else:
            fmin = f3
            xmin = x3

        a1 = (f2 - f1) / (x2 - x1)
        a2 = 1 / (x3 - x2) * ((f3 - f1) / (x3 - x1) - a1)
        xopt = (x2 + x1) / 2 - a1 / (2 * a2)
        fopt = f(xopt)

        if fopt < fmin:
            x1 = xopt
        elif fopt > fmin:
            x1 = xmin

        if abs(xopt - xmin) < eps:
            print("x минимальный: ", xmin, "минимальная функция: ", f(xmin))
            break

powell()
