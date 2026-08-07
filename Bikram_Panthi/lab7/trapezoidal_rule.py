# Lab 7 (Task 1) - Trapezoidal Rule
# f(x) = 1 / (1 + x^3),  Area = (h/2) * [ f(x0) + f(xn) + 2*sum(interior) ]
#
# I have set the limits as variables at the top instead of reading them with
# input(), so the file runs directly in VS Code. Change them as needed.
# Each interior point carries a weight of 2 in this formula.


def f(x):
    return 1 / (1 + x**3)


x0 = 0.0     # lower limit
xn = 1.0     # upper limit
n = 6        # number of sub-intervals

h = (xn - x0) / n
result = f(x0) + f(xn)

for i in range(1, n):
    x = x0 + i * h
    result += 2 * f(x)

area = (h / 2) * result
print(f"Area under curve (Trapezoidal, n={n}): {area:.4f}")
