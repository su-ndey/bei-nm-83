# Lab 1 - Bracketing Methods
# False Position Method (Regula-Falsi)
# Equation: f(x) = x^3 - x - 2 = 0   (root is near x = 1.521)
#
# Note: in the false position method one endpoint usually stays fixed, so the
# test |b - a| < tol never becomes true and the loop would never stop. I have
# therefore used |c_new - c_old| < tol as the convergence test, which is the
# correct criterion for this method.


def f(x):
    return x**3 - x - 2


a = 1
b = 2
tolerance = 0.0001
max_iter = 100

if f(a) * f(b) >= 0:
    print("Invalid interval. Root is not bracketed.")
else:
    c_old = a

    for i in range(max_iter):

        c = (a * f(b) - b * f(a)) / (f(b) - f(a))

        print(f"Iteration {i + 1}: c = {c}")

        # Exact root case
        if f(c) == 0:
            print("Exact root found:", c)
            break

        # Error condition
        if abs(c - c_old) < tolerance:
            print("Approximate root:", c)
            break

        # Root lies in left interval
        if f(a) * f(c) < 0:
            b = c

        # Root lies in right interval
        else:
            a = c

        c_old = c
