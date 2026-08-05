import math

def f(x):
    return x * math.sin(x) + math.cos(x)

x0 = 2.0
x1 = 3.0

def bisection_method(a, b, tol=1e-6, max_iter=100):
    fa = f(a)
    fb = f(b)

    if fa * fb > 0:
        print("Bisection method requires the value of a and b so f(a) and f(b)must have opposite signs.")
        return None, None

    for iteration in range(1, max_iter + 1):
        c = (a + b) / 2.0
        fc = f(c)

        if abs(fc) < tol or (b - a) / 2.0 < tol:
            return c, iteration

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    print(f"Will not converge after {max_iter} iterations")
    return None, None

def regula_falsi_method(a, b, tol=1e-6, max_iter=100):
    fa = f(a)
    fb = f(b)

    if fa * fb > 0:
        print("It requires the value of a and b so f(a) and f(b)  must have opposite signs.")
        return None, None

    c = a
    for iteration in range(1, max_iter + 1):
        c = (a * fb - b * fa) / (fb - fa)
        fc = f(c)

        if abs(fc) < tol or abs(b - a) < tol:
            return c, iteration

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    print(f"This method did not converge after {max_iter} iterations")
    return None, None

root, iterations = regula_falsi_method(x0, x1)
print(f"Root found (Regula Falsi): {root}")
print(f"Iterations = {iterations}")
