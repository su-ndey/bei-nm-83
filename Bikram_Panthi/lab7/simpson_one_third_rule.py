# Lab 7 (Task 2) - Simpson's 1/3 Rule
# f(x) = 1 / (1 + x^3),  n must be EVEN
# Area = (h/3) * [ f(x0) + f(xn) + 4*(odd terms) + 2*(even terms) ]


def f(x):
    return 1 / (1 + x**3)


x0 = 0.0     # lower limit
xn = 1.0     # upper limit
n = 6        # number of sub-intervals (must be even)

if n % 2 != 0:
    raise ValueError("n must be even")

h = (xn - x0) / n
result = f(x0) + f(xn)

for i in range(1, n):
    x = x0 + i * h
    if i % 2 == 0:
        result += 2 * f(x)
    else:
        result += 4 * f(x)

area = (h / 3) * result
print(f"Area under curve (Simpson 1/3, n={n}): {area:.4f}")
