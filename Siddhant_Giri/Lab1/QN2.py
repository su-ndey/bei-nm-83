def f(x):
    return x**3 - x - 2

a = 1
b = 2
tolerance = 0.0001
max_iter = 100

if f(a) * f(b) >= 0:
    print("Invalid interval. Root is not bracketed.")

else:
    for i in range(max_iter):

        c = (a * f(b) - b * f(a)) / (f(b) - f(a))

        print(f"Iteration {i+1}: c = {c}")

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