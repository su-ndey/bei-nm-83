def f(x):
    return x**3 - x - 2
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
tolerance = 0.001
max_iter = 100
if f(a) * f(b) >= 0:
    print("Invalid interval. Root is not bracketed.")
else:
    for i in range(max_iter):
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        if f(c) == 0:
            print("Exact root found:", c)
            print("Number of iterations:", i + 1)
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        if abs(f(c)) < tolerance:
            print("Approximate root:", c)
            print("Number of iterations:", i + 1)
            break