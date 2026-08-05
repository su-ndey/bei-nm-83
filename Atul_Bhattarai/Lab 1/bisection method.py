import math

def f(x):
    return x**3 - 4*x - 9  # Example function: f(x) = x^3 - 4x - 9

a = 2
b = 3
tolerance = 0.001
max_iter = 11 

if f(a) * f(b) >= 0:
    print("Invalid interval. Root is not bracketed.")
else:
    print(f"{'a':<10}{'b':<10}{'f(a)':<12}{'f(b)':<12}{'c':<10}{'f(c)':<12}")
    print("-" * 66)

    for i in range(max_iter):
        c = (a + b) / 2

        print(f"{a:<10.6f}{b:<10.6f}{f(a):<12.6f}{f(b):<12.6f}{c:<10.6f}{f(c):<12.6f}")

        if f(c) == 0:
            print("\nExact root found =", c)
            break

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        if abs(b - a) < tolerance:
            print("\nApproximate root =", c)
            break