import math
def f(x):
    return x * math.sin(x) + math.cos(x)

a = 2
b = 3
tolerance = 0.0001
max_iter = 100

if f(a) * f(b) >= 0:
    print("Invalid interval. Root is not bracketed.")
else:
    print(f"{'a':<12}{'b':<12}{'c':<12}{'f(c)':<12}")
    print("-" * 48)

    for i in range(max_iter):
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        print(f"{a:<12.6f}{b:<12.6f}{c:<12.6f}{f(c):<12.6f}")

        if f(c) == 0:
            print("Exact root found:", c)
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

        if abs(b - a) < tolerance:
            print("Approximate root:", c)
            break