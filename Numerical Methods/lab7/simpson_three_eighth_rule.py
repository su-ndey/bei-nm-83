# Lab 7 (Task 3) - Simpson's 3/8 Rule
# f(x) = 1 / (1 + x^3),  n must be DIVISIBLE BY 3
# Area = (3h/8) * [ f(x0) + f(xn) + 2*(every 3rd term) + 3*(all others) ]


def f(x):
    return 1 / (1 + x**3)


x0 = 0.0     # lower limit
xn = 1.0     # upper limit
n = 6        # number of sub-intervals (must be divisible by 3)

if n % 3 != 0:
    raise ValueError("n must be divisible by 3")

h = (xn - x0) / n
result = f(x0) + f(xn)

for i in range(1, n):
    x = x0 + i * h
    if i % 3 == 0:
        result += 2 * f(x)
    else:
        result += 3 * f(x)

area = (3 * h / 8) * result
print(f"Area under curve (Simpson 3/8, n={n}): {area:.4f}")
